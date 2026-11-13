# Relatório de Auditoria Estatística: Otimização Multiobjetivo para Arquitetura de Microsserviços (*i-to-microservices*)

Este documento apresenta a formatação tabular completa e auditada dos resultados estatísticos referentes ao delineamento fatorial completo $2^3$ ($N = 40$ execuções, $n = 5$ repetições por configuração) aplicado ao problema de decomposição e otimização de arquiteturas de microsserviços (*i-to-microservices*). A investigação avalia o impacto de três fatores arquiteturais do otimizador:
* **Fator $F_1$ (Algoritmo):** `NSGA-III` vs. `R-NSGA-III` (baseado em pontos de referência/aspiração).
* **Fator $F_2$ (Elitismo/Arquivamento Externo):** `ELIT_ON` vs. `ELIT_OFF`.
* **Fator $F_3$ (Manuseio de Restrições Arquiteturais):** `PENALTY` (penalização gradual de soluções inviáveis) vs. `KILL` (eliminação sumária de partições de microsserviços inviáveis).

---

## 1. Indicador: Hipervolume (HV)

O **Hipervolume (HV)** quantifica simultaneamente a convergência e a diversidade das arquiteturas candidatas de microsserviços na fronteira de Pareto aproximada (valores **maiores** indicam melhor qualidade de trade-off entre coesão, acoplamento e restrições modulares).

### Tabela 1.1: Auditoria de Normalidade (Shapiro-Wilk) para o Hipervolume (HV)
*Descrição: Avalia a aderência dos resíduos de cada configuração experimental do otimizador de microsserviços à distribuição normal ($n = 5$ execuções por grupo). A violação na `config_6` ($p = 0.011010 < 0.05$) invalida o pressuposto paramétrico global.*

| ID da Config. | Configuração Experimental ($F_1 \times F_2 \times F_3$) | $n$ | Estatística $W$ | Valor-$p$ | Normalidade ($\alpha = 0.05$) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| `config_1` | `nsgaiii__elit_on__penalty` | $5$ | $0.982934$ | $0.949680$ | `True` |
| `config_2` | `nsgaiii__elit_off__penalty` | $5$ | $0.932143$ | $0.611056$ | `True` |
| `config_3` | `rnsgaiii__elit_on__penalty` | $5$ | $0.905393$ | $0.440406$ | `True` |
| `config_4` | `rnsgaiii__elit_off__penalty` | $5$ | $0.972358$ | $0.890163$ | `True` |
| `config_5` | `nsgaiii__elit_on__kill` | $5$ | $0.827916$ | $0.134189$ | `True` |
| `config_6` | `nsgaiii__elit_off__kill` | $5$ | $0.705831$ | $0.011010$ | `False` |
| `config_7` | `rnsgaiii__elit_on__kill` | $5$ | $0.899612$ | $0.407744$ | `True` |
| `config_8` | `rnsgaiii__elit_off__kill` | $5$ | $0.887791$ | $0.346115$ | `True` |

### Tabela 1.2: Homocedasticidade (Levene) e Testes de Hipótese Globais para o Hipervolume (HV)
*Descrição: Apresenta a verificação de igualdade de variâncias centrada na mediana (Brown-Forsythe/Levene) e o teste global de diferença entre as 8 variantes de busca de microsserviços. Pelo protocolo formal de auditoria (`normalidade_ok = False` e `levene_ok = True`), adota-se o teste não-paramétrico de Kruskal-Wallis como decisão primária.*

| Etapa da Auditoria | Teste / Critério Estatístico | Estatística de Teste | Graus de Liberdade ($df$) | Valor-$p$ | Notação Científica | Resultado / Decisão |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **[2] Homocedasticidade** | Levene (`center='median'`) | $F/W = 2.008031$ | $(7, 32)$ | $0.084845$ | $8.4845 \times 10^{-2}$ | Homocedástico: `True` |
| **[3] Teste Global (Paramétrico)** | ANOVA One-Way | $F = 3.761244$ | $(7, 32)$ | $0.004401$ | $4.4010 \times 10^{-3}$ | Significativo ($p \le 0.05$) |
| **[3] Teste Global (Não-Paramétrico)** | **Kruskal-Wallis (Decisão Formal)** | $H = 17.871220$ | $7$ | $0.012565$ | $1.2565 \times 10^{-2}$ | **Significativo ($p \le 0.05$)** |

### Tabela 1.3: Top 12 Comparações Pós-Hoc Pareadas para o Hipervolume (HV)
*Descrição: Lista os 12 contrastes pareados mais relevantes ordenados pelo valor-$p$ ajustado de Dunn via Benjamini-Hochberg (`p_dunn_bh`). Evidencia a superioridade estatística significativa da configuração `config_4` (`rnsgaiii__elit_off__penalty`) frente às abordagens baseadas em descarte letal (`kill`) de soluções inviáveis.*

| Par ID | Comparação entre Configurações | $\text{diff}$ | $p_{\text{tukey}}$ | $p_{\text{tukey\_bh}}$ | Estatística $z$ | $p_{\text{dunn\_raw}}$ | $p_{\text{dunn\_bh}}$ | $\hat{A}_{12}$ | Magnitude |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `config_4` vs `config_8` | `rnsgaiii__elit_off__penalty` $-$ `rnsgaiii__elit_off__kill` | $0.276281$ | $0.018387$ | $0.396058$ | $3.164860$ | $0.001552$ | $0.043444$ | $1.000000$ | Grande |
| `config_4` vs `config_7` | `rnsgaiii__elit_off__penalty` $-$ `rnsgaiii__elit_on__kill` | $0.259290$ | $0.032036$ | $0.396058$ | $2.921410$ | $0.003485$ | $0.048783$ | $1.000000$ | Grande |
| `config_4` vs `config_5` | `rnsgaiii__elit_off__penalty` $-$ `nsgaiii__elit_on__kill` | $0.241311$ | $0.056118$ | $0.396058$ | $2.515658$ | $0.011881$ | $0.083167$ | $1.000000$ | Grande |
| `config_1` vs `config_8` | `nsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_off__kill` | $0.202867$ | $0.165334$ | $0.925868$ | $2.596809$ | $0.009409$ | $0.083167$ | $1.000000$ | Grande |
| `config_1` vs `config_7` | `nsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_on__kill` | $0.185876$ | $0.250015$ | $1.000000$ | $2.353358$ | $0.018605$ | $0.104186$ | $0.960000$ | Grande |
| `config_4` vs `config_6` | `rnsgaiii__elit_off__penalty` $-$ `nsgaiii__elit_off__kill` | $0.241041$ | $0.056580$ | $0.396058$ | $2.136957$ | $0.032601$ | $0.152140$ | $1.000000$ | Grande |
| `config_1` vs `config_5` | `nsgaiii__elit_on__penalty` $-$ `nsgaiii__elit_on__kill` | $0.167897$ | $0.367679$ | $1.000000$ | $1.947606$ | $0.051462$ | $0.204017$ | $0.920000$ | Grande |
| `config_2` vs `config_8` | `nsgaiii__elit_off__penalty` $-$ `rnsgaiii__elit_off__kill` | $0.174110$ | $0.323889$ | $1.000000$ | $1.893506$ | $0.058291$ | $0.204017$ | $0.840000$ | Grande |
| `config_3` vs `config_8` | `rnsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_off__kill` | $0.165646$ | $0.384290$ | $1.000000$ | $1.785306$ | $0.074212$ | $0.230881$ | $0.760000$ | Grande |
| `config_2` vs `config_7` | `nsgaiii__elit_off__penalty` $-$ `rnsgaiii__elit_on__kill` | $0.157119$ | $0.450338$ | $1.000000$ | $1.650055$ | $0.098932$ | $0.277008$ | $0.800000$ | Grande |
| `config_1` vs `config_6` | `nsgaiii__elit_on__penalty` $-$ `nsgaiii__elit_off__kill` | $0.167627$ | $0.369653$ | $1.000000$ | $1.568905$ | $0.116670$ | $0.287254$ | $0.880000$ | Grande |
| `config_3` vs `config_7` | `rnsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_on__kill` | $0.148656$ | $0.519661$ | $1.000000$ | $1.541855$ | $0.123109$ | $0.287254$ | $0.680000$ | Média |

* **Contabilização de Pares Significativos (HV):** $p_{\text{tukey}} \le 0.05$: $2$ | $p_{\text{tukey\_bh}} \le 0.05$: $0$ | $p_{\text{dunn\_raw}} \le 0.05$: $6$ | $p_{\text{dunn\_bh}} \le 0.05$: $2$.

### Tabela 1.4: Matriz Completa $8 \times 8$ de Tamanho de Efeito Vargha-Delaney $\hat{A}_{12}$ (HV)
*Descrição: Probabilidade estocástica de que uma execução da configuração na linha supere a configuração na coluna em termos de Hipervolume na geração das arquiteturas de microsserviços ($\hat{A}_{12} > 0.50$ favorece a linha).*

| Config. | `config_1` | `config_2` | `config_3` | `config_4` | `config_5` | `config_6` | `config_7` | `config_8` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`config_1`** | $0.50$ | $0.60$ | $0.56$ | $0.32$ | $0.92$ | $0.88$ | $0.96$ | $1.00$ |
| **`config_2`** | $0.40$ | $0.50$ | $0.52$ | $0.28$ | $0.68$ | $0.68$ | $0.80$ | $0.84$ |
| **`config_3`** | $0.44$ | $0.48$ | $0.50$ | $0.32$ | $0.68$ | $0.68$ | $0.68$ | $0.76$ |
| **`config_4`** | $0.68$ | $0.72$ | $0.68$ | $0.50$ | $1.00$ | $1.00$ | $1.00$ | $1.00$ |
| **`config_5`** | $0.08$ | $0.32$ | $0.32$ | $0.00$ | $0.50$ | $0.36$ | $0.64$ | $0.64$ |
| **`config_6`** | $0.12$ | $0.32$ | $0.32$ | $0.00$ | $0.64$ | $0.50$ | $0.76$ | $0.76$ |
| **`config_7`** | $0.04$ | $0.20$ | $0.32$ | $0.00$ | $0.36$ | $0.24$ | $0.50$ | $0.60$ |
| **`config_8`** | $0.00$ | $0.16$ | $0.24$ | $0.00$ | $0.36$ | $0.24$ | $0.40$ | $0.50$ |

### Tabela 1.5: Síntese de Magnitudes de Efeito $\hat{A}_{12}$ nos 28 Pares (HV)
*Descrição: Classificação qualitativa do tamanho de efeito não-paramétrico entre todos os 28 pares possíveis de configurações para o indicador HV.*

| Magnitude $\hat{A}_{12}$ | Quantidade de Pares | Proporção ($\text{Total} = 28$) |
| :--- | :---: | :---: |
| **Grande** | $14$ | $50.00\%$ |
| **Média** | $7$ | $25.00\%$ |
| **Pequena** | $6$ | $21.43\%$ |
| **Desprezível** | $1$ | $3.57\%$ |

---

## 2. Indicador: Distância Geracional Invertida Modificada ($\text{IGD}^+$)

O indicador **$\text{IGD}^+$** mede fracamente compatível com Pareto a distância das soluções obtidas em relação à fronteira de referência ótima de microsserviços (valores **menores** indicam melhor convergência e cobertura arquitetural).

### Tabela 2.1: Auditoria de Normalidade (Shapiro-Wilk) para o $\text{IGD}^+$
*Descrição: Avalia a normalidade das distribuições de $\text{IGD}^+$ nas 8 configurações. Assim como no HV, apenas a `config_6` apresenta desvio significativo da normalidade ($p = 0.009362$).*

| ID da Config. | Configuração Experimental ($F_1 \times F_2 \times F_3$) | $n$ | Estatística $W$ | Valor-$p$ | Normalidade ($\alpha = 0.05$) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| `config_1` | `nsgaiii__elit_on__penalty` | $5$ | $0.887604$ | $0.345199$ | `True` |
| `config_2` | `nsgaiii__elit_off__penalty` | $5$ | $0.929182$ | $0.590801$ | `True` |
| `config_3` | `rnsgaiii__elit_on__penalty` | $5$ | $0.929431$ | $0.592496$ | `True` |
| `config_4` | `rnsgaiii__elit_off__penalty` | $5$ | $0.946800$ | $0.714323$ | `True` |
| `config_5` | `nsgaiii__elit_on__kill` | $5$ | $0.953352$ | $0.761096$ | `True` |
| `config_6` | `nsgaiii__elit_off__kill` | $5$ | $0.699060$ | $0.009362$ | `False` |
| `config_7` | `rnsgaiii__elit_on__kill` | $5$ | $0.922644$ | $0.547136$ | `True` |
| `config_8` | `rnsgaiii__elit_off__kill` | $5$ | $0.890635$ | $0.360308$ | `True` |

### Tabela 2.2: Homocedasticidade (Levene) e Testes de Hipótese Globais para o $\text{IGD}^+$
*Descrição: Resultado dos testes de homogeneidade de variância e testes omnibus globais. Não há diferença global estatisticamente significativa ao nível de $5\%$ no teste omnibus ($p = 0.129848$), embora contrastes específicos apresentem efeitos práticos de grande magnitude.*

| Etapa da Auditoria | Teste / Critério Estatístico | Estatística de Teste | Graus de Liberdade ($df$) | Valor-$p$ | Notação Científica | Resultado / Decisão |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **[2] Homocedasticidade** | Levene (`center='median'`) | $F/W = 1.052203$ | $(7, 32)$ | $0.415825$ | $4.1583 \times 10^{-1}$ | Homocedástico: `True` |
| **[3] Teste Global (Paramétrico)** | ANOVA One-Way | $F = 1.910014$ | $(7, 32)$ | $0.100552$ | $1.0055 \times 10^{-1}$ | Não Significativo ($p > 0.05$) |
| **[3] Teste Global (Não-Paramétrico)** | **Kruskal-Wallis (Decisão Formal)** | $H = 11.206829$ | $7$ | $0.129848$ | $1.2985 \times 10^{-1}$ | **Não Significativo ($p > 0.05$)** |

### Tabela 2.3: Top 12 Comparações Pós-Hoc Pareadas para o $\text{IGD}^+$
*Descrição: Contrastes pós-hoc ordenados por `p_dunn_bh`. Quatro comparações envolvendo a `config_4` (`rnsgaiii__elit_off__penalty`) apresentam $p_{\text{dunn\_raw}} \le 0.05$ e tamanhos de efeito $\hat{A}_{12} \ge 0.92$, mas sofrem atenuação após a correção conservadora para 28 testes simultâneos.*

| Par ID | Comparação entre Configurações | $\text{diff}$ | $p_{\text{tukey}}$ | $p_{\text{tukey\_bh}}$ | Estatística $z$ | $p_{\text{dunn\_raw}}$ | $p_{\text{dunn\_bh}}$ | $\hat{A}_{12}$ | Magnitude |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `config_4` vs `config_7` | `rnsgaiii__elit_off__penalty` $-$ `rnsgaiii__elit_on__kill` | $-0.096571$ | $0.072659$ | $1.000000$ | $-2.921410$ | $0.003485$ | $0.097566$ | $1.000000$ | Grande |
| `config_4` vs `config_8` | `rnsgaiii__elit_off__penalty` $-$ `rnsgaiii__elit_off__kill` | $-0.089979$ | $0.114213$ | $1.000000$ | $-2.677959$ | $0.007407$ | $0.103701$ | $0.960000$ | Grande |
| `config_4` vs `config_5` | `rnsgaiii__elit_off__penalty` $-$ `nsgaiii__elit_on__kill` | $-0.083629$ | $0.171281$ | $1.000000$ | $-2.326308$ | $0.020002$ | $0.186687$ | $0.960000$ | Grande |
| `config_4` vs `config_6` | `rnsgaiii__elit_off__penalty` $-$ `nsgaiii__elit_off__kill` | $-0.086302$ | $0.144990$ | $1.000000$ | $-2.082857$ | $0.037264$ | $0.260850$ | $0.920000$ | Grande |
| `config_2` vs `config_4` | `nsgaiii__elit_off__penalty` $-$ `rnsgaiii__elit_off__penalty` | $0.067639$ | $0.404611$ | $1.000000$ | $1.920556$ | $0.054788$ | $0.306811$ | $0.160000$ | Grande |
| `config_3` vs `config_4` | `rnsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_off__penalty` | $0.061445$ | $0.524844$ | $1.000000$ | $1.758256$ | $0.078704$ | $0.367285$ | $0.240000$ | Grande |
| `config_1` vs `config_4` | `nsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_off__penalty` | $0.061029$ | $0.533233$ | $1.000000$ | $1.568905$ | $0.116670$ | $0.466680$ | $0.120000$ | Grande |
| `config_1` vs `config_7` | `nsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_on__kill` | $-0.035542$ | $0.944670$ | $1.000000$ | $-1.352504$ | $0.176214$ | $0.616749$ | $0.760000$ | Grande |
| `config_1` vs `config_8` | `nsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_off__kill` | $-0.028950$ | $0.981589$ | $1.000000$ | $-1.109054$ | $0.267407$ | $0.748740$ | $0.720000$ | Grande |
| `config_3` vs `config_7` | `rnsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_on__kill` | $-0.035126$ | $0.947879$ | $1.000000$ | $-1.163154$ | $0.244767$ | $0.748740$ | $0.680000$ | Média |
| `config_2` vs `config_7` | `nsgaiii__elit_off__penalty` $-$ `rnsgaiii__elit_on__kill` | $-0.028932$ | $0.981653$ | $1.000000$ | $-1.000853$ | $0.316898$ | $0.806649$ | $0.640000$ | Pequena |
| `config_3` vs `config_8` | `rnsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_off__kill` | $-0.028534$ | $0.983037$ | $1.000000$ | $-0.919703$ | $0.357728$ | $0.834699$ | $0.680000$ | Média |

* **Contabilização de Pares Significativos ($\text{IGD}^+$):** $p_{\text{tukey}} \le 0.05$: $0$ | $p_{\text{tukey\_bh}} \le 0.05$: $0$ | $p_{\text{dunn\_raw}} \le 0.05$: $4$ | $p_{\text{dunn\_bh}} \le 0.05$: $0$.

### Tabela 2.4: Matriz Completa $8 \times 8$ de Tamanho de Efeito Vargha-Delaney $\hat{A}_{12}$ ($\text{IGD}^+$)
*Descrição: Matriz pareada de dominância estocástica para $\text{IGD}^+$ ajustada à direção de otimalidade do indicador (valores na linha próximos de $1.00$, como na linha `config_4`, indicam que a configuração da linha atinge sistematicamente valores menores/melhores de $\text{IGD}^+$).*

| Config. | `config_1` | `config_2` | `config_3` | `config_4` | `config_5` | `config_6` | `config_7` | `config_8` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`config_1`** | $0.50$ | $0.56$ | $0.48$ | $0.12$ | $0.68$ | $0.68$ | $0.76$ | $0.72$ |
| **`config_2`** | $0.44$ | $0.50$ | $0.48$ | $0.16$ | $0.60$ | $0.60$ | $0.64$ | $0.56$ |
| **`config_3`** | $0.52$ | $0.52$ | $0.50$ | $0.24$ | $0.56$ | $0.52$ | $0.68$ | $0.68$ |
| **`config_4`** | $0.88$ | $0.84$ | $0.76$ | $0.50$ | $0.96$ | $0.92$ | $1.00$ | $0.96$ |
| **`config_5`** | $0.32$ | $0.40$ | $0.44$ | $0.04$ | $0.50$ | $0.44$ | $0.64$ | $0.60$ |
| **`config_6`** | $0.32$ | $0.40$ | $0.48$ | $0.08$ | $0.56$ | $0.50$ | $0.76$ | $0.64$ |
| **`config_7`** | $0.24$ | $0.36$ | $0.32$ | $0.00$ | $0.36$ | $0.24$ | $0.50$ | $0.48$ |
| **`config_8`** | $0.28$ | $0.44$ | $0.32$ | $0.04$ | $0.40$ | $0.36$ | $0.52$ | $0.50$ |

### Tabela 2.5: Síntese de Magnitudes de Efeito $\hat{A}_{12}$ nos 28 Pares ($\text{IGD}^+$)
*Descrição: Distribuição da magnitude prática das diferenças observadas no indicador $\text{IGD}^+$.*

| Magnitude $\hat{A}_{12}$ | Quantidade de Pares | Proporção ($\text{Total} = 28$) |
| :--- | :---: | :---: |
| **Grande** | $10$ | $35.71\%$ |
| **Pequena** | $9$ | $32.14\%$ |
| **Desprezível** | $5$ | $17.86\%$ |
| **Média** | $4$ | $14.29\%$ |

---

## 3. Indicador: Distância Euclidiana Média ($\text{ED}_{\text{média}}$)

O indicador **$\text{ED}_{\text{média}}$** avalia a proximidade média de toda a população final de arquiteturas de microsserviços em relação ao ponto ideal/aspiracional definido pelo arquiteto de software (valores **menores** refletem maior concentração das soluções em torno das preferências de projeto).

### Tabela 3.1: Auditoria de Normalidade (Shapiro-Wilk) para $\text{ED}_{\text{média}}$
*Descrição: Verifica a normalidade de $\text{ED}_{\text{média}}$ por grupo. Detecta-se rejeição da hipótese de normalidade na configuração `config_7` (`rnsgaiii__elit_on__kill`, com $p = 0.015789$).*

| ID da Config. | Configuração Experimental ($F_1 \times F_2 \times F_3$) | $n$ | Estatística $W$ | Valor-$p$ | Normalidade ($\alpha = 0.05$) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| `config_1` | `nsgaiii__elit_on__penalty` | $5$ | $0.890547$ | $0.359860$ | `True` |
| `config_2` | `nsgaiii__elit_off__penalty` | $5$ | $0.926770$ | $0.574513$ | `True` |
| `config_3` | `rnsgaiii__elit_on__penalty` | $5$ | $0.964059$ | $0.835927$ | `True` |
| `config_4` | `rnsgaiii__elit_off__penalty` | $5$ | $0.895540$ | $0.385726$ | `True` |
| `config_5` | `nsgaiii__elit_on__kill` | $5$ | $0.929160$ | $0.590654$ | `True` |
| `config_6` | `nsgaiii__elit_off__kill` | $5$ | $0.893535$ | $0.375189$ | `True` |
| `config_7` | `rnsgaiii__elit_on__kill` | $5$ | $0.721300$ | $0.015789$ | `False` |
| `config_8` | `rnsgaiii__elit_off__kill` | $5$ | $0.804749$ | $0.088538$ | `True` |

### Tabela 3.2: Homocedasticidade (Levene) e Testes de Hipótese Globais para $\text{ED}_{\text{média}}$
*Descrição: Resultados da homocedasticidade e testes globais para a distância euclidiana média. O fluxo formal seleciona Kruskal-Wallis devido à violação de normalidade na `config_7`.*

| Etapa da Auditoria | Teste / Critério Estatístico | Estatística de Teste | Graus de Liberdade ($df$) | Valor-$p$ | Notação Científica | Resultado / Decisão |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **[2] Homocedasticidade** | Levene (`center='median'`) | $F/W = 0.682403$ | $(7, 32)$ | $0.685762$ | $6.8576 \times 10^{-1}$ | Homocedástico: `True` |
| **[3] Teste Global (Paramétrico)** | ANOVA One-Way | $F = 1.477671$ | $(7, 32)$ | $0.210447$ | $2.1045 \times 10^{-1}$ | Não Significativo ($p > 0.05$) |
| **[3] Teste Global (Não-Paramétrico)** | **Kruskal-Wallis (Decisão Formal)** | $H = 10.428293$ | $7$ | $0.165573$ | $1.6557 \times 10^{-1}$ | **Não Significativo ($p > 0.05$)** |

### Tabela 3.3: Top 12 Comparações Pós-Hoc Pareadas para $\text{ED}_{\text{média}}$
*Descrição: Principais contrastes pareados de $\text{ED}_{\text{média}}$. Observa-se que 5 pares envolvendo a `config_4` (`rnsgaiii__elit_off__penalty`) atingem $p_{\text{dunn\_raw}} \le 0.05$, confirmando a capacidade do `R-NSGA-III` em guiar o enxame de soluções para mais perto da região de interesse arquitetural.*

| Par ID | Comparação entre Configurações | $\text{diff}$ | $p_{\text{tukey}}$ | $p_{\text{tukey\_bh}}$ | Estatística $z$ | $p_{\text{dunn\_raw}}$ | $p_{\text{dunn\_bh}}$ | $\hat{A}_{12}$ | Magnitude |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `config_1` vs `config_4` | `nsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_off__penalty` | $0.135200$ | $0.175309$ | $1.000000$ | $2.461558$ | $0.013833$ | $0.186687$ | $0.000000$ | Grande |
| `config_4` vs `config_5` | `rnsgaiii__elit_off__penalty` $-$ `nsgaiii__elit_on__kill` | $-0.109670$ | $0.406639$ | $1.000000$ | $-2.434508$ | $0.014912$ | $0.186687$ | $1.000000$ | Grande |
| `config_2` vs `config_4` | `nsgaiii__elit_off__penalty` $-$ `rnsgaiii__elit_off__penalty` | $0.118646$ | $0.311139$ | $1.000000$ | $2.326308$ | $0.020002$ | $0.186687$ | $0.200000$ | Grande |
| `config_3` vs `config_4` | `rnsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_off__penalty` | $0.098762$ | $0.537609$ | $1.000000$ | $2.028757$ | $0.042483$ | $0.237905$ | $0.120000$ | Grande |
| `config_4` vs `config_6` | `rnsgaiii__elit_off__penalty` $-$ `nsgaiii__elit_off__kill` | $-0.103053$ | $0.484723$ | $1.000000$ | $-2.028757$ | $0.042483$ | $0.237905$ | $0.920000$ | Grande |
| `config_4` vs `config_7` | `rnsgaiii__elit_off__penalty` $-$ `rnsgaiii__elit_on__kill` | $-0.073357$ | $0.832703$ | $1.000000$ | $-1.758256$ | $0.078704$ | $0.367285$ | $0.800000$ | Grande |
| `config_5` vs `config_8` | `nsgaiii__elit_on__kill` $-$ `rnsgaiii__elit_off__kill` | $0.061058$ | $0.926883$ | $1.000000$ | $1.514805$ | $0.129822$ | $0.454376$ | $0.200000$ | Grande |
| `config_1` vs `config_8` | `nsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_off__kill` | $0.086588$ | $0.688600$ | $1.000000$ | $1.541855$ | $0.123109$ | $0.454376$ | $0.200000$ | Grande |
| `config_2` vs `config_8` | `nsgaiii__elit_off__penalty` $-$ `rnsgaiii__elit_off__kill` | $0.070035$ | $0.862500$ | $1.000000$ | $1.406605$ | $0.159545$ | $0.496361$ | $0.320000$ | Média |
| `config_3` vs `config_8` | `rnsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_off__kill` | $0.050150$ | $0.973641$ | $1.000000$ | $1.109054$ | $0.267407$ | $0.680672$ | $0.280000$ | Grande |
| `config_6` vs `config_8` | `nsgaiii__elit_off__kill` $-$ `rnsgaiii__elit_off__kill` | $0.054441$ | $0.959066$ | $1.000000$ | $1.109054$ | $0.267407$ | $0.680672$ | $0.240000$ | Grande |
| `config_4` vs `config_8` | `rnsgaiii__elit_off__penalty` $-$ `rnsgaiii__elit_off__kill` | $-0.048612$ | $0.977805$ | $1.000000$ | $-0.919703$ | $0.357728$ | $0.834699$ | $0.680000$ | Média |

* **Contabilização de Pares Significativos ($\text{ED}_{\text{média}}$):** $p_{\text{tukey}} \le 0.05$: $0$ | $p_{\text{tukey\_bh}} \le 0.05$: $0$ | $p_{\text{dunn\_raw}} \le 0.05$: $5$ | $p_{\text{dunn\_bh}} \le 0.05$: $0$.

### Tabela 3.4: Matriz Completa $8 \times 8$ de Tamanho de Efeito Vargha-Delaney $\hat{A}_{12}$ ($\text{ED}_{\text{média}}$)
*Descrição: Matriz de superioridade estocástica para $\text{ED}_{\text{média}}$. Valores acima de $0.50$ na linha indicam que a configuração da linha apresenta menor distância euclidiana média até o ponto de referência arquitetural.*

| Config. | `config_1` | `config_2` | `config_3` | `config_4` | `config_5` | `config_6` | `config_7` | `config_8` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`config_1`** | $0.50$ | $0.48$ | $0.44$ | $0.00$ | $0.48$ | $0.44$ | $0.40$ | $0.20$ |
| **`config_2`** | $0.52$ | $0.50$ | $0.40$ | $0.20$ | $0.44$ | $0.44$ | $0.32$ | $0.32$ |
| **`config_3`** | $0.56$ | $0.60$ | $0.50$ | $0.12$ | $0.56$ | $0.52$ | $0.44$ | $0.28$ |
| **`config_4`** | $1.00$ | $0.80$ | $0.88$ | $0.50$ | $1.00$ | $0.92$ | $0.80$ | $0.68$ |
| **`config_5`** | $0.52$ | $0.56$ | $0.44$ | $0.00$ | $0.50$ | $0.36$ | $0.40$ | $0.20$ |
| **`config_6`** | $0.56$ | $0.56$ | $0.48$ | $0.08$ | $0.64$ | $0.50$ | $0.52$ | $0.24$ |
| **`config_7`** | $0.60$ | $0.68$ | $0.56$ | $0.20$ | $0.60$ | $0.48$ | $0.50$ | $0.36$ |
| **`config_8`** | $0.80$ | $0.68$ | $0.72$ | $0.32$ | $0.80$ | $0.76$ | $0.64$ | $0.50$ |

### Tabela 3.5: Síntese de Magnitudes de Efeito $\hat{A}_{12}$ nos 28 Pares ($\text{ED}_{\text{média}}$)
*Descrição: Contagem das magnitudes de efeito Vargha-Delaney entre os 28 pares avaliados para $\text{ED}_{\text{média}}$.*

| Magnitude $\hat{A}_{12}$ | Quantidade de Pares | Proporção ($\text{Total} = 28$) |
| :--- | :---: | :---: |
| **Grande** | $10$ | $35.71\%$ |
| **Desprezível** | $9$ | $32.14\%$ |
| **Pequena** | $6$ | $21.43\%$ |
| **Média** | $3$ | $10.71\%$ |

---

## 4. Indicador: Distância Euclidiana Mínima ($\text{ED}_{\text{min}}$)

O indicador **$\text{ED}_{\text{min}}$** representa a distância da **melhor solução individual de compromisso** (*knee/best-compromise architecture*) até o ponto ideal de decomposição de microsserviços (valores **menores** são mais desejáveis para a tomada de decisão final do arquiteto).

### Tabela 4.1: Auditoria de Normalidade (Shapiro-Wilk) para $\text{ED}_{\text{min}}$
*Descrição: Todos os 8 grupos experimentais satisfazem o pressuposto de normalidade ($p > 0.05$ em todas as configurações).*

| ID da Config. | Configuração Experimental ($F_1 \times F_2 \times F_3$) | $n$ | Estatística $W$ | Valor-$p$ | Normalidade ($\alpha = 0.05$) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| `config_1` | `nsgaiii__elit_on__penalty` | $5$ | $0.924504$ | $0.559399$ | `True` |
| `config_2` | `nsgaiii__elit_off__penalty` | $5$ | $0.935770$ | $0.636211$ | `True` |
| `config_3` | `rnsgaiii__elit_on__penalty` | $5$ | $0.920964$ | $0.536178$ | `True` |
| `config_4` | `rnsgaiii__elit_off__penalty` | $5$ | $0.883725$ | $0.326534$ | `True` |
| `config_5` | `nsgaiii__elit_on__kill` | $5$ | $0.989382$ | $0.977486$ | `True` |
| `config_6` | `nsgaiii__elit_off__kill` | $5$ | $0.812871$ | $0.102747$ | `True` |
| `config_7` | `rnsgaiii__elit_on__kill` | $5$ | $0.931409$ | $0.606012$ | `True` |
| `config_8` | `rnsgaiii__elit_off__kill` | $5$ | $0.941673$ | $0.677790$ | `True` |

### Tabela 4.2: Homocedasticidade (Levene) e Testes de Hipótese Globais para $\text{ED}_{\text{min}}$
*Descrição: Atendidos ambos os pressupostos paramétricos (`normalidade_ok = True` e `levene_ok = True`), a decisão formal recai sobre a ANOVA One-Way, que aponta tendência marginal de significância ($p = 0.071307$).*

| Etapa da Auditoria | Teste / Critério Estatístico | Estatística de Teste | Graus de Liberdade ($df$) | Valor-$p$ | Notação Científica | Resultado / Decisão |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **[2] Homocedasticidade** | Levene (`center='median'`) | $F/W = 0.696013$ | $(7, 32)$ | $0.674921$ | $6.7492 \times 10^{-1}$ | Homocedástico: `True` |
| **[3] Teste Global (Paramétrico)** | **ANOVA One-Way (Decisão Formal)** | $F = 2.108188$ | $(7, 32)$ | $0.071307$ | $7.1307 \times 10^{-2}$ | **Marginal ($0.05 < p < 0.10$)** |
| **[3] Teste Global (Não-Paramétrico)** | Kruskal-Wallis | $H = 9.921951$ | $7$ | $0.193040$ | $1.9304 \times 10^{-1}$ | Não Significativo ($p > 0.05$) |

### Tabela 4.3: Top 12 Comparações Pós-Hoc Pareadas para $\text{ED}_{\text{min}}$
*Descrição: Contrastes pareados ordenados pelo valor-$p$ ajustado de Tukey (`p_tukey_bh`). Destaca-se novamente a `config_4` com diferenças brutas expressivas e $p_{\text{tukey}} \approx 0.07$ frente às configurações `config_6` e `config_7`.*

| Par ID | Comparação entre Configurações | $\text{diff}$ | $p_{\text{tukey}}$ | $p_{\text{tukey\_bh}}$ | Estatística $z$ | $p_{\text{dunn\_raw}}$ | $p_{\text{dunn\_bh}}$ | $\hat{A}_{12}$ | Magnitude |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `config_4` vs `config_7` | `rnsgaiii__elit_off__penalty` $-$ `rnsgaiii__elit_on__kill` | $-0.133875$ | $0.069432$ | $0.982762$ | $-2.677959$ | $0.007407$ | $0.200576$ | $0.960000$ | Grande |
| `config_4` vs `config_6` | `rnsgaiii__elit_off__penalty` $-$ `nsgaiii__elit_off__kill` | $-0.133663$ | $0.070197$ | $0.982762$ | $-2.299258$ | $0.021490$ | $0.200576$ | $0.960000$ | Grande |
| `config_1` vs `config_2` | `nsgaiii__elit_on__penalty` $-$ `nsgaiii__elit_off__penalty` | $-0.007333$ | $1.000000$ | $1.000000$ | $-0.486902$ | $0.626328$ | $0.923010$ | $0.600000$ | Pequena |
| `config_6` vs `config_7` | `nsgaiii__elit_off__kill` $-$ `rnsgaiii__elit_on__kill` | $-0.000212$ | $1.000000$ | $1.000000$ | $-0.378701$ | $0.704910$ | $0.938075$ | $0.600000$ | Pequena |
| `config_5` vs `config_8` | `nsgaiii__elit_on__kill` $-$ `rnsgaiii__elit_off__kill` | $-0.003820$ | $1.000000$ | $1.000000$ | $-0.243451$ | $0.807656$ | $0.938075$ | $0.560000$ | Pequena |
| `config_5` vs `config_7` | `nsgaiii__elit_on__kill` $-$ `rnsgaiii__elit_on__kill` | $-0.015370$ | $0.999957$ | $1.000000$ | $-0.541002$ | $0.588506$ | $0.915454$ | $0.600000$ | Pequena |
| `config_5` vs `config_6` | `nsgaiii__elit_on__kill` $-$ `nsgaiii__elit_off__kill` | $-0.015158$ | $0.999961$ | $1.000000$ | $-0.162301$ | $0.871069$ | $0.938075$ | $0.560000$ | Pequena |
| `config_4` vs `config_8` | `rnsgaiii__elit_off__penalty` $-$ `rnsgaiii__elit_off__kill` | $-0.122325$ | $0.123242$ | $1.000000$ | $-2.380408$ | $0.017293$ | $0.200576$ | $0.920000$ | Grande |
| `config_4` vs `config_5` | `rnsgaiii__elit_off__penalty` $-$ `nsgaiii__elit_on__kill` | $-0.118506$ | $0.147318$ | $1.000000$ | $-2.136957$ | $0.032601$ | $0.208680$ | $0.920000$ | Grande |
| `config_3` vs `config_8` | `rnsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_off__kill` | $-0.048913$ | $0.944869$ | $1.000000$ | $-0.946753$ | $0.343765$ | $0.915454$ | $0.680000$ | Média |
| `config_3` vs `config_7` | `rnsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_on__kill` | $-0.060463$ | $0.851502$ | $1.000000$ | $-1.244304$ | $0.213388$ | $0.746857$ | $0.680000$ | Média |
| `config_3` vs `config_6` | `rnsgaiii__elit_on__penalty` $-$ `nsgaiii__elit_off__kill` | $-0.060251$ | $0.853709$ | $1.000000$ | $-0.865603$ | $0.386708$ | $0.915454$ | $0.640000$ | Pequena |

* **Contabilização de Pares Significativos ($\text{ED}_{\text{min}}$):** $p_{\text{tukey}} \le 0.05$: $0$ | $p_{\text{tukey\_bh}} \le 0.05$: $0$ | $p_{\text{dunn\_raw}} \le 0.05$: $5$ | $p_{\text{dunn\_bh}} \le 0.05$: $0$.

### Tabela 4.4: Matriz Completa $8 \times 8$ de Tamanho de Efeito Vargha-Delaney $\hat{A}_{12}$ ($\text{ED}_{\text{min}}$)
*Descrição: Dominância estocástica pareada para a menor distância euclidiana. A linha `config_4` supera todas as demais configurações com probabilidades entre $0.72$ e $0.96$.*

| Config. | `config_1` | `config_2` | `config_3` | `config_4` | `config_5` | `config_6` | `config_7` | `config_8` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`config_1`** | $0.50$ | $0.60$ | $0.40$ | $0.12$ | $0.64$ | $0.64$ | $0.72$ | $0.72$ |
| **`config_2`** | $0.40$ | $0.50$ | $0.40$ | $0.16$ | $0.52$ | $0.52$ | $0.60$ | $0.52$ |
| **`config_3`** | $0.60$ | $0.60$ | $0.50$ | $0.28$ | $0.60$ | $0.64$ | $0.68$ | $0.68$ |
| **`config_4`** | $0.88$ | $0.84$ | $0.72$ | $0.50$ | $0.92$ | $0.96$ | $0.96$ | $0.92$ |
| **`config_5`** | $0.36$ | $0.48$ | $0.40$ | $0.08$ | $0.50$ | $0.56$ | $0.60$ | $0.56$ |
| **`config_6`** | $0.36$ | $0.48$ | $0.36$ | $0.04$ | $0.44$ | $0.50$ | $0.60$ | $0.52$ |
| **`config_7`** | $0.28$ | $0.40$ | $0.32$ | $0.04$ | $0.40$ | $0.40$ | $0.50$ | $0.40$ |
| **`config_8`** | $0.28$ | $0.48$ | $0.32$ | $0.08$ | $0.44$ | $0.48$ | $0.60$ | $0.50$ |

### Tabela 4.5: Síntese de Magnitudes de Efeito $\hat{A}_{12}$ nos 28 Pares ($\text{ED}_{\text{min}}$)
*Descrição: Resumo das magnitudes de efeito para $\text{ED}_{\text{min}}$ nos 28 contrastes.*

| Magnitude $\hat{A}_{12}$ | Quantidade de Pares | Proporção ($\text{Total} = 28$) |
| :--- | :---: | :---: |
| **Pequena** | $13$ | $46.43\%$ |
| **Grande** | $9$ | $32.14\%$ |
| **Desprezível** | $4$ | $14.29\%$ |
| **Média** | $2$ | $7.14\%$ |

---

## 5. Indicador: Espaçamento (*Spacing*)

O indicador **Spacing** mensura a uniformidade do espaçamento entre soluções vizinhas na fronteira de Pareto aproximada. Na auditoria da decomposição de microsserviços, valores menores de Spacing sob a estratégia `KILL` ocorrem como artefato do colapso da extensão da fronteira (soluções agrupadas em uma região restrita), enquanto a estratégia `PENALTY` expande a fronteira (aumentando o HV e consequentemente a variação de espaçamento absoluto).

### Tabela 5.1: Auditoria de Normalidade (Shapiro-Wilk) para o *Spacing*
*Descrição: Todos os 8 grupos experimentais apresentam distribuição normal ($p > 0.10$ em todas as configurações).*

| ID da Config. | Configuração Experimental ($F_1 \times F_2 \times F_3$) | $n$ | Estatística $W$ | Valor-$p$ | Normalidade ($\alpha = 0.05$) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| `config_1` | `nsgaiii__elit_on__penalty` | $5$ | $0.965795$ | $0.847639$ | `True` |
| `config_2` | `nsgaiii__elit_off__penalty` | $5$ | $0.927275$ | $0.577907$ | `True` |
| `config_3` | `rnsgaiii__elit_on__penalty` | $5$ | $0.814189$ | $0.105226$ | `True` |
| `config_4` | `rnsgaiii__elit_off__penalty` | $5$ | $0.879121$ | $0.305348$ | `True` |
| `config_5` | `nsgaiii__elit_on__kill` | $5$ | $0.880337$ | $0.310843$ | `True` |
| `config_6` | `nsgaiii__elit_off__kill` | $5$ | $0.906941$ | $0.449428$ | `True` |
| `config_7` | `rnsgaiii__elit_on__kill` | $5$ | $0.907225$ | $0.451093$ | $True$ |
| `config_8` | `rnsgaiii__elit_off__kill` | $5$ | $0.966991$ | $0.855616$ | `True` |

### Tabela 5.2: Homocedasticidade (Levene) e Testes de Hipótese Globais para o *Spacing*
*Descrição: Com normalidade e homocedasticidade confirmadas, aplica-se a ANOVA One-Way, revelando diferença altamente significativa entre as configurações ($p = 0.000105$), corroborada pelo teste de Kruskal-Wallis ($p = 0.000117$).*

| Etapa da Auditoria | Teste / Critério Estatístico | Estatística de Teste | Graus de Liberdade ($df$) | Valor-$p$ | Notação Científica | Resultado / Decisão |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **[2] Homocedasticidade** | Levene (`center='median'`) | $F/W = 1.712770$ | $(7, 32)$ | $0.141260$ | $1.4126 \times 10^{-1}$ | Homocedástico: `True` |
| **[3] Teste Global (Paramétrico)** | **ANOVA One-Way (Decisão Formal)** | $F = 6.327625$ | $(7, 32)$ | $0.000105$ | $1.0455 \times 10^{-4}$ | **Altamente Significativo ($p \le 0.001$)** |
| **[3] Teste Global (Não-Paramétrico)** | Kruskal-Wallis | $H = 29.505366$ | $7$ | $0.000117$ | $1.1699 \times 10^{-4}$ | Altamente Significativo ($p \le 0.001$) |

### Tabela 5.3: Top 12 Comparações Pós-Hoc Pareadas para o *Spacing*
*Descrição: Contrastes pós-hoc ordenados por `p_tukey_bh`. Seis pares permanecem estatisticamente significativos mesmo após a correção BH no teste de Tukey ($p_{\text{tukey\_bh}} = 0.049099$), e 13 pares no teste de Dunn ajustado, separando nitidamente os regimes `PENALTY` (`config_1` a `config_4`) e `KILL` (`config_5` a `config_8`).*

| Par ID | Comparação entre Configurações | $\text{diff}$ | $p_{\text{tukey}}$ | $p_{\text{tukey\_bh}}$ | Estatística $z$ | $p_{\text{dunn\_raw}}$ | $p_{\text{dunn\_bh}}$ | $\hat{A}_{12}$ | Magnitude |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `config_3` vs `config_8` | `rnsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_off__kill` | $0.051735$ | $0.007594$ | $0.049099$ | $3.164860$ | $0.001552$ | $0.014481$ | $0.000000$ | Grande |
| `config_1` vs `config_5` | `nsgaiii__elit_on__penalty` $-$ `nsgaiii__elit_on__kill` | $0.050309$ | $0.010135$ | $0.049099$ | $2.786159$ | $0.005334$ | $0.021335$ | $0.000000$ | Grande |
| `config_1` vs `config_6` | `nsgaiii__elit_on__penalty` $-$ `nsgaiii__elit_off__kill` | $0.055157$ | $0.003742$ | $0.049099$ | $3.164860$ | $0.001552$ | $0.014481$ | $0.000000$ | Grande |
| `config_1` vs `config_7` | `nsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_on__kill` | $0.051562$ | $0.007865$ | $0.049099$ | $3.029610$ | $0.002449$ | $0.017141$ | $0.000000$ | Grande |
| `config_1` vs `config_8` | `nsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_off__kill` | $0.056769$ | $0.002666$ | $0.049099$ | $3.516512$ | $0.000437$ | $0.012243$ | $0.000000$ | Grande |
| `config_3` vs `config_6` | `rnsgaiii__elit_on__penalty` $-$ `nsgaiii__elit_off__kill` | $0.050123$ | $0.010521$ | $0.049099$ | $2.813209$ | $0.004905$ | $0.021335$ | $0.000000$ | Grande |
| `config_3` vs `config_7` | `rnsgaiii__elit_on__penalty` $-$ `rnsgaiii__elit_on__kill` | $0.046528$ | $0.021357$ | $0.085428$ | $2.677959$ | $0.007407$ | $0.023045$ | $0.000000$ | Grande |
| `config_3` vs `config_5` | `rnsgaiii__elit_on__penalty` $-$ `nsgaiii__elit_on__kill` | $0.045275$ | $0.027132$ | $0.094963$ | $2.434508$ | $0.014912$ | $0.037958$ | $0.000000$ | Grande |
| `config_4` vs `config_8` | `rnsgaiii__elit_off__penalty` $-$ `rnsgaiii__elit_off__kill` | $0.033059$ | $0.210899$ | $0.656131$ | $2.786159$ | $0.005334$ | $0.021335$ | $0.000000$ | Grande |
| `config_4` vs `config_6` | `rnsgaiii__elit_off__penalty` $-$ `nsgaiii__elit_off__kill` | $0.031447$ | $0.262861$ | $0.669101$ | $2.434508$ | $0.014912$ | $0.037958$ | $0.000000$ | Grande |
| `config_2` vs `config_8` | `nsgaiii__elit_off__penalty` $-$ `rnsgaiii__elit_off__kill` | $0.031558$ | $0.259039$ | $0.669101$ | $2.705009$ | $0.006830$ | $0.023045$ | $0.000000$ | Grande |
| `config_2` vs `config_6` | `nsgaiii__elit_off__penalty` $-$ `nsgaiii__elit_off__kill` | $0.029947$ | $0.318444$ | $0.743036$ | $2.353358$ | $0.018605$ | $0.043411$ | $0.000000$ | Grande |

* **Contabilização de Pares Significativos (Spacing):** $p_{\text{tukey}} \le 0.05$: $8$ | $p_{\text{tukey\_bh}} \le 0.05$: $6$ | $p_{\text{dunn\_raw}} \le 0.05$: $16$ | $p_{\text{dunn\_bh}} \le 0.05$: $13$.

### Tabela 5.4: Matriz Completa $8 \times 8$ de Tamanho de Efeito Vargha-Delaney $\hat{A}_{12}$ (*Spacing*)
*Descrição: Matriz $\hat{A}_{12}$ para o indicador Spacing (orientada para menor Spacing: as configurações `config_5` a `config_8` apresentam $\hat{A}_{12} = 0.92$ a $1.00$ contra `config_1` a `config_4`).*

| Config. | `config_1` | `config_2` | `config_3` | `config_4` | `config_5` | `config_6` | `config_7` | `config_8` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`config_1`** | $0.50$ | $0.20$ | $0.40$ | $0.24$ | $0.00$ | $0.00$ | $0.00$ | $0.00$ |
| **`config_2`** | $0.80$ | $0.50$ | $0.60$ | $0.48$ | $0.08$ | $0.00$ | $0.08$ | $0.00$ |
| **`config_3`** | $0.60$ | $0.40$ | $0.50$ | $0.36$ | $0.00$ | $0.00$ | $0.00$ | $0.00$ |
| **`config_4`** | $0.76$ | $0.52$ | $0.64$ | $0.50$ | $0.00$ | $0.00$ | $0.00$ | $0.00$ |
| **`config_5`** | $1.00$ | $0.92$ | $1.00$ | $1.00$ | $0.50$ | $0.40$ | $0.40$ | $0.24$ |
| **`config_6`** | $1.00$ | $1.00$ | $1.00$ | $1.00$ | $0.60$ | $0.50$ | $0.52$ | $0.40$ |
| **`config_7`** | $1.00$ | $0.92$ | $1.00$ | $1.00$ | $0.60$ | $0.48$ | $0.50$ | $0.32$ |
| **`config_8`** | $1.00$ | $1.00$ | $1.00$ | $1.00$ | $0.76$ | $0.60$ | $0.68$ | $0.50$ |

### Tabela 5.5: Síntese de Magnitudes de Efeito $\hat{A}_{12}$ nos 28 Pares (*Spacing*)
*Descrição: Contagem de pares por magnitude de efeito para o indicador Spacing.*

| Magnitude $\hat{A}_{12}$ | Quantidade de Pares | Proporção ($\text{Total} = 28$) |
| :--- | :---: | :---: |
| **Grande** | $19$ | $67.86\%$ |
| **Pequena** | $6$ | $21.43\%$ |
| **Desprezível** | $2$ | $7.14\%$ |
| **Média** | $1$ | $3.57\%$ |

---

## 6. Mapeamento Integral dos Pares com Magnitude Grande e Média

Esta seção consolida todos os pares de configurações (dentre os 28 possíveis por indicador) que obtiveram magnitude de efeito prática **Grande** ou **Média** segundo a métrica de Vargha-Delaney ($\hat{A}_{12}$), permitindo auditar simultaneamente a significância paramétrica (Tukey) e não-paramétrica (Dunn).

### Tabela 6.1: Todos os Pares de Magnitude Grande e Média — Hipervolume (HV)
*Descrição: Total de 21 pares ($14$ Grandes e $7$ Médios) com relevância prática na qualidade do volume dominado pelas arquiteturas de microsserviços.*

| Par de Configurações | $\hat{A}_{12}$ | Magnitude | $z_{\text{dunn}}$ | $p_{\text{dunn}}$ | $p_{\text{dunn\_bh}}$ | $\text{diff}$ | $p_{\text{tukey}}$ | $p_{\text{tukey\_bh}}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `config_4` vs `config_8` | $1.000000$ | Grande | $3.164860$ | $0.001552$ | $0.043444$ | $0.276281$ | $0.018387$ | $0.396058$ |
| `config_4` vs `config_7` | $1.000000$ | Grande | $2.921410$ | $0.003485$ | $0.048783$ | $0.259290$ | $0.032036$ | $0.396058$ |
| `config_1` vs `config_8` | $1.000000$ | Grande | $2.596809$ | $0.009409$ | $0.083167$ | $0.202867$ | $0.165334$ | $0.925868$ |
| `config_4` vs `config_5` | $1.000000$ | Grande | $2.515658$ | $0.011881$ | $0.083167$ | $0.241311$ | $0.056118$ | $0.396058$ |
| `config_4` vs `config_6` | $1.000000$ | Grande | $2.136957$ | $0.032601$ | $0.152140$ | $0.241041$ | $0.056580$ | $0.396058$ |
| `config_1` vs `config_7` | $0.960000$ | Grande | $2.353358$ | $0.018605$ | $0.104186$ | $0.185876$ | $0.250015$ | $1.000000$ |
| `config_1` vs `config_5` | $0.920000$ | Grande | $1.947606$ | $0.051462$ | $0.204017$ | $0.167897$ | $0.367679$ | $1.000000$ |
| `config_1` vs `config_6` | $0.880000$ | Grande | $1.568905$ | $0.116670$ | $0.287254$ | $0.167627$ | $0.369653$ | $1.000000$ |
| `config_2` vs `config_8` | $0.840000$ | Grande | $1.893506$ | $0.058291$ | $0.204017$ | $0.174110$ | $0.323889$ | $1.000000$ |
| `config_2` vs `config_7` | $0.800000$ | Grande | $1.650055$ | $0.098932$ | $0.277008$ | $0.157119$ | $0.450338$ | $1.000000$ |
| `config_3` vs `config_8` | $0.760000$ | Grande | $1.785306$ | $0.074212$ | $0.230881$ | $0.165646$ | $0.384290$ | $1.000000$ |
| `config_6` vs `config_8` | $0.760000$ | Grande | $1.027903$ | $0.303995$ | $0.500698$ | $0.035240$ | $0.999738$ | $1.000000$ |
| `config_6` vs `config_7` | $0.760000$ | Grande | $0.784453$ | $0.432775$ | $0.598412$ | $0.018249$ | $0.999997$ | $1.000000$ |
| `config_2` vs `config_4` | $0.280000$ | Grande | $-1.271354$ | $0.203603$ | $0.398324$ | $-0.102171$ | $0.872187$ | $1.000000$ |
| `config_3` vs `config_7` | $0.680000$ | Média | $1.541855$ | $0.123109$ | $0.287254$ | $0.148656$ | $0.519661$ | $1.000000$ |
| `config_2` vs `config_5` | $0.680000$ | Média | $1.244304$ | $0.213388$ | $0.398324$ | $0.139140$ | $0.599759$ | $1.000000$ |
| `config_3` vs `config_5` | $0.680000$ | Média | $1.136104$ | $0.255913$ | $0.447848$ | $0.130677$ | $0.670427$ | $1.000000$ |
| `config_2` vs `config_6` | $0.680000$ | Média | $0.865603$ | $0.386708$ | $0.598412$ | $0.138870$ | $0.602039$ | $1.000000$ |
| `config_3` vs `config_6` | $0.680000$ | Média | $0.757402$ | $0.448809$ | $0.598412$ | $0.130407$ | $0.672646$ | $1.000000$ |
| `config_3` vs `config_4` | $0.320000$ | Média | $-1.379555$ | $0.167724$ | $0.361251$ | $-0.110634$ | $0.821007$ | $1.000000$ |
| `config_1` vs `config_4` | $0.320000$ | Média | $-0.568052$ | $0.570000$ | $0.665000$ | $-0.073414$ | $0.975499$ | $1.000000$ |

### Tabela 6.2: Todos os Pares de Magnitude Grande e Média — $\text{IGD}^+$
*Descrição: Total de 14 pares ($10$ Grandes e $4$ Médios) com efeito prático expressivo sobre a convergência e cobertura medida pelo $\text{IGD}^+$.*

| Par de Configurações | $\hat{A}_{12}$ | Magnitude | $z_{\text{dunn}}$ | $p_{\text{dunn}}$ | $p_{\text{dunn\_bh}}$ | $\text{diff}$ | $p_{\text{tukey}}$ | $p_{\text{tukey\_bh}}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `config_4` vs `config_7` | $1.000000$ | Grande | $-2.921410$ | $0.003485$ | $0.097566$ | $-0.096571$ | $0.072659$ | $1.000000$ |
| `config_4` vs `config_8` | $0.960000$ | Grande | $-2.677959$ | $0.007407$ | $0.103701$ | $-0.089979$ | $0.114213$ | $1.000000$ |
| `config_4` vs `config_5` | $0.960000$ | Grande | $-2.326308$ | $0.020002$ | $0.186687$ | $-0.083629$ | $0.171281$ | $1.000000$ |
| `config_4` vs `config_6` | $0.920000$ | Grande | $-2.082857$ | $0.037264$ | $0.260850$ | $-0.086302$ | $0.144990$ | $1.000000$ |
| `config_1` vs `config_4` | $0.120000$ | Grande | $1.568905$ | $0.116670$ | $0.466680$ | $0.061029$ | $0.533233$ | $1.000000$ |
| `config_2` vs `config_4` | $0.160000$ | Grande | $1.920556$ | $0.054788$ | $0.306811$ | $0.067639$ | $0.404611$ | $1.000000$ |
| `config_3` vs `config_4` | $0.240000$ | Grande | $1.758256$ | $0.078704$ | $0.367285$ | $0.061445$ | $0.524844$ | $1.000000$ |
| `config_1` vs `config_7` | $0.760000$ | Grande | $-1.352504$ | $0.176214$ | $0.616749$ | $-0.035542$ | $0.944670$ | $1.000000$ |
| `config_6` vs `config_7` | $0.760000$ | Grande | $-0.838553$ | $0.401720$ | $0.837776$ | $-0.010269$ | $0.999976$ | $1.000000$ |
| `config_1` vs `config_8` | $0.720000$ | Grande | $-1.109054$ | $0.267407$ | $0.748740$ | $-0.028950$ | $0.981589$ | $1.000000$ |
| `config_3` vs `config_7` | $0.680000$ | Média | $-1.163154$ | $0.244767$ | $0.748740$ | $-0.035126$ | $0.947879$ | $1.000000$ |
| `config_3` vs `config_8` | $0.680000$ | Média | $-0.919703$ | $0.357728$ | $0.834699$ | $-0.028534$ | $0.983037$ | $1.000000$ |
| `config_1` vs `config_5` | $0.680000$ | Média | $-0.757402$ | $0.448809$ | $0.837776$ | $-0.022600$ | $0.995736$ | $1.000000$ |
| `config_1` vs `config_6` | $0.680000$ | Média | $-0.513952$ | $0.607286$ | $0.871069$ | $-0.025273$ | $0.991623$ | $1.000000$ |

### Tabela 6.3: Todos os Pares de Magnitude Grande e Média — $\text{ED}_{\text{média}}$
*Descrição: Total de 13 pares ($10$ Grandes e $3$ Médios) com diferenças práticas relevantes na distância média até o ponto aspiracional de microsserviços.*

| Par de Configurações | $\hat{A}_{12}$ | Magnitude | $z_{\text{dunn}}$ | $p_{\text{dunn}}$ | $p_{\text{dunn\_bh}}$ | $\text{diff}$ | $p_{\text{tukey}}$ | $p_{\text{tukey\_bh}}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `config_1` vs `config_4` | $0.000000$ | Grande | $2.461558$ | $0.013833$ | $0.186687$ | $0.135200$ | $0.175309$ | $1.000000$ |
| `config_4` vs `config_5` | $1.000000$ | Grande | $-2.434508$ | $0.014912$ | $0.186687$ | $-0.109670$ | $0.406639$ | $1.000000$ |
| `config_4` vs `config_6` | $0.920000$ | Grande | $-2.028757$ | $0.042483$ | $0.237905$ | $-0.103053$ | $0.484723$ | $1.000000$ |
| `config_3` vs `config_4` | $0.120000$ | Grande | $2.028757$ | $0.042483$ | $0.237905$ | $0.098762$ | $0.537609$ | $1.000000$ |
| `config_4` vs `config_7` | $0.800000$ | Grande | $-1.758256$ | $0.078704$ | $0.367285$ | $-0.073357$ | $0.832703$ | $1.000000$ |
| `config_2` vs `config_4` | $0.200000$ | Grande | $2.326308$ | $0.020002$ | $0.186687$ | $0.118646$ | $0.311139$ | $1.000000$ |
| `config_1` vs `config_8` | $0.200000$ | Grande | $1.541855$ | $0.123109$ | $0.454376$ | $0.086588$ | $0.688600$ | $1.000000$ |
| `config_5` vs `config_8` | $0.200000$ | Grande | $1.514805$ | $0.129822$ | $0.454376$ | $0.061058$ | $0.926883$ | $1.000000$ |
| `config_6` vs `config_8` | $0.240000$ | Grande | $1.109054$ | $0.267407$ | $0.680672$ | $0.054441$ | $0.959066$ | $1.000000$ |
| `config_3` vs `config_8` | $0.280000$ | Grande | $1.109054$ | $0.267407$ | $0.680672$ | $0.050150$ | $0.973641$ | $1.000000$ |
| `config_4` vs `config_8` | $0.680000$ | Média | $-0.919703$ | $0.357728$ | $0.834699$ | $-0.048612$ | $0.977805$ | $1.000000$ |
| `config_2` vs `config_8` | $0.320000$ | Média | $1.406605$ | $0.159545$ | $0.496361$ | $0.070035$ | $0.862500$ | $1.000000$ |
| `config_2` vs `config_7` | $0.320000$ | Média | $0.568052$ | $0.570000$ | $0.917904$ | $0.045289$ | $0.985118$ | $1.000000$ |

### Tabela 6.4: Todos os Pares de Magnitude Grande e Média — $\text{ED}_{\text{min}}$
*Descrição: Total de 11 pares ($9$ Grandes e $2$ Médios) com impacto substancial na qualidade da melhor arquitetura de compromisso encontrada.*

| Par de Configurações | $\hat{A}_{12}$ | Magnitude | $z_{\text{dunn}}$ | $p_{\text{dunn}}$ | $p_{\text{dunn\_bh}}$ | $\text{diff}$ | $p_{\text{tukey}}$ | $p_{\text{tukey\_bh}}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `config_4` vs `config_6` | $0.960000$ | Grande | $-2.299258$ | $0.021490$ | $0.200576$ | $-0.133663$ | $0.070197$ | $0.982762$ |
| `config_4` vs `config_7` | $0.960000$ | Grande | $-2.677959$ | $0.007407$ | $0.200576$ | $-0.133875$ | $0.069432$ | $0.982762$ |
| `config_4` vs `config_8` | $0.920000$ | Grande | $-2.380408$ | $0.017293$ | $0.200576$ | $-0.122325$ | $0.123242$ | $1.000000$ |
| `config_4` vs `config_5` | $0.920000$ | Grande | $-2.136957$ | $0.032601$ | $0.208680$ | $-0.118506$ | $0.147318$ | $1.000000$ |
| `config_1` vs `config_4` | $0.120000$ | Grande | $1.595955$ | $0.110499$ | $0.515661$ | $0.092001$ | $0.420124$ | $1.000000$ |
| `config_2` vs `config_4` | $0.160000$ | Grande | $2.082857$ | $0.037264$ | $0.208680$ | $0.099334$ | $0.326165$ | $1.000000$ |
| `config_3` vs `config_4` | $0.280000$ | Grande | $1.433655$ | $0.151671$ | $0.606683$ | $0.073413$ | $0.688777$ | $1.000000$ |
| `config_1` vs `config_7` | $0.720000$ | Grande | $-1.082004$ | $0.279251$ | $0.868781$ | $-0.041875$ | $0.975789$ | $1.000000$ |
| `config_1` vs `config_8` | $0.720000$ | Grande | $-0.784453$ | $0.432775$ | $0.915454$ | $-0.030325$ | $0.996367$ | $1.000000$ |
| `config_3` vs `config_7` | $0.680000$ | Média | $-1.244304$ | $0.213388$ | $0.746857$ | $-0.060463$ | $0.851502$ | $1.000000$ |
| `config_3` vs `config_8` | $0.680000$ | Média | $-0.946753$ | $0.343765$ | $0.915454$ | $-0.048913$ | $0.944869$ | $1.000000$ |

### Tabela 6.5: Todos os Pares de Magnitude Grande e Média — *Spacing*
*Descrição: Total de 20 pares ($19$ Grandes e $1$ Médio) evidenciando a forte dicotomia estrutural na distribuição das soluções entre os métodos de penalização e descarte.*

| Par de Configurações | $\hat{A}_{12}$ | Magnitude | $z_{\text{dunn}}$ | $p_{\text{dunn}}$ | $p_{\text{dunn\_bh}}$ | $\text{diff}$ | $p_{\text{tukey}}$ | $p_{\text{tukey\_bh}}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `config_1` vs `config_8` | $0.000000$ | Grande | $3.516512$ | $0.000437$ | $0.012243$ | $0.056769$ | $0.002666$ | $0.049099$ |
| `config_1` vs `config_6` | $0.000000$ | Grande | $3.164860$ | $0.001552$ | $0.014481$ | $0.055157$ | $0.003742$ | $0.049099$ |
| `config_3` vs `config_8` | $0.000000$ | Grande | $3.164860$ | $0.001552$ | $0.014481$ | $0.051735$ | $0.007594$ | $0.049099$ |
| `config_1` vs `config_7` | $0.000000$ | Grande | $3.029610$ | $0.002449$ | $0.017141$ | $0.051562$ | $0.007865$ | $0.049099$ |
| `config_1` vs `config_5` | $0.000000$ | Grande | $2.786159$ | $0.005334$ | $0.021335$ | $0.050309$ | $0.010135$ | $0.049099$ |
| `config_3` vs `config_6` | $0.000000$ | Grande | $2.813209$ | $0.004905$ | $0.021335$ | $0.050123$ | $0.010521$ | $0.049099$ |
| `config_4` vs `config_8` | $0.000000$ | Grande | $2.786159$ | $0.005334$ | $0.021335$ | $0.033059$ | $0.210899$ | $0.656131$ |
| `config_2` vs `config_8` | $0.000000$ | Grande | $2.705009$ | $0.006830$ | $0.023045$ | $0.031558$ | $0.259039$ | $0.669101$ |
| `config_3` vs `config_7` | $0.000000$ | Grande | $2.677959$ | $0.007407$ | $0.023045$ | $0.046528$ | $0.021357$ | $0.085428$ |
| `config_3` vs `config_5` | $0.000000$ | Grande | $2.434508$ | $0.014912$ | $0.037958$ | $0.045275$ | $0.027132$ | $0.094963$ |
| `config_4` vs `config_6` | $0.000000$ | Grande | $2.434508$ | $0.014912$ | $0.037958$ | $0.031447$ | $0.262861$ | $0.669101$ |
| `config_2` vs `config_6` | $0.000000$ | Grande | $2.353358$ | $0.018605$ | $0.043411$ | $0.029947$ | $0.318444$ | $0.743036$ |
| `config_4` vs `config_7` | $0.000000$ | Grande | $2.299258$ | $0.021490$ | $0.046287$ | $0.027852$ | $0.406729$ | $0.876031$ |
| `config_4` vs `config_5` | $0.000000$ | Grande | $2.055807$ | $0.039801$ | $0.074295$ | $0.026599$ | $0.464465$ | $0.884268$ |
| `config_2` vs `config_7` | $0.080000$ | Grande | $2.218107$ | $0.026548$ | $0.053095$ | $0.026352$ | $0.476223$ | $0.884268$ |
| `config_2` vs `config_5` | $0.080000$ | Grande | $1.974656$ | $0.048307$ | $0.084537$ | $0.025099$ | $0.536877$ | $0.884268$ |
| `config_1` vs `config_2` | $0.200000$ | Grande | $0.811503$ | $0.417077$ | $0.685521$ | $0.025211$ | $0.531398$ | $0.884268$ |
| `config_1` vs `config_4` | $0.240000$ | Grande | $0.730352$ | $0.465175$ | $0.685521$ | $0.023710$ | $0.605268$ | $0.941527$ |
| `config_5` vs `config_8` | $0.240000$ | Grande | $0.730352$ | $0.465175$ | $0.685521$ | $0.006459$ | $0.999589$ | $1.000000$ |
| `config_7` vs `config_8` | $0.320000$ | Média | $0.486902$ | $0.626328$ | $0.812112$ | $0.005206$ | $0.999902$ | $1.000000$ |

---

## 7. Auditoria de Postos Médios ($\bar{R}$) e Parâmetros de Empate (Kruskal-Wallis / Dunn)

Para validar a exatidão matemática das estatísticas $H$ (Kruskal-Wallis) e $z$ (Dunn), audita-se a ocorrência de empates (*ties*) nas $N = 40$ observações e os postos médios ($\bar{R}_i$) de cada configuração experimental.

### Tabela 7.1: Diagnóstico de Unicidade e Variância dos Postos ($N = 40$)
*Descrição: Confirma a ausência total de empates ($40/40$ valores contínuos únicos) em todos os 5 indicadores, resultando em fator de correção de empates $T = 0$ e variância exata dos postos $\sigma^2 = \frac{N(N+1)}{12} = \frac{40 \times 41}{12} = 136.666667$.*

| Indicador Auditado | Valores Únicos ($N = 40$) | Fator de Correção de Empates ($T$) | Variância dos Postos ($\sigma^2$) |
| :--- | :---: | :---: | :---: |
| **`hv`** | $40/40$ | $0$ | $136.666667$ |
| **`igd_plus`** | $40/40$ | $0$ | $136.666667$ |
| **`ed_media`** | $40/40$ | $0$ | $136.666667$ |
| **`ed_min`** | $40/40$ | $0$ | $136.666667$ |
| **`spacing`** | $40/40$ | $0$ | $136.666667$ |

### Tabela 7.2: Postos Médios ($\bar{R}$) por Configuração Experimental em Todos os Indicadores
*Descrição: Posto médio ($\bar{R} \in [1, 40]$) obtido por cada configuração. Para `HV`, postos **maiores** indicam melhor desempenho; para `IGD_PLUS`, `ED_MEDIA`, `ED_MIN` e `SPACING`, postos **menores** refletem menores valores absolutos do indicador. A `config_4` lidera simultaneamente em HV (maior posto: $33.40$) e nos três indicadores de convergência/distância (menores postos: $6.40$, $7.60$ e $7.00$).*

| ID da Config. | Configuração Experimental ($F_1 \times F_2 \times F_3$) | $\bar{R}_{\text{hv}}$ | $\bar{R}_{\text{igd\_plus}}$ | $\bar{R}_{\text{ed\_media}}$ | $\bar{R}_{\text{ed\_min}}$ | $\bar{R}_{\text{spacing}}$ |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `config_1` | `nsgaiii__elit_on__penalty` | $29.20$ | $18.00$ | $25.80$ | $18.80$ | $33.80$ |
| `config_2` | `nsgaiii__elit_off__penalty` | $24.00$ | $20.60$ | $24.80$ | $22.40$ | $27.80$ |
| `config_3` | `rnsgaiii__elit_on__penalty` | $23.20$ | $19.40$ | $22.60$ | $17.60$ | $31.20$ |
| **`config_4`** | **`rnsgaiii__elit_off__penalty`** | **$33.40$** | **$6.40$** | **$7.60$** | **$7.00$** | **$28.40$** |
| `config_5` | `nsgaiii__elit_on__kill` | $14.80$ | $23.60$ | $25.60$ | $22.80$ | $13.20$ |
| `config_6` | `nsgaiii__elit_off__kill` | $17.60$ | $21.80$ | $22.60$ | $24.00$ | $10.40$ |
| `config_7` | `rnsgaiii__elit_on__kill` | $11.80$ | $28.00$ | $20.60$ | $26.80$ | $11.40$ |
| `config_8` | `rnsgaiii__elit_off__kill` | $10.00$ | $26.20$ | $14.40$ | $24.60$ | $7.80$ |

---

## 8. Estatísticas Descritivas das Interações Bidimensionais $2 \times 2$ ($n = 10$ por célula)

Ao colapsar um dos três fatores do experimento fatorial $2^3$, cada célula bidimensional passa a contar com $n = 10$ execuções independentes, fornecendo estimativas paramétricas ($\text{Média} \pm \text{DP}$) e não-paramétricas ($\text{Mediana}, \text{IQR}$) robustas para auditar sinergias entre os componentes algorítmicos.

### Tabela 8.1: Interação $2 \times 2$ entre Algoritmo e Manuseio de Restrições ($F_1 \times F_3$, $n = 10$ por célula)
*Descrição: Desempenho combinado entre a escolha do algoritmo (`NSGA-III` vs. `R-NSGA-III`) e o método de restrição (`PENALTY` vs. `KILL`). Evidencia que o `R-NSGA-III` combinado com `PENALTY` atinge a maior média e mediana de Hipervolume ($1.0090 \pm 0.1576$, mediana $1.0242$) e os menores erros em $\text{IGD}^+$, $\text{ED}_{\text{média}}$ e $\text{ED}_{\text{min}}$.*

| Indicador | `NSGA-III` $\times$ `PENALTY` | `NSGA-III` $\times$ `KILL` | `R-NSGA-III` $\times$ `PENALTY` | `R-NSGA-III` $\times$ `KILL` |
| :--- | :---: | :---: | :---: | :---: |
| **`hv`** | $0.9765 \pm 0.1438$<br>($\text{med } 0.9599, \text{IQR } 0.1815$) | $0.8231 \pm 0.0817$<br>($\text{med } 0.8576, \text{IQR } 0.0426$) | $1.0090 \pm 0.1576$<br>($\text{med } 1.0242, \text{IQR } 0.1766$) | $0.7965 \pm 0.0492$<br>($\text{med } 0.7867, \text{IQR } 0.0886$) |
| **`igd_plus`** | $0.1465 \pm 0.0485$<br>($\text{med } 0.1380, \text{IQR } 0.0653$) | $0.1671 \pm 0.0440$<br>($\text{med } 0.1510, \text{IQR } 0.0245$) | $0.1129 \pm 0.0700$<br>($\text{med } 0.0916, \text{IQR } 0.0886$) | $0.1754 \pm 0.0257$<br>($\text{med } 0.1863, \text{IQR } 0.0323$) |
| **`ed_media`** | $0.6742 \pm 0.1047$<br>($\text{med } 0.6598, \text{IQR } 0.1431$) | $0.6536 \pm 0.0644$<br>($\text{med } 0.6487, \text{IQR } 0.0503$) | $0.5966 \pm 0.0768$<br>($\text{med } 0.5753, \text{IQR } 0.0754$) | $0.6082 \pm 0.0713$<br>($\text{med } 0.6193, \text{IQR } 0.1062$) |
| **`ed_min`** | $0.4479 \pm 0.0636$<br>($\text{med } 0.4604, \text{IQR } 0.0693$) | $0.4783 \pm 0.0632$<br>($\text{med } 0.4720, \text{IQR } 0.0557$) | $0.3890 \pm 0.0903$<br>($\text{med } 0.3544, \text{IQR } 0.1245$) | $0.4803 \pm 0.0452$<br>($\text{med } 0.4970, \text{IQR } 0.0669$) |
| **`spacing`** | $0.0758 \pm 0.0269$<br>($\text{med } 0.0647, \text{IQR } 0.0306$) | $0.0357 \pm 0.0066$<br>($\text{med } 0.0338, \text{IQR } 0.0058$) | $0.0741 \pm 0.0307$<br>($\text{med } 0.0662, \text{IQR } 0.0249$) | $0.0343 \pm 0.0086$<br>($\text{med } 0.0321, \text{IQR } 0.0126$) |

### Tabela 8.2: Interação $2 \times 2$ entre Algoritmo e Elitismo ($F_1 \times F_2$, $n = 10$ por célula)
*Descrição: Avalia o efeito da ativação/desativação do arquivo de elitismo dentro de cada algoritmo. Demonstra que o `R-NSGA-III` opera melhor sob `ELIT_OFF` em todos os indicadores de convergência e diversidade.*

| Indicador | `NSGA-III` $\times$ `ELIT_ON` | `NSGA-III` $\times$ `ELIT_OFF` | `R-NSGA-III` $\times$ `ELIT_ON` | `R-NSGA-III` $\times$ `ELIT_OFF` |
| :--- | :---: | :---: | :---: | :---: |
| **`hv`** | $0.9070 \pm 0.1213$<br>($\text{med } 0.8676, \text{IQR } 0.1376$) | $0.8927 \pm 0.1600$<br>($\text{med } 0.8676, \text{IQR } 0.0911$) | $0.8794 \pm 0.1556$<br>($\text{med } 0.8253, \text{IQR } 0.1593$) | $0.9262 \pm 0.1640$<br>($\text{med } 0.9014, \text{IQR } 0.2544$) |
| **`igd_plus`** | $0.1545 \pm 0.0344$<br>($\text{med } 0.1525, \text{IQR } 0.0435$) | $0.1591 \pm 0.0577$<br>($\text{med } 0.1488, \text{IQR } 0.0612$) | $0.1611 \pm 0.0597$<br>($\text{med } 0.1647, \text{IQR } 0.0338$) | $0.1271 \pm 0.0593$<br>($\text{med } 0.1364, \text{IQR } 0.0898$) |
| **`ed_media`** | $0.6697 \pm 0.0776$<br>($\text{med } 0.6492, \text{IQR } 0.0676$) | $0.6581 \pm 0.0961$<br>($\text{med } 0.6487, \text{IQR } 0.1464$) | $0.6333 \pm 0.0708$<br>($\text{med } 0.6408, \text{IQR } 0.0568$) | $0.5716 \pm 0.0627$<br>($\text{med } 0.5584, \text{IQR } 0.0384$) |
| **`ed_min`** | $0.4575 \pm 0.0532$<br>($\text{med } 0.4604, \text{IQR } 0.0550$) | $0.4687 \pm 0.0752$<br>($\text{med } 0.4740, \text{IQR } 0.0688$) | $0.4559 \pm 0.0825$<br>($\text{med } 0.4674, \text{IQR } 0.0811$) | $0.4134 \pm 0.0838$<br>($\text{med } 0.4228, \text{IQR } 0.1395$) |
| **`spacing`** | $0.0633 \pm 0.0343$<br>($\text{med } 0.0503, \text{IQR } 0.0487$) | $0.0482 \pm 0.0189$<br>($\text{med } 0.0402, \text{IQR } 0.0288$) | $0.0601 \pm 0.0370$<br>($\text{med } 0.0497, \text{IQR } 0.0352$) | $0.0482 \pm 0.0211$<br>($\text{med } 0.0462, \text{IQR } 0.0242$) |

### Tabela 8.3: Interação $2 \times 2$ entre Elitismo e Manuseio de Restrições ($F_2 \times F_3$, $n = 10$ por célula)
*Descrição: Cruza o regime de elitismo com a estratégia de tratamento de restrições. A combinação `ELIT_OFF` $\times$ `PENALTY` maximiza o Hipervolume médio ($1.0132 \pm 0.1497$) e minimiza $\text{IGD}^+$, $\text{ED}_{\text{média}}$ e $\text{ED}_{\text{min}}$.*

| Indicador | `ELIT_ON` $\times$ `PENALTY` | `ELIT_ON` $\times$ `KILL` | `ELIT_OFF` $\times$ `PENALTY` | `ELIT_OFF` $\times$ `KILL` |
| :--- | :---: | :---: | :---: | :---: |
| **`hv`** | $0.9723 \pm 0.1508$<br>($\text{med } 0.9698, \text{IQR } 0.2369$) | $0.8140 \pm 0.0520$<br>($\text{med } 0.8270, \text{IQR } 0.0894$) | $1.0132 \pm 0.1497$<br>($\text{med } 1.0202, \text{IQR } 0.1685$) | $0.8057 \pm 0.0822$<br>($\text{med } 0.8431, \text{IQR } 0.1058$) |
| **`igd_plus`** | $0.1434 \pm 0.0584$<br>($\text{med } 0.1403, \text{IQR } 0.0512$) | $0.1722 \pm 0.0300$<br>($\text{med } 0.1686, \text{IQR } 0.0327$) | $0.1160 \pm 0.0636$<br>($\text{med } 0.1050, \text{IQR } 0.0805$) | $0.1703 \pm 0.0417$<br>($\text{med } 0.1548, \text{IQR } 0.0436$) |
| **`ed_media`** | $0.6642 \pm 0.0899$<br>($\text{med } 0.6385, \text{IQR } 0.0986$) | $0.6388 \pm 0.0577$<br>($\text{med } 0.6514, \text{IQR } 0.0387$) | $0.6066 \pm 0.1013$<br>($\text{med } 0.5753, \text{IQR } 0.1287$) | $0.6231 \pm 0.0831$<br>($\text{med } 0.6022, \text{IQR } 0.0878$) |
| **`ed_min`** | $0.4350 \pm 0.0776$<br>($\text{med } 0.4463, \text{IQR } 0.0920$) | $0.4784 \pm 0.0507$<br>($\text{med } 0.4843, \text{IQR } 0.0748$) | $0.4019 \pm 0.0866$<br>($\text{med } 0.3949, \text{IQR } 0.1414$) | $0.4802 \pm 0.0589$<br>($\text{med } 0.4740, \text{IQR } 0.0544$) |
| **`spacing`** | $0.0859 \pm 0.0343$<br>($\text{med } 0.0794, \text{IQR } 0.0399$) | $0.0375 \pm 0.0087$<br>($\text{med } 0.0349, \text{IQR } 0.0155$) | $0.0640 \pm 0.0148$<br>($\text{med } 0.0615, \text{IQR } 0.0182$) | $0.0325 \pm 0.0054$<br>($\text{med } 0.0318, \text{IQR } 0.0039$) |

---

## 9. Contrastes Condicionais (Efeitos Simples) nas Interações $2 \times 2$ ($n = 10$ vs. $n = 10$)

### Tabela 9.1: Auditoria de Efeitos Simples via Mann-Whitney $U$ e Vargha-Delaney $\hat{A}_{12}$
*Descrição: Avalia o efeito isolado de um fator mantendo outro fator fixo ($n = 10$ vs. $n = 10$). Confirma estatisticamente que `PENALTY` supera `KILL` dentro do `R-NSGA-III` em quase todos os indicadores ($p = 0.0073$ em HV, $p = 0.0140$ em $\text{IGD}^+$, $p = 0.0211$ em $\text{ED}_{\text{min}}$), e que o `R-NSGA-III` supera significativamente o `NSGA-III` em $\text{ED}_{\text{média}}$ quando `ELIT_OFF` está ativo ($p = 0.0312$, $\hat{A}_{12} = 0.79$).*

| Contraste Condicional (Efeito Simples) | Indicador | $\Delta\text{Média}\ (\%)$ | Estatística $U$ | $p_{\text{raw}}$ | $\hat{A}_{12}$ | Magnitude |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `F1\|PENALTY: R-NSGA-III vs NSGA-III (sob PENALTY)` | `hv` | $+3.3256\%$ | $58.0000$ | $0.5708$ | $0.5800$ | Pequena |
| `F1\|PENALTY: R-NSGA-III vs NSGA-III (sob PENALTY)` | `igd_plus` | $-22.9482\%$ | $31.0000$ | $0.1620$ | $0.6900$ | Média |
| `F1\|PENALTY: R-NSGA-III vs NSGA-III (sob PENALTY)` | `ed_media` | $-11.5017\%$ | $26.0000$ | $0.0757$ | $0.7400$ | Grande |
| `F1\|PENALTY: R-NSGA-III vs NSGA-III (sob PENALTY)` | `ed_min` | $-13.1635\%$ | $27.0000$ | $0.0890$ | $0.7300$ | Grande |
| `F1\|PENALTY: R-NSGA-III vs NSGA-III (sob PENALTY)` | `spacing` | $-2.3302\%$ | $43.0000$ | $0.6232$ | $0.5700$ | Pequena |
| `F1\|KILL: R-NSGA-III vs NSGA-III (sob KILL)` | `hv` | $-3.2326\%$ | $30.0000$ | $0.1405$ | $0.3000$ | Média |
| `F1\|KILL: R-NSGA-III vs NSGA-III (sob KILL)` | `igd_plus` | $+4.9729\%$ | $66.0000$ | $0.2413$ | $0.3400$ | Média |
| `F1\|KILL: R-NSGA-III vs NSGA-III (sob KILL)` | `ed_media` | $-6.9425\%$ | $34.0000$ | $0.2413$ | $0.6600$ | Média |
| `F1\|KILL: R-NSGA-III vs NSGA-III (sob KILL)` | `ed_min` | $+0.4214\%$ | $57.0000$ | $0.6232$ | $0.4300$ | Pequena |
| `F1\|KILL: R-NSGA-III vs NSGA-III (sob KILL)` | `spacing` | $-4.0122\%$ | $39.0000$ | $0.4274$ | $0.6100$ | Pequena |
| `F3\|NSGA-III: PENALTY vs KILL (em NSGA-III)` | `hv` | $+18.6339\%$ | $79.0000$ | $0.0312$ | $0.7900$ | Grande |
| `F3\|NSGA-III: PENALTY vs KILL (em NSGA-III)` | `igd_plus` | $-12.3470\%$ | $36.0000$ | $0.3075$ | $0.6400$ | Pequena |
| `F3\|NSGA-III: PENALTY vs KILL (em NSGA-III)` | `ed_media` | $+3.1458\%$ | $55.0000$ | $0.7337$ | $0.4500$ | Desprezível |
| `F3\|NSGA-III: PENALTY vs KILL (em NSGA-III)` | `ed_min` | $-6.3590\%$ | $42.0000$ | $0.5708$ | $0.5800$ | Pequena |
| `F3\|NSGA-III: PENALTY vs KILL (em NSGA-III)` | `spacing` | $+112.4347\%$ | $98.0000$ | $0.0003$ | $0.0200$ | Grande |
| `F3\|R-NSGA-III: PENALTY vs KILL (em R-NSGA-III)` | `hv` | $+26.6741\%$ | $86.0000$ | $0.0073$ | $0.8600$ | Grande |
| `F3\|R-NSGA-III: PENALTY vs KILL (em R-NSGA-III)` | `igd_plus` | $-35.6613\%$ | $17.0000$ | $0.0140$ | $0.8300$ | Grande |
| `F3\|R-NSGA-III: PENALTY vs KILL (em R-NSGA-III)` | `ed_media` | $-1.9077\%$ | $45.0000$ | $0.7337$ | $0.5500$ | Desprezível |
| `F3\|R-NSGA-III: PENALTY vs KILL (em R-NSGA-III)` | `ed_min` | $-19.0267\%$ | $19.0000$ | $0.0211$ | $0.8100$ | Grande |
| `F3\|R-NSGA-III: PENALTY vs KILL (em R-NSGA-III)` | `spacing` | $+116.1572\%$ | $100.0000$ | $0.0002$ | $0.0000$ | Grande |
| `F2\|R-NSGA-III: ELIT_OFF vs ELIT_ON (em R-NSGA-III)` | `hv` | $+5.3245\%$ | $58.0000$ | $0.5708$ | $0.5800$ | Pequena |
| `F2\|R-NSGA-III: ELIT_OFF vs ELIT_ON (em R-NSGA-III)` | `igd_plus` | $-21.1110\%$ | $35.0000$ | $0.2730$ | $0.6500$ | Média |
| `F2\|R-NSGA-III: ELIT_OFF vs ELIT_ON (em R-NSGA-III)` | `ed_media` | $-9.7509\%$ | $24.0000$ | $0.0539$ | $0.7600$ | Grande |
| `F2\|R-NSGA-III: ELIT_OFF vs ELIT_ON (em R-NSGA-III)` | `ed_min` | $-9.3183\%$ | $35.0000$ | $0.2730$ | $0.6500$ | Média |
| `F2\|R-NSGA-III: ELIT_OFF vs ELIT_ON (em R-NSGA-III)` | `spacing` | $-19.8604\%$ | $42.0000$ | $0.5708$ | $0.5800$ | Pequena |
| `F2\|NSGA-III: ELIT_OFF vs ELIT_ON (em NSGA-III)` | `hv` | $-1.5705\%$ | $46.0000$ | $0.7913$ | $0.4600$ | Desprezível |
| `F2\|NSGA-III: ELIT_OFF vs ELIT_ON (em NSGA-III)` | `igd_plus` | $+3.0047\%$ | $52.0000$ | $0.9097$ | $0.4800$ | Desprezível |
| `F2\|NSGA-III: ELIT_OFF vs ELIT_ON (em NSGA-III)` | `ed_media` | $-1.7299\%$ | $46.0000$ | $0.7913$ | $0.5400$ | Desprezível |
| `F2\|NSGA-III: ELIT_OFF vs ELIT_ON (em NSGA-III)` | `ed_min` | $+2.4580\%$ | $57.0000$ | $0.6232$ | $0.4300$ | Pequena |
| `F2\|NSGA-III: ELIT_OFF vs ELIT_ON (em NSGA-III)` | `spacing` | $-23.7547\%$ | $38.0000$ | $0.3847$ | $0.6200$ | Pequena |
| `F1\|ELIT_OFF: R-NSGA-III vs NSGA-III (sob ELIT_OFF)` | `hv` | $+3.7487\%$ | $53.0000$ | $0.8501$ | $0.5300$ | Desprezível |
| `F1\|ELIT_OFF: R-NSGA-III vs NSGA-III (sob ELIT_OFF)` | `igd_plus` | $-20.1006\%$ | $36.0000$ | $0.3075$ | $0.6400$ | Pequena |
| `F1\|ELIT_OFF: R-NSGA-III vs NSGA-III (sob ELIT_OFF)` | `ed_media` | $-13.1504\%$ | $21.0000$ | $0.0312$ | $0.7900$ | Grande |
| `F1\|ELIT_OFF: R-NSGA-III vs NSGA-III (sob ELIT_OFF)` | `ed_min` | $-11.8051\%$ | $31.0000$ | $0.1620$ | $0.6900$ | Média |
| `F1\|ELIT_OFF: R-NSGA-III vs NSGA-III (sob ELIT_OFF)` | `spacing` | $-0.1146\%$ | $47.0000$ | $0.8501$ | $0.5300$ | Desprezível |
| `F1\|ELIT_ON: R-NSGA-III vs NSGA-III (sob ELIT_ON)` | `hv` | $-3.0431\%$ | $38.0000$ | $0.3847$ | $0.3800$ | Pequena |
| `F1\|ELIT_ON: R-NSGA-III vs NSGA-III (sob ELIT_ON)` | `igd_plus` | $+4.3240\%$ | $58.0000$ | $0.5708$ | $0.4200$ | Pequena |
| `F1\|ELIT_ON: R-NSGA-III vs NSGA-III (sob ELIT_ON)` | `ed_media` | $-5.4316\%$ | $42.0000$ | $0.5708$ | $0.5800$ | Pequena |
| `F1\|ELIT_ON: R-NSGA-III vs NSGA-III (sob ELIT_ON)` | `ed_min` | $-0.3517\%$ | $53.0000$ | $0.8501$ | $0.4700$ | Desprezível |
| `F1\|ELIT_ON: R-NSGA-III vs NSGA-III (sob ELIT_ON)` | `spacing` | $-4.9684\%$ | $45.0000$ | $0.7337$ | $0.5500$ | Desprezível |
| `F2\|PENALTY: ELIT_OFF vs ELIT_ON (sob PENALTY)` | `hv` | $+4.2105\%$ | $57.0000$ | $0.6232$ | $0.5700$ | Pequena |
| `F2\|PENALTY: ELIT_OFF vs ELIT_ON (sob PENALTY)` | `igd_plus` | $-19.1237\%$ | $36.0000$ | $0.3075$ | $0.6400$ | Pequena |
| `F2\|PENALTY: ELIT_OFF vs ELIT_ON (sob PENALTY)` | `ed_media` | $-8.6803\%$ | $30.0000$ | $0.1405$ | $0.7000$ | Média |
| `F2\|PENALTY: ELIT_OFF vs ELIT_ON (sob PENALTY)` | `ed_min` | $-7.5962\%$ | $40.0000$ | $0.4727$ | $0.6000$ | Pequena |
| `F2\|PENALTY: ELIT_OFF vs ELIT_ON (sob PENALTY)` | `spacing` | $-25.5432\%$ | $30.0000$ | $0.1405$ | $0.7000$ | Média |
| `F2\|KILL: ELIT_OFF vs ELIT_ON (sob KILL)` | `hv` | $-1.0270\%$ | $54.0000$ | $0.7913$ | $0.5400$ | Desprezível |
| `F2\|KILL: ELIT_OFF vs ELIT_ON (sob KILL)` | `igd_plus` | $-1.1378\%$ | $44.0000$ | $0.6776$ | $0.5600$ | Pequena |
| `F2\|KILL: ELIT_OFF vs ELIT_ON (sob KILL)` | `ed_media` | $-2.4549\%$ | $35.0000$ | $0.2730$ | $0.6500$ | Média |
| `F2\|KILL: ELIT_OFF vs ELIT_ON (sob KILL)` | `ed_min` | $+0.3770\%$ | $48.0000$ | $0.9097$ | $0.5200$ | Desprezível |
| `F2\|KILL: ELIT_OFF vs ELIT_ON (sob KILL)` | `spacing` | $-13.4102\%$ | $36.0000$ | $0.3075$ | $0.6400$ | Pequena |

---

## 10. Decomposição de Variância via ANOVA Fatorial $3$-Way ($2^3$)

A decomposição da Soma dos Quadrados ($\text{SS}\%$) isola a contribuição percentual exata de cada efeito principal ($F_1$, $F_2$, $F_3$), das interações duplas e da interação tripla sobre a variabilidade total observada na busca de microsserviços.

### Tabela 10.1: Decomposição Fatorial $3$-Way — Hipervolume ($\text{Total SS} = 0.834811$)
*Descrição: Demonstra que o fator $F_3$ (Manuseio de Restrições: `PENALTY` vs. `KILL`) domina completamente a variância explicada do Hipervolume, respondendo por $40.08\%$ de toda a Soma dos Quadrados ($p < 0.0001$).*

| Fonte de Variação (Fator / Interação) | Fração da Soma dos Quadrados ($\text{SS}\%$) | Estatística $F(1, 32)$ | Valor-$p$ | Significância ($\alpha = 0.05$) |
| :--- | :---: | :---: | :---: | :---: |
| `C(F1_alg)` (Algoritmo) | $0.01\%$ | $0.0060$ | $0.9387$ | Não Significativo |
| `C(F2_elit)` (Elitismo) | $0.32\%$ | $0.1854$ | $0.6697$ | Não Significativo |
| **`C(F3_rest)` (Restrição)** | **$40.08\%$** | **$23.3800$** | **$0.0000$** | **Significativo ($p < 0.0001$)** |
| `C(F1_alg):C(F2_elit)` | $1.12\%$ | $0.6514$ | $0.4256$ | Não Significativo |
| `C(F1_alg):C(F3_rest)` | $1.05\%$ | $0.6098$ | $0.4406$ | Não Significativo |
| `C(F2_elit):C(F3_rest)` | $0.73\%$ | $0.4245$ | $0.5193$ | Não Significativo |
| `C(F1_alg):C(F2_elit):C(F3_rest)` | $1.84\%$ | $1.0716$ | $0.3083$ | Não Significativo |
| **Residual (Erro Puro)** | **$54.86\%$** | — | — | — |

### Tabela 10.2: Decomposição Fatorial $3$-Way — $\text{IGD}^+$ ($\text{Total SS} = 0.111871$)
*Descrição: O manuseio de restrições (`F3_rest`) é novamente o único efeito principal estatisticamente significativo ($15.46\%$ da variância total, $F = 7.0157$, $p = 0.0124$).*

| Fonte de Variação (Fator / Interação) | Fração da Soma dos Quadrados ($\text{SS}\%$) | Estatística $F(1, 32)$ | Valor-$p$ | Significância ($\alpha = 0.05$) |
| :--- | :---: | :---: | :---: | :---: |
| `C(F1_alg)` (Algoritmo) | $1.43\%$ | $0.6491$ | $0.4264$ | Não Significativo |
| `C(F2_elit)` (Elitismo) | $1.93\%$ | $0.8750$ | $0.3566$ | Não Significativo |
| **`C(F3_rest)` (Restrição)** | **$15.46\%$** | **$7.0157$** | **$0.0124$** | **Significativo ($p \le 0.05$)** |
| `C(F1_alg):C(F2_elit)` | $3.34\%$ | $1.5153$ | $0.2273$ | Não Significativo |
| `C(F1_alg):C(F3_rest)` | $3.93\%$ | $1.7818$ | $0.1914$ | Não Significativo |
| `C(F2_elit):C(F3_rest)` | $1.45\%$ | $0.6571$ | $0.4236$ | Não Significativo |
| `C(F1_alg):C(F2_elit):C(F3_rest)` | $1.93\%$ | $0.8761$ | $0.3563$ | Não Significativo |
| **Residual (Erro Puro)** | **$70.53\%$** | — | — | — |

### Tabela 10.3: Decomposição Fatorial $3$-Way — $\text{ED}_{\text{média}}$ ($\text{Total SS} = 0.275381$)
*Descrição: Ao contrário dos indicadores de volume global, a distância média até o ponto de referência arquitetural ($\text{ED}_{\text{média}}$) é governada significativamente pela escolha do **Algoritmo** (`F1_alg`: `R-NSGA-III` vs. `NSGA-III`), que explica $13.72\%$ da variância ($F = 5.8081$, $p = 0.0219$).*

| Fonte de Variação (Fator / Interação) | Fração da Soma dos Quadrados ($\text{SS}\%$) | Estatística $F(1, 32)$ | Valor-$p$ | Significância ($\alpha = 0.05$) |
| :--- | :---: | :---: | :---: | :---: |
| **`C(F1_alg)` (Algoritmo)** | **$13.72\%$** | **$5.8081$** | **$0.0219$** | **Significativo ($p \le 0.05$)** |
| `C(F2_elit)` (Elitismo) | $4.88\%$ | $2.0676$ | $0.1602$ | Não Significativo |
| `C(F3_rest)` (Restrição) | $0.07\%$ | $0.0308$ | $0.8617$ | Não Significativo |
| `C(F1_alg):C(F2_elit)` | $2.28\%$ | $0.9675$ | $0.3327$ | Não Significativo |
| `C(F1_alg):C(F3_rest)` | $0.94\%$ | $0.3977$ | $0.5328$ | Não Significativo |
| `C(F2_elit):C(F3_rest)` | $1.60\%$ | $0.6773$ | $0.4166$ | Não Significativo |
| `C(F1_alg):C(F2_elit):C(F3_rest)` | $0.93\%$ | $0.3946$ | $0.5343$ | Não Significativo |
| **Residual (Erro Puro)** | **$75.57\%$** | — | — | — |

### Tabela 10.4: Decomposição Fatorial $3$-Way — $\text{ED}_{\text{min}}$ ($\text{Total SS} = 0.218662$)
*Descrição: A proximidade da melhor solução individual de compromisso ($\text{ED}_{\text{min}}$) depende significativamente do fator de restrição `F3_rest` ($\text{SS}\% = 16.96\%$, $F = 7.9321$, $p = 0.0082$).*

| Fonte de Variação (Fator / Interação) | Fração da Soma dos Quadrados ($\text{SS}\%$) | Estatística $F(1, 32)$ | Valor-$p$ | Significância ($\alpha = 0.05$) |
| :--- | :---: | :---: | :---: | :---: |
| `C(F1_alg)` (Algoritmo) | $3.71\%$ | $1.7335$ | $0.1973$ | Não Significativo |
| `C(F2_elit)` (Elitismo) | $1.12\%$ | $0.5216$ | $0.4754$ | Não Significativo |
| **`C(F3_rest)` (Restrição)** | **$16.96\%$** | **$7.9321$** | **$0.0082$** | **Significativo ($p \le 0.01$)** |
| `C(F1_alg):C(F2_elit)` | $3.30\%$ | $1.5431$ | $0.2232$ | Não Significativo |
| `C(F1_alg):C(F3_rest)` | $4.25\%$ | $1.9877$ | $0.1682$ | Não Significativo |
| `C(F2_elit):C(F3_rest)` | $1.39\%$ | $0.6490$ | $0.4264$ | Não Significativo |
| `C(F1_alg):C(F2_elit):C(F3_rest)` | $0.83\%$ | $0.3903$ | $0.5366$ | Não Significativo |
| **Residual (Erro Puro)** | **$68.44\%$** | — | — | — |

### Tabela 10.5: Decomposição Fatorial $3$-Way — *Spacing* ($\text{Total SS} = 0.032007$)
*Descrição: No indicador Spacing, tanto o manuseio de restrições `F3_rest` ($\text{SS}\% = 49.89\%$, $p < 0.0001$) quanto o elitismo `F2_elit` ($\text{SS}\% = 5.68\%$, $p = 0.0454$) exercem efeitos principais estatisticamente significativos.*

| Fonte de Variação (Fator / Interação) | Fração da Soma dos Quadrados ($\text{SS}\%$) | Estatística $F(1, 32)$ | Valor-$p$ | Significância ($\alpha = 0.05$) |
| :--- | :---: | :---: | :---: | :---: |
| `C(F1_alg)` (Algoritmo) | $0.08\%$ | $0.0610$ | $0.8065$ | Não Significativo |
| **`C(F2_elit)` (Elitismo)** | **$5.68\%$** | **$4.3348$** | **$0.0454$** | **Significativo ($p \le 0.05$)** |
| **`C(F3_rest)` (Restrição)** | **$49.89\%$** | **$38.0641$** | **$0.0000$** | **Significativo ($p < 0.0001$)** |
| `C(F1_alg):C(F2_elit)` | $0.07\%$ | $0.0568$ | $0.8131$ | Não Significativo |
| `C(F1_alg):C(F3_rest)` | $0.00\%$ | $0.0007$ | $0.9795$ | Não Significativo |
| `C(F2_elit):C(F3_rest)` | $2.24\%$ | $1.7053$ | $0.2009$ | Não Significativo |
| `C(F1_alg):C(F2_elit):C(F3_rest)` | $0.09\%$ | $0.0708$ | $0.7919$ | Não Significativo |
| **Residual (Erro Puro)** | **$41.94\%$** | — | — | — |

---

## 11. Auditoria de Correlações e Diagnóstico Geométrico da Fronteira ($N = 40$)

Esta seção examina a associação linear (Pearson $r$) e monotônica (Spearman $\rho$) entre os indicadores de qualidade e o número de arquiteturas na fronteira (`n_pontos`), esclarecendo o aparente paradoxo entre *Spacing* e *Hipervolume*.

### Tabela 11.1: Matriz de Correlações de Pearson ($r$) e Spearman ($\rho$) nas $N = 40$ Execuções
*Descrição: Mostra forte correlação negativa entre `hv` e `igd_plus` ($r = -0.8885$, $\rho = -0.8644$), validando a consistência entre ambos. Revela também correlação positiva altamente significativa entre `spacing` e `hv` ($r = +0.6708$, $\rho = +0.6722$), provando que fronteiras mais amplas (maior HV) apresentam maior distância absoluta entre soluções do que fronteiras colapsadas.*

| Par de Variáveis Auditadas | Correlação de Pearson ($r$) | Valor-$p$ (Pearson) | Correlação de Spearman ($\rho$) | Valor-$p$ (Spearman) | Interpretação na Auditoria |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **`spacing` vs `hv`** | $+0.6708$ | $2.1784 \times 10^{-6}$ | $+0.6722$ | $2.0311 \times 10^{-6}$ | Forte associação positiva (expansão da fronteira) |
| **`spacing` vs `igd_plus`** | $-0.4280$ | $5.8720 \times 10^{-3}$ | $-0.3966$ | $1.1283 \times 10^{-2}$ | Associação negativa moderada e significativa |
| **`spacing` vs `ed_media`** | $+0.0151$ | $9.2654 \times 10^{-1}$ | $-0.0006$ | $9.9725 \times 10^{-1}$ | Ausência de correlação (ortogonalidade) |
| **`spacing` vs `ed_min`** | $-0.4194$ | $7.0624 \times 10^{-3}$ | $-0.3319$ | $3.6417 \times 10^{-2}$ | Associação negativa moderada e significativa |
| **`spacing` vs `n_pontos`** | $-0.3425$ | $3.0487 \times 10^{-2}$ | $-0.3179$ | $4.5640 \times 10^{-2}$ | Maior densidade de pontos reduz o espaçamento |
| **`hv` vs `igd_plus`** | $-0.8885$ | $2.0067 \times 10^{-14}$ | $-0.8644$ | $6.6794 \times 10^{-13}$ | Forte concordância inversa de convergência/volume |

### Tabela 11.2: Diagnóstico Estratificado por Regime de Restrição (`PENALTY` vs. `KILL`)
*Descrição: Estratifica a relação `spacing` vs. `hv` e contabiliza a cardinalidade média da fronteira (`n_pontos`) e o número médio de soluções duplicadas (`dup`). Sob `KILL`, há maior quantidade de pontos ($121.15 \pm 10.86$) e mais duplicatas ($9.00$) confinados em uma sub-região estreita (menor HV e menor Spacing), ao passo que `PENALTY` explora uma extensão muito maior do espaço de objetivos de microsserviços.*

| Regime de Restrição ($F_3$) | $n$ | Spearman $\rho$ (`spacing` vs `hv`) | Valor-$p$ (Spearman) | Cardinalidade da Fronteira (`n_pontos` $\text{Média} \pm \text{DP}$) | Média de Duplicatas (`dup mean`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`PENALTY`** | $20$ | $+0.4617$ | $0.0405$ | $106.50 \pm 25.81$ | $7.75$ |
| **`KILL`** | $20$ | $+0.2361$ | $0.3163$ | $121.15 \pm 10.86$ | $9.00$ |