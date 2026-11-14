import json
import subprocess
import sys
import zipfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

RAIZ = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "analise").resolve()
DADOS = RAIZ / "persona_3"
SCRIPT_OFICIAL = RAIZ / "script-analise-resultado-i-toMicroservices"
SAIDA = Path(__file__).resolve().parent / "saida"
FIG = SAIDA / "figuras"
PERSONA = "P3-Fast-Domain-Extractor"

CONFIGS = {
    "C1": "nsgaiii__elit_on__penalty",
    "C2": "nsgaiii__elit_off__penalty",
    "C3": "rnsgaiii__elit_on__penalty",
    "C4": "rnsgaiii__elit_off__penalty",
    "C5": "nsgaiii__elit_on__kill",
    "C6": "nsgaiii__elit_off__kill",
    "C7": "rnsgaiii__elit_on__kill",
    "C8": "rnsgaiii__elit_off__kill",
}
NIVEIS = list(CONFIGS)
ID2LBL = {v: k for k, v in CONFIGS.items()}
SISTEMAS = ["spring-petclinic", "jpetstore"]
NOME_SIS = {"spring-petclinic": "Spring PetClinic", "jpetstore": "JPetStore"}
INDICADORES = ["hv", "igd_plus", "ed_media"]
NOME_IND = {"hv": "HV", "igd_plus": "IGD+", "ed_media": "ED (média)"}
MAIOR_MELHOR = {"hv"}
OBJETIVOS = ["Coupling", "Cohesion", "Overhead", "Functionality", "ReusePerMS"]
NOME_OBJ = {"Coupling": "Acoplamento", "Cohesion": "1/Coesão", "Overhead": "Overhead",
            "Functionality": "1/Funcionalidade", "ReusePerMS": "1/Reúso"}
GERACOES = [0, 150, 300, 450, 999]
PENALTY = 1e5

COR = dict(zip(NIVEIS, ["#2a78d6", "#eb6834", "#1baf7a", "#eda100",
                        "#e87ba4", "#008300", "#6250d6", "#e34948"]))
MARC = dict(zip(NIVEIS, ["o", "s", "^", "D", "v", "P", "X", "*"]))
COR_EXEC = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]

plt.rcParams.update({
    "font.family": "serif", "font.size": 8, "axes.titlesize": 8, "axes.labelsize": 8,
    "xtick.labelsize": 7, "ytick.labelsize": 7, "legend.fontsize": 7,
    "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True,
    "grid.color": "#e4e4e0", "grid.linewidth": 0.5, "axes.edgecolor": "#888",
    "pdf.fonttype": 42, "savefig.bbox": "tight", "savefig.dpi": 200,
})


def indicadores():
    pasta = SAIDA / "indicadores"
    if not (pasta / "por_sistema").exists():
        subprocess.run([sys.executable, "-m", "analise_estudo", "--root", str(RAIZ),
                        "--out", str(pasta), "--group-by", "persona"],
                       cwd=SCRIPT_OFICIAL, check=True, stdout=subprocess.DEVNULL)
    df = pd.concat([pd.read_csv(pasta / "por_sistema" / f"{PERSONA}_{s}.csv") for s in SISTEMAS],
                   ignore_index=True)
    df["cfg"] = df["config"].map(ID2LBL)
    limites = {s: json.loads((pasta / "por_sistema" / f"{PERSONA}_{s}.json").read_text())
               for s in SISTEMAS}
    return df, limites


def melhores_por_geracao(cands):
    out = {}
    for entrada in cands:
        m = np.array([[mt["value"] for mt in sorted(c["metrics"], key=lambda x: x["index"])]
                      for c in entrada["candidates"]])
        m = m[(m < PENALTY).all(axis=1)]
        out[int(entrada["generation"])] = dict(zip(OBJETIVOS, m.min(axis=0)))
    return out


def ler_execucoes():
    gen0 = {s: melhores_por_geracao(json.loads((DADOS / "analise" / "gen0" / f"{s}_numMS6.json").read_text()))[0]
            for s in SISTEMAS}
    conv, fronts = [], []
    for k in NIVEIS:
        for s in SISTEMAS:
            for z in sorted((DADOS / f"config_{k[1]}" / s).glob("*.zip")):
                with zipfile.ZipFile(z) as zf:
                    rep = int(json.loads(zf.read("manifest.json"))["study"]["repetition"])
                    best = melhores_por_geracao(json.loads(zf.read("candidates.json")))
                    best[0] = gen0[s]
                    for gen, vals in best.items():
                        conv.append({"sistema": s, "cfg": k, "rep": rep, "geracao": gen, **vals})
                    fr = json.loads(zf.read("frontiers.json"))
                    arr = np.array(fr["frontier"], float)
                    arr = arr[(arr < PENALTY).all(axis=1)]
                    for row in np.unique(arr, axis=0):
                        fronts.append({"sistema": s, "cfg": k, "rep": rep, **dict(zip(fr["metricNames"], row))})
    return pd.DataFrame(conv), pd.DataFrame(fronts)


def salvar(fig, nome):
    for ext in ("pdf", "png"):
        fig.savefig(FIG / f"{nome}.{ext}")
    plt.close(fig)


def fig_boxplots(df):
    fig, axes = plt.subplots(2, 3, figsize=(7.16, 4.0))
    rng = np.random.default_rng(1)
    for i, s in enumerate(SISTEMAS):
        for j, ind in enumerate(INDICADORES):
            ax = axes[i, j]
            dados = [df[(df.sistema == s) & (df.cfg == k)][ind].to_numpy() for k in NIVEIS]
            bp = ax.boxplot(dados, widths=0.55, patch_artist=True, showfliers=False,
                            medianprops={"color": "#222", "linewidth": 1.1})
            for patch, k in zip(bp["boxes"], NIVEIS):
                patch.set_facecolor(COR[k] + "40")
                patch.set_edgecolor(COR[k])
            for x, (k, v) in enumerate(zip(NIVEIS, dados), start=1):
                ax.scatter(x + rng.uniform(-.13, .13, len(v)), v, s=10, color=COR[k],
                           marker=MARC[k], edgecolor="white", linewidth=0.4, zorder=3)
            ax.set_xticks(range(1, 9), NIVEIS)
            seta = "↑" if ind in MAIOR_MELHOR else "↓"
            ax.set_title(f"{NOME_SIS[s]} — {NOME_IND[ind]} ({seta})")
    fig.tight_layout()
    salvar(fig, "boxplots_indicadores")


def fig_convergencia(conv, geracoes, nome):
    objs = [o for o in OBJETIVOS if o != "ReusePerMS"]
    pos = {g: i for i, g in enumerate(geracoes)}
    conv = conv[conv.geracao.isin(geracoes)]
    fig, axes = plt.subplots(2, 4, figsize=(7.16, 3.6))
    for i, s in enumerate(SISTEMAS):
        for j, obj in enumerate(objs):
            ax = axes[i, j]
            for k in NIVEIS:
                med = conv[(conv.sistema == s) & (conv.cfg == k)].groupby("geracao")[obj].median()
                ax.plot([pos[g] for g in med.index], med.values, color=COR[k], marker=MARC[k],
                        markersize=3, linewidth=1.1, label=k, alpha=0.9)
            ax.set_xticks(range(len(geracoes)), [str(g) for g in geracoes])
            ax.set_title(NOME_OBJ[obj])
            if j == 0:
                ax.set_ylabel(NOME_SIS[s])
            if i == 1:
                ax.set_xlabel("Geração")
    h, l = axes[0, 0].get_legend_handles_labels()
    fig.legend(h, l, loc="upper center", ncol=8, frameon=False, bbox_to_anchor=(0.5, 1.03))
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    salvar(fig, nome)


def fig_paralelas(fronts, limites):
    for s in SISTEMAS:
        lim = limites[s]["limites_normalizacao"]
        names = limites[s]["metric_names"]
        lo, hi = np.array(lim["min"]), np.array(lim["max"])
        span = np.where(hi > lo, hi - lo, 1.0)
        fig, axes = plt.subplots(2, 4, figsize=(7.16, 4.4), sharey=True)
        for ax, k in zip(axes.ravel(), NIVEIS):
            sub = fronts[(fronts.sistema == s) & (fronts.cfg == k)]
            for r in sorted(sub.rep.unique()):
                m = (sub[sub.rep == r][names].to_numpy() - lo) / span
                for linha in m:
                    ax.plot(range(5), linha, color=COR_EXEC[r - 1], alpha=0.25, linewidth=0.5)
                ax.plot([], [], color=COR_EXEC[r - 1], linewidth=1.5, label=f"exec. {r}")
            ax.set_xticks(range(5), [NOME_OBJ[n] for n in names], rotation=35, ha="right", fontsize=6)
            ax.set_title(k)
            ax.set_ylim(-0.03, 1.03)
            ax.grid(axis="y", visible=False)
            for x in range(5):
                ax.axvline(x, color="#bbb", linewidth=0.6, zorder=0)
        for r in range(2):
            axes[r, 0].set_ylabel("Valor normalizado")
        h, l = axes[0, 0].get_legend_handles_labels()
        fig.legend(h, l, loc="upper center", ncol=5, frameon=False, bbox_to_anchor=(0.5, 1.03))
        fig.tight_layout(rect=(0, 0, 1, 0.97))
        salvar(fig, f"paralelas_{s}")


def main():
    FIG.mkdir(parents=True, exist_ok=True)
    df, limites = indicadores()
    conv, fronts = ler_execucoes()
    fig_boxplots(df)
    fig_convergencia(conv, GERACOES, "convergencia_fitness")
    fig_paralelas(fronts, limites)


if __name__ == "__main__":
    main()
