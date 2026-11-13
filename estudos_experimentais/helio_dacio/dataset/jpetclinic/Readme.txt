EIA-ME — resultados da análise (HV, IGD+, ED)

Conteúdo
- por_sistema/<persona>_<sistema>.csv: uma linha por execução (8 configurações x 5 execuções = 40 linhas).
- resumo_por_config.csv: médias e desvios por configuração.
- por_sistema/<persona>_<sistema>.json: metadados (limites de normalização, Z* e execuções).
- resumo.json: configuração usada e contagens.

Colunas do CSV
persona, participante, config, sistema, repeticao, geracao, completo, n_pontos,
n_duplicados, hv, igd_plus, ed_media, ed_min, spacing

Direção dos indicadores
- HV: maior é melhor.
- IGD+, ED (média e mínima) e spacing: menor é melhor.

Como os valores foram calculados
- Normalização e fronteira de referência (Z*) por persona x sistema.
- HV com ponto de referência fixo 1.1 no espaço normalizado.
- ED ao ideal (0,0,0,0,0).
- Compare valores DENTRO de cada CSV (mesma persona x sistema), não entre CSVs.

Configurações (config_N -> configId)
config_1=nsgaiii__elit_on__penalty; config_2=nsgaiii__elit_off__penalty;
config_3=rnsgaiii__elit_on__penalty; config_4=rnsgaiii__elit_off__penalty;
config_5=nsgaiii__elit_on__kill;     config_6=nsgaiii__elit_off__kill;
config_7=rnsgaiii__elit_on__kill;    config_8=rnsgaiii__elit_off__kill.

Análise estatística (R)
Para cada CSV, rode:
  Rscript R/analise_estatistica.R <caminho do CSV>
O script imprime Shapiro-Wilk, Levene, ANOVA/Kruskal-Wallis, pós-hoc (Tukey/Dunn)
com FDR-BH e o tamanho de efeito Vargha-Delaney A12.

Escopo disponível
- P1: somente spring-petclinic (jpetstore ainda não disponível).
- P2 e P3: jpetstore e spring-petclinic.


------------------------------------------------------------
GERAÇÃO 0 (baseline de fitness)
------------------------------------------------------------
Pasta gen0/: um arquivo por (sistema, número inicial de microsserviços).
  spring-petclinic_numMS4.json
  spring-petclinic_numMS6.json
  jpetstore_numMS4.json
  jpetstore_numMS6.json

Formato: lista com 1 entrada AllCandidates (generation=0), igual ao formato do
candidates.json exportado nas interações/final. Cada entrada tem bestCandidates
e candidates (132 itens com index, microservices e os 5 objetivos).

Importante: a geração 0 é a POPULAÇÃO INICIAL DETERMINÍSTICA. O createSolution
ordena os vértices por nome e faz a partição em numMS (sem shuffle); como todos
os 132 indivíduos são criados pela mesma função determinística, os 132 candidatos
da gen 0 são IDÊNTICOS (um único vetor de fitness). A diversidade começa na gen 1.

Escolha o arquivo pelo manifest do ZIP:
  run.sourceId (spring-petclinic/jpetstore) + run.numberOfMicroservices (4/6).
Ex.: P1 e P2 usam spring-petclinic/numMS=4; P3 usa spring-petclinic/numMS=6;
     P2 usa jpetstore/numMS=4; P3 usa jpetstore/numMS=6.

Fitness da gen 0 (mesma convenção do candidates.json; todos minimizados;
Coesão/Funcionalidade/Reúso já estão invertidos como 1/valor):
  sistema/numMS        Coupling  Cohesion   Overhead  Functionality  ReusePerMS
  spring-petclinic/4   97.0      1.133333   1488.0    0.318245       1.0
  spring-petclinic/6   121.0     0.635838   3000.0    0.234909       1.0
  jpetstore/4          331.0     6.035479   2152.0    0.331901       1.0
  jpetstore/6          366.0     3.091620   2384.0    0.224791       1.0