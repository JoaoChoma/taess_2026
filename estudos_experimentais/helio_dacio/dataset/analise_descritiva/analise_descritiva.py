# Análise descritiva e verificação de normalidade — Experimento i-toMicroservices (persona P1)
# Entrada: os CSVs de indicadores por execução (um por sistema), com as colunas
#   config, repeticao, geracao, hv, igd_plus, ed_media  (arquivos fornecidos pelo responsável pelo projeto)
# Saída (pasta SAIDA):
#   estatistica_descritiva.csv          média, mediana, desvio-padrão, Q1, Q3, IQR, mínimo e máximo
#   boxplots_<sistema>.png/.pdf          boxplot de HV, IGD+ e ED média por configuração (com os 5 pontos)
#   normalidade_<sistema>_<ind>.png/.pdf histograma + Q-Q plot por configuração (p do Shapiro-Wilk no título)
#   residuos_<sistema>_<ind>.png/.pdf    histograma (com curva normal) + Q-Q plot dos 40 resíduos
import os
import numpy as np, pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats

# ---------------------------------------------------------------- 1) caminhos
PASTA_DADOS = 'dados'                    # onde estão os CSVs
SAIDA       = 'saida'                    # onde salvar as figuras e a tabela
ARQUIVOS = {'spring-petclinic': 'P1-Reflective-Architect_spring-petclinic.csv',
            'jpetstore':        'P1-Reflective-Architect_jpetstore.csv'}

# ---------------------------------------------------------------- 2) configurações e estilo
IDS = ['nsgaiii__elit_on__penalty', 'nsgaiii__elit_off__penalty', 'rnsgaiii__elit_on__penalty', 'rnsgaiii__elit_off__penalty',
       'nsgaiii__elit_on__kill', 'nsgaiii__elit_off__kill', 'rnsgaiii__elit_on__kill', 'rnsgaiii__elit_off__kill']
CFG = {c: f'C{i+1}' for i, c in enumerate(IDS)}
IND = [('hv', 'HV (maior é melhor)'), ('igd_plus', 'IGD+ (menor é melhor)'), ('ed_media', 'ED média (menor é melhor)')]
COL = ['#2a78d6', '#eb6834', '#1baf7a', '#eda100', '#e87ba4', '#008300', '#6250d6', '#e34948']
TXT, MUT = '#1f1f1e', '#6b6a63'
plt.rcParams.update({'pdf.fonttype': 42, 'font.size': 9, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.edgecolor': MUT})
virgula = lambda x, n=3: f'{x:.{n}f}'.replace('.', ',')

def carregar(sistema):
    d = pd.read_csv(os.path.join(PASTA_DADOS, ARQUIVOS[sistema]))
    d = d[d.geracao == 999].copy()
    d['C'] = d.config.map(CFG)
    assert len(d) == 40 and d.groupby('C').size().eq(5).all(), 'esperava 8 configurações x 5 execuções'
    return d

# ---------------------------------------------------------------- 3) estatística descritiva
def descritiva(d, sistema):
    linhas = []
    for ind, _ in IND:
        for c in [f'C{k}' for k in range(1, 9)]:
            v = d[d.C == c][ind].values
            q1, q3 = np.percentile(v, [25, 75])
            linhas.append(dict(sistema=sistema, config=c, indicador=ind, n=len(v), media=v.mean(), mediana=np.median(v),
                               desvio_padrao=v.std(ddof=1), q1=q1, q3=q3, iqr=q3 - q1, minimo=v.min(), maximo=v.max(),
                               shapiro_p=stats.shapiro(v).pvalue))
    return linhas

# ---------------------------------------------------------------- 4) boxplots
def boxplots(d, sistema):
    fig, axs = plt.subplots(1, 3, figsize=(15, 4.6))
    for ax, (ind, tit) in zip(axs, IND):
        dados = [d[d.C == f'C{k}'][ind].values for k in range(1, 9)]
        b = ax.boxplot(dados, widths=0.55, patch_artist=True, showfliers=False,
                       medianprops=dict(color=TXT, lw=1.5), whiskerprops=dict(color=MUT), capprops=dict(color=MUT))
        for k, p in enumerate(b['boxes']):
            p.set_facecolor(COL[k]); p.set_alpha(0.55); p.set_edgecolor(COL[k])
        for k, v in enumerate(dados):
            ax.scatter([k + 1] * len(v), v, color=COL[k], s=20, zorder=3, edgecolor='white', lw=0.7)
        ax.set_xticks(range(1, 9)); ax.set_xticklabels([f'C{k}' for k in range(1, 9)])
        ax.axvline(4.5, color=MUT, lw=0.8, ls='--')
        ax.text(2.5, 1.0, 'PENALTY', transform=ax.get_xaxis_transform(), ha='center', va='bottom', color=MUT, fontsize=8)
        ax.text(6.5, 1.0, 'KILL', transform=ax.get_xaxis_transform(), ha='center', va='bottom', color=MUT, fontsize=8)
        ax.set_title(tit, loc='left', pad=16, color=TXT)
    fig.suptitle(f'{sistema} — indicadores por configuração (5 execuções; pontos = execuções)', x=0.01, ha='left', fontsize=11)
    fig.tight_layout()
    for ext in ('png', 'pdf'):
        fig.savefig(os.path.join(SAIDA, f'boxplots_{sistema}.{ext}'), dpi=200)
    plt.close(fig)

# ---------------------------------------------------------------- 5) normalidade por configuração
def normalidade(d, sistema):
    for ind, tit in IND:
        fig, axs = plt.subplots(2, 8, figsize=(16, 4.6))
        for k in range(8):
            v = np.sort(d[d.C == f'C{k+1}'][ind].values); p = stats.shapiro(v).pvalue
            ax = axs[0, k]; ax.hist(v, bins='auto', color=COL[k], alpha=0.75, edgecolor='white')
            ax.set_title(f'C{k+1}  (SW p = {virgula(p)})', fontsize=8.5, color='#c00000' if p <= 0.05 else TXT)
            ax.tick_params(labelsize=7)
            (osm, osr), (sl, ic, _) = stats.probplot(v, dist='norm')
            ax = axs[1, k]; ax.scatter(osm, osr, color=COL[k], s=18, zorder=3); ax.plot(osm, sl * np.array(osm) + ic, color=MUT, lw=1)
            ax.tick_params(labelsize=7); ax.set_xlabel('quantis teóricos', fontsize=7.5)
        axs[0, 0].set_ylabel('frequência'); axs[1, 0].set_ylabel('valores observados')
        fig.suptitle(f'{sistema} — {tit.split(" (")[0]}: histograma (em cima) e Q-Q plot (embaixo) por configuração', x=0.01, ha='left', fontsize=10)
        fig.tight_layout()
        for ext in ('png', 'pdf'):
            fig.savefig(os.path.join(SAIDA, f'normalidade_{sistema}_{ind}.{ext}'), dpi=200)
        plt.close(fig)

# ---------------------------------------------------------------- 6) normalidade dos resíduos
def residuos(d, sistema):
    for ind, tit in IND:
        nome = tit.split(' (')[0]
        r = (d[ind] - d.groupby('C')[ind].transform('mean')).values
        p = stats.shapiro(r).pvalue
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4))
        a1.hist(r, bins='auto', density=True, color='#4a7fc1', edgecolor='white', alpha=0.85)
        x = np.linspace(r.min() * 1.1, r.max() * 1.1, 200)
        a1.plot(x, stats.norm.pdf(x, r.mean(), r.std(ddof=1)), color='#d6336c', lw=2)
        a1.set_xlabel(f'resíduo do {nome} (valor − média da configuração)'); a1.set_ylabel('densidade')
        (osm, osr), (sl, ic, _) = stats.probplot(r, dist='norm')
        a2.scatter(osm, osr, color='#4a7fc1', s=20, zorder=3); a2.plot(osm, sl * np.array(osm) + ic, '--', color='#d6336c', lw=1.5)
        a2.set_xlabel('quantis teóricos (normal)'); a2.set_ylabel('quantis observados')
        fig.suptitle(f'{sistema} — {nome}: 40 resíduos (8 configurações × 5 execuções) · Shapiro-Wilk p = {virgula(p)}', x=0.01, ha='left', fontsize=10)
        fig.tight_layout()
        for ext in ('png', 'pdf'):
            fig.savefig(os.path.join(SAIDA, f'residuos_{sistema}_{ind}.{ext}'), dpi=200)
        plt.close(fig)

# ---------------------------------------------------------------- 7) execução
if __name__ == '__main__':
    os.makedirs(SAIDA, exist_ok=True)
    tabela = []
    for sistema in ARQUIVOS:
        d = carregar(sistema)
        tabela += descritiva(d, sistema)
        boxplots(d, sistema); normalidade(d, sistema); residuos(d, sistema)
    t = pd.DataFrame(tabela)
    t.to_csv(os.path.join(SAIDA, 'estatistica_descritiva.csv'), sep=';', decimal=',', index=False, float_format='%.4f')
    print('Arquivos gerados em', os.path.abspath(SAIDA)); print(sorted(os.listdir(SAIDA)))
