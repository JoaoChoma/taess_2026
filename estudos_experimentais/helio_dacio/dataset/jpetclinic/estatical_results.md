====================================================================
INDICADOR: HV
====================================================================

[1] SHAPIRO-WILK:
config_id                      config  n        W        p  normal
 config_1   nsgaiii__elit_on__penalty  5 0.982934 0.949680    True
 config_2  nsgaiii__elit_off__penalty  5 0.932143 0.611056    True
 config_3  rnsgaiii__elit_on__penalty  5 0.905393 0.440406    True
 config_4 rnsgaiii__elit_off__penalty  5 0.972358 0.890163    True
 config_5      nsgaiii__elit_on__kill  5 0.827916 0.134189    True
 config_6     nsgaiii__elit_off__kill  5 0.705831 0.011010   False
 config_7     rnsgaiii__elit_on__kill  5 0.899612 0.407744    True
 config_8    rnsgaiii__elit_off__kill  5 0.887791 0.346115    True

[2] LEVENE (center='median'): F/W = 2.008031, df = (7, 32), p = 0.084845 -> Homocedástico? True

[3] TESTE GLOBAL:
  Decisão pelo fluxo formal (normalidade_ok=False & levene_ok=True): Kruskal-Wallis
  ANOVA One-Way : F(7, 32) = 3.761244, p = 0.004401 (4.4010e-03)
  Kruskal-Wallis: H(7)     = 17.871220, p = 0.012565 (1.2565e-02)

[4] TOP 12 PARES PÓS-HOC (ordenados por p_dunn_bh):
              par_id                                             comparacao     diff  p_tukey  p_tukey_bh        z  p_dunn_raw  p_dunn_bh      A12 magnitude
config_4 vs config_8 rnsgaiii__elit_off__penalty - rnsgaiii__elit_off__kill 0.276281 0.018387    0.396058 3.164860    0.001552   0.043444 1.000000    Grande
config_4 vs config_7  rnsgaiii__elit_off__penalty - rnsgaiii__elit_on__kill 0.259290 0.032036    0.396058 2.921410    0.003485   0.048783 1.000000    Grande
config_4 vs config_5   rnsgaiii__elit_off__penalty - nsgaiii__elit_on__kill 0.241311 0.056118    0.396058 2.515658    0.011881   0.083167 1.000000    Grande
config_1 vs config_8   nsgaiii__elit_on__penalty - rnsgaiii__elit_off__kill 0.202867 0.165334    0.925868 2.596809    0.009409   0.083167 1.000000    Grande
config_1 vs config_7    nsgaiii__elit_on__penalty - rnsgaiii__elit_on__kill 0.185876 0.250015    1.000000 2.353358    0.018605   0.104186 0.960000    Grande
config_4 vs config_6  rnsgaiii__elit_off__penalty - nsgaiii__elit_off__kill 0.241041 0.056580    0.396058 2.136957    0.032601   0.152140 1.000000    Grande
config_1 vs config_5     nsgaiii__elit_on__penalty - nsgaiii__elit_on__kill 0.167897 0.367679    1.000000 1.947606    0.051462   0.204017 0.920000    Grande
config_2 vs config_8  nsgaiii__elit_off__penalty - rnsgaiii__elit_off__kill 0.174110 0.323889    1.000000 1.893506    0.058291   0.204017 0.840000    Grande
config_3 vs config_8  rnsgaiii__elit_on__penalty - rnsgaiii__elit_off__kill 0.165646 0.384290    1.000000 1.785306    0.074212   0.230881 0.760000    Grande
config_2 vs config_7   nsgaiii__elit_off__penalty - rnsgaiii__elit_on__kill 0.157119 0.450338    1.000000 1.650055    0.098932   0.277008 0.800000    Grande
config_1 vs config_6    nsgaiii__elit_on__penalty - nsgaiii__elit_off__kill 0.167627 0.369653    1.000000 1.568905    0.116670   0.287254 0.880000    Grande
config_3 vs config_7   rnsgaiii__elit_on__penalty - rnsgaiii__elit_on__kill 0.148656 0.519661    1.000000 1.541855    0.123109   0.287254 0.680000     Média
  Pares com p_tukey <= 0.05: 2 | p_tukey_bh <= 0.05: 0 | p_dunn_raw <= 0.05: 6 | p_dunn_bh <= 0.05: 2

[5] MATRIZ 8x8 A12 (hv):
          config_1  config_2  config_3  config_4  config_5  config_6  config_7  config_8
config_1      0.50      0.60      0.56      0.32      0.92      0.88      0.96      1.00
config_2      0.40      0.50      0.52      0.28      0.68      0.68      0.80      0.84
config_3      0.44      0.48      0.50      0.32      0.68      0.68      0.68      0.76
config_4      0.68      0.72      0.68      0.50      1.00      1.00      1.00      1.00
config_5      0.08      0.32      0.32      0.00      0.50      0.36      0.64      0.64
config_6      0.12      0.32      0.32      0.00      0.64      0.50      0.76      0.76
config_7      0.04      0.20      0.32      0.00      0.36      0.24      0.50      0.60
config_8      0.00      0.16      0.24      0.00      0.36      0.24      0.40      0.50

  Contagem de Magnitudes A12 (28 pares):
magnitude
Grande         14
Média           7
Pequena         6
Desprezível     1
====================================================================
INDICADOR: IGD_PLUS
====================================================================

[1] SHAPIRO-WILK:
config_id                      config  n        W        p  normal
 config_1   nsgaiii__elit_on__penalty  5 0.887604 0.345199    True
 config_2  nsgaiii__elit_off__penalty  5 0.929182 0.590801    True
 config_3  rnsgaiii__elit_on__penalty  5 0.929431 0.592496    True
 config_4 rnsgaiii__elit_off__penalty  5 0.946800 0.714323    True
 config_5      nsgaiii__elit_on__kill  5 0.953352 0.761096    True
 config_6     nsgaiii__elit_off__kill  5 0.699060 0.009362   False
 config_7     rnsgaiii__elit_on__kill  5 0.922644 0.547136    True
 config_8    rnsgaiii__elit_off__kill  5 0.890635 0.360308    True

[2] LEVENE (center='median'): F/W = 1.052203, df = (7, 32), p = 0.415825 -> Homocedástico? True

[3] TESTE GLOBAL:
  Decisão pelo fluxo formal (normalidade_ok=False & levene_ok=True): Kruskal-Wallis
  ANOVA One-Way : F(7, 32) = 1.910014, p = 0.100552 (1.0055e-01)
  Kruskal-Wallis: H(7)     = 11.206829, p = 0.129848 (1.2985e-01)

[4] TOP 12 PARES PÓS-HOC (ordenados por p_dunn_bh):
              par_id                                               comparacao      diff  p_tukey  p_tukey_bh         z  p_dunn_raw  p_dunn_bh      A12 magnitude
config_4 vs config_7    rnsgaiii__elit_off__penalty - rnsgaiii__elit_on__kill -0.096571 0.072659    1.000000 -2.921410    0.003485   0.097566 1.000000    Grande
config_4 vs config_8   rnsgaiii__elit_off__penalty - rnsgaiii__elit_off__kill -0.089979 0.114213    1.000000 -2.677959    0.007407   0.103701 0.960000    Grande
config_4 vs config_5     rnsgaiii__elit_off__penalty - nsgaiii__elit_on__kill -0.083629 0.171281    1.000000 -2.326308    0.020002   0.186687 0.960000    Grande
config_4 vs config_6    rnsgaiii__elit_off__penalty - nsgaiii__elit_off__kill -0.086302 0.144990    1.000000 -2.082857    0.037264   0.260850 0.920000    Grande
config_2 vs config_4 nsgaiii__elit_off__penalty - rnsgaiii__elit_off__penalty  0.067639 0.404611    1.000000  1.920556    0.054788   0.306811 0.160000    Grande
config_3 vs config_4 rnsgaiii__elit_on__penalty - rnsgaiii__elit_off__penalty  0.061445 0.524844    1.000000  1.758256    0.078704   0.367285 0.240000    Grande
config_1 vs config_4  nsgaiii__elit_on__penalty - rnsgaiii__elit_off__penalty  0.061029 0.533233    1.000000  1.568905    0.116670   0.466680 0.120000    Grande
config_1 vs config_7      nsgaiii__elit_on__penalty - rnsgaiii__elit_on__kill -0.035542 0.944670    1.000000 -1.352504    0.176214   0.616749 0.760000    Grande
config_1 vs config_8     nsgaiii__elit_on__penalty - rnsgaiii__elit_off__kill -0.028950 0.981589    1.000000 -1.109054    0.267407   0.748740 0.720000    Grande
config_3 vs config_7     rnsgaiii__elit_on__penalty - rnsgaiii__elit_on__kill -0.035126 0.947879    1.000000 -1.163154    0.244767   0.748740 0.680000     Média
config_2 vs config_7     nsgaiii__elit_off__penalty - rnsgaiii__elit_on__kill -0.028932 0.981653    1.000000 -1.000853    0.316898   0.806649 0.640000   Pequena
config_3 vs config_8    rnsgaiii__elit_on__penalty - rnsgaiii__elit_off__kill -0.028534 0.983037    1.000000 -0.919703    0.357728   0.834699 0.680000     Média
  Pares com p_tukey <= 0.05: 0 | p_tukey_bh <= 0.05: 0 | p_dunn_raw <= 0.05: 4 | p_dunn_bh <= 0.05: 0

[5] MATRIZ 8x8 A12 (igd_plus):
          config_1  config_2  config_3  config_4  config_5  config_6  config_7  config_8
config_1      0.50      0.56      0.48      0.12      0.68      0.68      0.76      0.72
config_2      0.44      0.50      0.48      0.16      0.60      0.60      0.64      0.56
config_3      0.52      0.52      0.50      0.24      0.56      0.52      0.68      0.68
config_4      0.88      0.84      0.76      0.50      0.96      0.92      1.00      0.96
config_5      0.32      0.40      0.44      0.04      0.50      0.44      0.64      0.60
config_6      0.32      0.40      0.48      0.08      0.56      0.50      0.76      0.64
config_7      0.24      0.36      0.32      0.00      0.36      0.24      0.50      0.48
config_8      0.28      0.44      0.32      0.04      0.40      0.36      0.52      0.50

  Contagem de Magnitudes A12 (28 pares):
magnitude
Grande         10
Pequena         9
Desprezível     5
Média           4
====================================================================
INDICADOR: ED_MEDIA
====================================================================

[1] SHAPIRO-WILK:
config_id                      config  n        W        p  normal
 config_1   nsgaiii__elit_on__penalty  5 0.890547 0.359860    True
 config_2  nsgaiii__elit_off__penalty  5 0.926770 0.574513    True
 config_3  rnsgaiii__elit_on__penalty  5 0.964059 0.835927    True
 config_4 rnsgaiii__elit_off__penalty  5 0.895540 0.385726    True
 config_5      nsgaiii__elit_on__kill  5 0.929160 0.590654    True
 config_6     nsgaiii__elit_off__kill  5 0.893535 0.375189    True
 config_7     rnsgaiii__elit_on__kill  5 0.721300 0.015789   False
 config_8    rnsgaiii__elit_off__kill  5 0.804749 0.088538    True

[2] LEVENE (center='median'): F/W = 0.682403, df = (7, 32), p = 0.685762 -> Homocedástico? True

[3] TESTE GLOBAL:
  Decisão pelo fluxo formal (normalidade_ok=False & levene_ok=True): Kruskal-Wallis
  ANOVA One-Way : F(7, 32) = 1.477671, p = 0.210447 (2.1045e-01)
  Kruskal-Wallis: H(7)     = 10.428293, p = 0.165573 (1.6557e-01)

[4] TOP 12 PARES PÓS-HOC (ordenados por p_dunn_bh):
              par_id                                               comparacao      diff  p_tukey  p_tukey_bh         z  p_dunn_raw  p_dunn_bh      A12 magnitude
config_1 vs config_4  nsgaiii__elit_on__penalty - rnsgaiii__elit_off__penalty  0.135200 0.175309    1.000000  2.461558    0.013833   0.186687 0.000000    Grande
config_4 vs config_5     rnsgaiii__elit_off__penalty - nsgaiii__elit_on__kill -0.109670 0.406639    1.000000 -2.434508    0.014912   0.186687 1.000000    Grande
config_2 vs config_4 nsgaiii__elit_off__penalty - rnsgaiii__elit_off__penalty  0.118646 0.311139    1.000000  2.326308    0.020002   0.186687 0.200000    Grande
config_3 vs config_4 rnsgaiii__elit_on__penalty - rnsgaiii__elit_off__penalty  0.098762 0.537609    1.000000  2.028757    0.042483   0.237905 0.120000    Grande
config_4 vs config_6    rnsgaiii__elit_off__penalty - nsgaiii__elit_off__kill -0.103053 0.484723    1.000000 -2.028757    0.042483   0.237905 0.920000    Grande
config_4 vs config_7    rnsgaiii__elit_off__penalty - rnsgaiii__elit_on__kill -0.073357 0.832703    1.000000 -1.758256    0.078704   0.367285 0.800000    Grande
config_5 vs config_8        nsgaiii__elit_on__kill - rnsgaiii__elit_off__kill  0.061058 0.926883    1.000000  1.514805    0.129822   0.454376 0.200000    Grande
config_1 vs config_8     nsgaiii__elit_on__penalty - rnsgaiii__elit_off__kill  0.086588 0.688600    1.000000  1.541855    0.123109   0.454376 0.200000    Grande
config_2 vs config_8    nsgaiii__elit_off__penalty - rnsgaiii__elit_off__kill  0.070035 0.862500    1.000000  1.406605    0.159545   0.496361 0.320000     Média
config_3 vs config_8    rnsgaiii__elit_on__penalty - rnsgaiii__elit_off__kill  0.050150 0.973641    1.000000  1.109054    0.267407   0.680672 0.280000    Grande
config_6 vs config_8       nsgaiii__elit_off__kill - rnsgaiii__elit_off__kill  0.054441 0.959066    1.000000  1.109054    0.267407   0.680672 0.240000    Grande
config_4 vs config_8   rnsgaiii__elit_off__penalty - rnsgaiii__elit_off__kill -0.048612 0.977805    1.000000 -0.919703    0.357728   0.834699 0.680000     Média
  Pares com p_tukey <= 0.05: 0 | p_tukey_bh <= 0.05: 0 | p_dunn_raw <= 0.05: 5 | p_dunn_bh <= 0.05: 0

[5] MATRIZ 8x8 A12 (ed_media):
          config_1  config_2  config_3  config_4  config_5  config_6  config_7  config_8
config_1      0.50      0.48      0.44      0.00      0.48      0.44      0.40      0.20
config_2      0.52      0.50      0.40      0.20      0.44      0.44      0.32      0.32
config_3      0.56      0.60      0.50      0.12      0.56      0.52      0.44      0.28
config_4      1.00      0.80      0.88      0.50      1.00      0.92      0.80      0.68
config_5      0.52      0.56      0.44      0.00      0.50      0.36      0.40      0.20
config_6      0.56      0.56      0.48      0.08      0.64      0.50      0.52      0.24
config_7      0.60      0.68      0.56      0.20      0.60      0.48      0.50      0.36
config_8      0.80      0.68      0.72      0.32      0.80      0.76      0.64      0.50

  Contagem de Magnitudes A12 (28 pares):
magnitude
Grande         10
Desprezível     9
Pequena         6
Média           3
====================================================================
INDICADOR: ED_MIN
====================================================================

[1] SHAPIRO-WILK:
config_id                      config  n        W        p  normal
 config_1   nsgaiii__elit_on__penalty  5 0.924504 0.559399    True
 config_2  nsgaiii__elit_off__penalty  5 0.935770 0.636211    True
 config_3  rnsgaiii__elit_on__penalty  5 0.920964 0.536178    True
 config_4 rnsgaiii__elit_off__penalty  5 0.883725 0.326534    True
 config_5      nsgaiii__elit_on__kill  5 0.989382 0.977486    True
 config_6     nsgaiii__elit_off__kill  5 0.812871 0.102747    True
 config_7     rnsgaiii__elit_on__kill  5 0.931409 0.606012    True
 config_8    rnsgaiii__elit_off__kill  5 0.941673 0.677790    True

[2] LEVENE (center='median'): F/W = 0.696013, df = (7, 32), p = 0.674921 -> Homocedástico? True

[3] TESTE GLOBAL:
  Decisão pelo fluxo formal (normalidade_ok=True & levene_ok=True): ANOVA One-Way
  ANOVA One-Way : F(7, 32) = 2.108188, p = 0.071307 (7.1307e-02)
  Kruskal-Wallis: H(7)     = 9.921951, p = 0.193040 (1.9304e-01)

[4] TOP 12 PARES PÓS-HOC (ordenados por p_tukey_bh):
              par_id                                             comparacao      diff  p_tukey  p_tukey_bh         z  p_dunn_raw  p_dunn_bh      A12 magnitude
config_4 vs config_7  rnsgaiii__elit_off__penalty - rnsgaiii__elit_on__kill -0.133875 0.069432    0.982762 -2.677959    0.007407   0.200576 0.960000    Grande
config_4 vs config_6  rnsgaiii__elit_off__penalty - nsgaiii__elit_off__kill -0.133663 0.070197    0.982762 -2.299258    0.021490   0.200576 0.960000    Grande
config_1 vs config_2 nsgaiii__elit_on__penalty - nsgaiii__elit_off__penalty -0.007333 1.000000    1.000000 -0.486902    0.626328   0.923010 0.600000   Pequena
config_6 vs config_7      nsgaiii__elit_off__kill - rnsgaiii__elit_on__kill -0.000212 1.000000    1.000000 -0.378701    0.704910   0.938075 0.600000   Pequena
config_5 vs config_8      nsgaiii__elit_on__kill - rnsgaiii__elit_off__kill -0.003820 1.000000    1.000000 -0.243451    0.807656   0.938075 0.560000   Pequena
config_5 vs config_7       nsgaiii__elit_on__kill - rnsgaiii__elit_on__kill -0.015370 0.999957    1.000000 -0.541002    0.588506   0.915454 0.600000   Pequena
config_5 vs config_6       nsgaiii__elit_on__kill - nsgaiii__elit_off__kill -0.015158 0.999961    1.000000 -0.162301    0.871069   0.938075 0.560000   Pequena
config_4 vs config_8 rnsgaiii__elit_off__penalty - rnsgaiii__elit_off__kill -0.122325 0.123242    1.000000 -2.380408    0.017293   0.200576 0.920000    Grande
config_4 vs config_5   rnsgaiii__elit_off__penalty - nsgaiii__elit_on__kill -0.118506 0.147318    1.000000 -2.136957    0.032601   0.208680 0.920000    Grande
config_3 vs config_8  rnsgaiii__elit_on__penalty - rnsgaiii__elit_off__kill -0.048913 0.944869    1.000000 -0.946753    0.343765   0.915454 0.680000     Média
config_3 vs config_7   rnsgaiii__elit_on__penalty - rnsgaiii__elit_on__kill -0.060463 0.851502    1.000000 -1.244304    0.213388   0.746857 0.680000     Média
config_3 vs config_6   rnsgaiii__elit_on__penalty - nsgaiii__elit_off__kill -0.060251 0.853709    1.000000 -0.865603    0.386708   0.915454 0.640000   Pequena
  Pares com p_tukey <= 0.05: 0 | p_tukey_bh <= 0.05: 0 | p_dunn_raw <= 0.05: 5 | p_dunn_bh <= 0.05: 0

[5] MATRIZ 8x8 A12 (ed_min):
          config_1  config_2  config_3  config_4  config_5  config_6  config_7  config_8
config_1      0.50      0.60      0.40      0.12      0.64      0.64      0.72      0.72
config_2      0.40      0.50      0.40      0.16      0.52      0.52      0.60      0.52
config_3      0.60      0.60      0.50      0.28      0.60      0.64      0.68      0.68
config_4      0.88      0.84      0.72      0.50      0.92      0.96      0.96      0.92
config_5      0.36      0.48      0.40      0.08      0.50      0.56      0.60      0.56
config_6      0.36      0.48      0.36      0.04      0.44      0.50      0.60      0.52
config_7      0.28      0.40      0.32      0.04      0.40      0.40      0.50      0.40
config_8      0.28      0.48      0.32      0.08      0.44      0.48      0.60      0.50

  Contagem de Magnitudes A12 (28 pares):
magnitude
Pequena        13
Grande          9
Desprezível     4
Média           2
====================================================================
INDICADOR: SPACING
====================================================================

[1] SHAPIRO-WILK:
config_id                      config  n        W        p  normal
 config_1   nsgaiii__elit_on__penalty  5 0.965795 0.847639    True
 config_2  nsgaiii__elit_off__penalty  5 0.927275 0.577907    True
 config_3  rnsgaiii__elit_on__penalty  5 0.814189 0.105226    True
 config_4 rnsgaiii__elit_off__penalty  5 0.879121 0.305348    True
 config_5      nsgaiii__elit_on__kill  5 0.880337 0.310843    True
 config_6     nsgaiii__elit_off__kill  5 0.906941 0.449428    True
 config_7     rnsgaiii__elit_on__kill  5 0.907225 0.451093    True
 config_8    rnsgaiii__elit_off__kill  5 0.966991 0.855616    True

[2] LEVENE (center='median'): F/W = 1.712770, df = (7, 32), p = 0.141260 -> Homocedástico? True

[3] TESTE GLOBAL:
  Decisão pelo fluxo formal (normalidade_ok=True & levene_ok=True): ANOVA One-Way
  ANOVA One-Way : F(7, 32) = 6.327625, p = 0.000105 (1.0455e-04)
  Kruskal-Wallis: H(7)     = 29.505366, p = 0.000117 (1.1699e-04)

[4] TOP 12 PARES PÓS-HOC (ordenados por p_tukey_bh):
              par_id                                             comparacao     diff  p_tukey  p_tukey_bh        z  p_dunn_raw  p_dunn_bh      A12 magnitude
config_3 vs config_8  rnsgaiii__elit_on__penalty - rnsgaiii__elit_off__kill 0.051735 0.007594    0.049099 3.164860    0.001552   0.014481 0.000000    Grande
config_1 vs config_5     nsgaiii__elit_on__penalty - nsgaiii__elit_on__kill 0.050309 0.010135    0.049099 2.786159    0.005334   0.021335 0.000000    Grande
config_1 vs config_6    nsgaiii__elit_on__penalty - nsgaiii__elit_off__kill 0.055157 0.003742    0.049099 3.164860    0.001552   0.014481 0.000000    Grande
config_1 vs config_7    nsgaiii__elit_on__penalty - rnsgaiii__elit_on__kill 0.051562 0.007865    0.049099 3.029610    0.002449   0.017141 0.000000    Grande
config_1 vs config_8   nsgaiii__elit_on__penalty - rnsgaiii__elit_off__kill 0.056769 0.002666    0.049099 3.516512    0.000437   0.012243 0.000000    Grande
config_3 vs config_6   rnsgaiii__elit_on__penalty - nsgaiii__elit_off__kill 0.050123 0.010521    0.049099 2.813209    0.004905   0.021335 0.000000    Grande
config_3 vs config_7   rnsgaiii__elit_on__penalty - rnsgaiii__elit_on__kill 0.046528 0.021357    0.085428 2.677959    0.007407   0.023045 0.000000    Grande
config_3 vs config_5    rnsgaiii__elit_on__penalty - nsgaiii__elit_on__kill 0.045275 0.027132    0.094963 2.434508    0.014912   0.037958 0.000000    Grande
config_4 vs config_8 rnsgaiii__elit_off__penalty - rnsgaiii__elit_off__kill 0.033059 0.210899    0.656131 2.786159    0.005334   0.021335 0.000000    Grande
config_4 vs config_6  rnsgaiii__elit_off__penalty - nsgaiii__elit_off__kill 0.031447 0.262861    0.669101 2.434508    0.014912   0.037958 0.000000    Grande
config_2 vs config_8  nsgaiii__elit_off__penalty - rnsgaiii__elit_off__kill 0.031558 0.259039    0.669101 2.705009    0.006830   0.023045 0.000000    Grande
config_2 vs config_6   nsgaiii__elit_off__penalty - nsgaiii__elit_off__kill 0.029947 0.318444    0.743036 2.353358    0.018605   0.043411 0.000000    Grande
  Pares com p_tukey <= 0.05: 8 | p_tukey_bh <= 0.05: 6 | p_dunn_raw <= 0.05: 16 | p_dunn_bh <= 0.05: 13

[5] MATRIZ 8x8 A12 (spacing):
          config_1  config_2  config_3  config_4  config_5  config_6  config_7  config_8
config_1      0.50      0.20      0.40      0.24      0.00      0.00      0.00      0.00
config_2      0.80      0.50      0.60      0.48      0.08      0.00      0.08      0.00
config_3      0.60      0.40      0.50      0.36      0.00      0.00      0.00      0.00
config_4      0.76      0.52      0.64      0.50      0.00      0.00      0.00      0.00
config_5      1.00      0.92      1.00      1.00      0.50      0.40      0.40      0.24
config_6      1.00      1.00      1.00      1.00      0.60      0.50      0.52      0.40
config_7      1.00      0.92      1.00      1.00      0.60      0.48      0.50      0.32
config_8      1.00      1.00      1.00      1.00      0.76      0.60      0.68      0.50

  Contagem de Magnitudes A12 (28 pares):
magnitude
Grande         19
Pequena         6
Desprezível     2
Média           1

=============== HV — TODOS OS PARES GRANDE E MÉDIA ================
                 par      A12 magnitude    z_dunn   p_dunn  p_dunn_bh      diff  p_tukey  p_tukey_bh
config_4 vs config_8 1.000000    Grande  3.164860 0.001552   0.043444  0.276281 0.018387    0.396058
config_4 vs config_7 1.000000    Grande  2.921410 0.003485   0.048783  0.259290 0.032036    0.396058
config_1 vs config_8 1.000000    Grande  2.596809 0.009409   0.083167  0.202867 0.165334    0.925868
config_4 vs config_5 1.000000    Grande  2.515658 0.011881   0.083167  0.241311 0.056118    0.396058
config_4 vs config_6 1.000000    Grande  2.136957 0.032601   0.152140  0.241041 0.056580    0.396058
config_1 vs config_7 0.960000    Grande  2.353358 0.018605   0.104186  0.185876 0.250015    1.000000
config_1 vs config_5 0.920000    Grande  1.947606 0.051462   0.204017  0.167897 0.367679    1.000000
config_1 vs config_6 0.880000    Grande  1.568905 0.116670   0.287254  0.167627 0.369653    1.000000
config_2 vs config_8 0.840000    Grande  1.893506 0.058291   0.204017  0.174110 0.323889    1.000000
config_2 vs config_7 0.800000    Grande  1.650055 0.098932   0.277008  0.157119 0.450338    1.000000
config_3 vs config_8 0.760000    Grande  1.785306 0.074212   0.230881  0.165646 0.384290    1.000000
config_6 vs config_8 0.760000    Grande  1.027903 0.303995   0.500698  0.035240 0.999738    1.000000
config_6 vs config_7 0.760000    Grande  0.784453 0.432775   0.598412  0.018249 0.999997    1.000000
config_2 vs config_4 0.280000    Grande -1.271354 0.203603   0.398324 -0.102171 0.872187    1.000000
config_3 vs config_7 0.680000     Média  1.541855 0.123109   0.287254  0.148656 0.519661    1.000000
config_2 vs config_5 0.680000     Média  1.244304 0.213388   0.398324  0.139140 0.599759    1.000000
config_3 vs config_5 0.680000     Média  1.136104 0.255913   0.447848  0.130677 0.670427    1.000000
config_2 vs config_6 0.680000     Média  0.865603 0.386708   0.598412  0.138870 0.602039    1.000000
config_3 vs config_6 0.680000     Média  0.757402 0.448809   0.598412  0.130407 0.672646    1.000000
config_3 vs config_4 0.320000     Média -1.379555 0.167724   0.361251 -0.110634 0.821007    1.000000
config_1 vs config_4 0.320000     Média -0.568052 0.570000   0.665000 -0.073414 0.975499    1.000000

================ IGD_PLUS — TODOS OS PARES GRANDE E MÉDIA ================
                 par      A12 magnitude    z_dunn   p_dunn  p_dunn_bh      diff  p_tukey  p_tukey_bh
config_4 vs config_7 1.000000    Grande -2.921410 0.003485   0.097566 -0.096571 0.072659    1.000000
config_4 vs config_8 0.960000    Grande -2.677959 0.007407   0.103701 -0.089979 0.114213    1.000000
config_4 vs config_5 0.960000    Grande -2.326308 0.020002   0.186687 -0.083629 0.171281    1.000000
config_4 vs config_6 0.920000    Grande -2.082857 0.037264   0.260850 -0.086302 0.144990    1.000000
config_1 vs config_4 0.120000    Grande  1.568905 0.116670   0.466680  0.061029 0.533233    1.000000
config_2 vs config_4 0.160000    Grande  1.920556 0.054788   0.306811  0.067639 0.404611    1.000000
config_3 vs config_4 0.240000    Grande  1.758256 0.078704   0.367285  0.061445 0.524844    1.000000
config_1 vs config_7 0.760000    Grande -1.352504 0.176214   0.616749 -0.035542 0.944670    1.000000
config_6 vs config_7 0.760000    Grande -0.838553 0.401720   0.837776 -0.010269 0.999976    1.000000
config_1 vs config_8 0.720000    Grande -1.109054 0.267407   0.748740 -0.028950 0.981589    1.000000
config_3 vs config_7 0.680000     Média -1.163154 0.244767   0.748740 -0.035126 0.947879    1.000000
config_3 vs config_8 0.680000     Média -0.919703 0.357728   0.834699 -0.028534 0.983037    1.000000
config_1 vs config_5 0.680000     Média -0.757402 0.448809   0.837776 -0.022600 0.995736    1.000000
config_1 vs config_6 0.680000     Média -0.513952 0.607286   0.871069 -0.025273 0.991623    1.000000

================ ED_MEDIA — TODOS OS PARES GRANDE E MÉDIA ================
                 par      A12 magnitude    z_dunn   p_dunn  p_dunn_bh      diff  p_tukey  p_tukey_bh
config_1 vs config_4 0.000000    Grande  2.461558 0.013833   0.186687  0.135200 0.175309    1.000000
config_4 vs config_5 1.000000    Grande -2.434508 0.014912   0.186687 -0.109670 0.406639    1.000000
config_4 vs config_6 0.920000    Grande -2.028757 0.042483   0.237905 -0.103053 0.484723    1.000000
config_3 vs config_4 0.120000    Grande  2.028757 0.042483   0.237905  0.098762 0.537609    1.000000
config_4 vs config_7 0.800000    Grande -1.758256 0.078704   0.367285 -0.073357 0.832703    1.000000
config_2 vs config_4 0.200000    Grande  2.326308 0.020002   0.186687  0.118646 0.311139    1.000000
config_1 vs config_8 0.200000    Grande  1.541855 0.123109   0.454376  0.086588 0.688600    1.000000
config_5 vs config_8 0.200000    Grande  1.514805 0.129822   0.454376  0.061058 0.926883    1.000000
config_6 vs config_8 0.240000    Grande  1.109054 0.267407   0.680672  0.054441 0.959066    1.000000
config_3 vs config_8 0.280000    Grande  1.109054 0.267407   0.680672  0.050150 0.973641    1.000000
config_4 vs config_8 0.680000     Média -0.919703 0.357728   0.834699 -0.048612 0.977805    1.000000
config_2 vs config_8 0.320000     Média  1.406605 0.159545   0.496361  0.070035 0.862500    1.000000
config_2 vs config_7 0.320000     Média  0.568052 0.570000   0.917904  0.045289 0.985118    1.000000

================ ED_MIN — TODOS OS PARES GRANDE E MÉDIA ================
                 par      A12 magnitude    z_dunn   p_dunn  p_dunn_bh      diff  p_tukey  p_tukey_bh
config_4 vs config_6 0.960000    Grande -2.299258 0.021490   0.200576 -0.133663 0.070197    0.982762
config_4 vs config_7 0.960000    Grande -2.677959 0.007407   0.200576 -0.133875 0.069432    0.982762
config_4 vs config_8 0.920000    Grande -2.380408 0.017293   0.200576 -0.122325 0.123242    1.000000
config_4 vs config_5 0.920000    Grande -2.136957 0.032601   0.208680 -0.118506 0.147318    1.000000
config_1 vs config_4 0.120000    Grande  1.595955 0.110499   0.515661  0.092001 0.420124    1.000000
config_2 vs config_4 0.160000    Grande  2.082857 0.037264   0.208680  0.099334 0.326165    1.000000
config_3 vs config_4 0.280000    Grande  1.433655 0.151671   0.606683  0.073413 0.688777    1.000000
config_1 vs config_7 0.720000    Grande -1.082004 0.279251   0.868781 -0.041875 0.975789    1.000000
config_1 vs config_8 0.720000    Grande -0.784453 0.432775   0.915454 -0.030325 0.996367    1.000000
config_3 vs config_7 0.680000     Média -1.244304 0.213388   0.746857 -0.060463 0.851502    1.000000
config_3 vs config_8 0.680000     Média -0.946753 0.343765   0.915454 -0.048913 0.944869    1.000000

================ SPACING — TODOS OS PARES GRANDE E MÉDIA ================
                 par      A12 magnitude   z_dunn   p_dunn  p_dunn_bh     diff  p_tukey  p_tukey_bh
config_1 vs config_8 0.000000    Grande 3.516512 0.000437   0.012243 0.056769 0.002666    0.049099
config_1 vs config_6 0.000000    Grande 3.164860 0.001552   0.014481 0.055157 0.003742    0.049099
config_3 vs config_8 0.000000    Grande 3.164860 0.001552   0.014481 0.051735 0.007594    0.049099
config_1 vs config_7 0.000000    Grande 3.029610 0.002449   0.017141 0.051562 0.007865    0.049099
config_1 vs config_5 0.000000    Grande 2.786159 0.005334   0.021335 0.050309 0.010135    0.049099
config_3 vs config_6 0.000000    Grande 2.813209 0.004905   0.021335 0.050123 0.010521    0.049099
config_4 vs config_8 0.000000    Grande 2.786159 0.005334   0.021335 0.033059 0.210899    0.656131
config_2 vs config_8 0.000000    Grande 2.705009 0.006830   0.023045 0.031558 0.259039    0.669101
config_3 vs config_7 0.000000    Grande 2.677959 0.007407   0.023045 0.046528 0.021357    0.085428
config_3 vs config_5 0.000000    Grande 2.434508 0.014912   0.037958 0.045275 0.027132    0.094963
config_4 vs config_6 0.000000    Grande 2.434508 0.014912   0.037958 0.031447 0.262861    0.669101
config_2 vs config_6 0.000000    Grande 2.353358 0.018605   0.043411 0.029947 0.318444    0.743036
config_4 vs config_7 0.000000    Grande 2.299258 0.021490   0.046287 0.027852 0.406729    0.876031
config_4 vs config_5 0.000000    Grande 2.055807 0.039801   0.074295 0.026599 0.464465    0.884268
config_2 vs config_7 0.080000    Grande 2.218107 0.026548   0.053095 0.026352 0.476223    0.884268
config_2 vs config_5 0.080000    Grande 1.974656 0.048307   0.084537 0.025099 0.536877    0.884268
config_1 vs config_2 0.200000    Grande 0.811503 0.417077   0.685521 0.025211 0.531398    0.884268
config_1 vs config_4 0.240000    Grande 0.730352 0.465175   0.685521 0.023710 0.605268    0.941527
config_5 vs config_8 0.240000    Grande 0.730352 0.465175   0.685521 0.006459 0.999589    1.000000
config_7 vs config_8 0.320000     Média 0.486902 0.626328   0.812112 0.005206 0.999902    1.000000



hv        : unique = 40/40, T = 0, sigma2 = 136.666667
igd_plus  : unique = 40/40, T = 0, sigma2 = 136.666667
ed_media  : unique = 40/40, T = 0, sigma2 = 136.666667
ed_min    : unique = 40/40, T = 0, sigma2 = 136.666667
spacing   : unique = 40/40, T = 0, sigma2 = 136.666667

config_id                      config  Rbar_hv  Rbar_igd_plus  Rbar_ed_media  Rbar_ed_min  Rbar_spacing
 config_1   nsgaiii__elit_on__penalty    29.20          18.00          25.80        18.80         33.80
 config_2  nsgaiii__elit_off__penalty    24.00          20.60          24.80        22.40         27.80
 config_3  rnsgaiii__elit_on__penalty    23.20          19.40          22.60        17.60         31.20
 config_4 rnsgaiii__elit_off__penalty    33.40           6.40           7.60         7.00         28.40
 config_5      nsgaiii__elit_on__kill    14.80          23.60          25.60        22.80         13.20
 config_6     nsgaiii__elit_off__kill    17.60          21.80          22.60        24.00         10.40
 config_7     rnsgaiii__elit_on__kill    11.80          28.00          20.60        26.80         11.40
 config_8    rnsgaiii__elit_off__kill    10.00          26.20          14.40        24.60          7.80


=== INTERAÇÃO 2x2: F1xF3 (Alg × Rest) (n=10 por célula) ===
hv       | NSGA-III × PENALTY: 0.9765±0.1438 (med 0.9599, IQR 0.1815) | NSGA-III × KILL: 0.8231±0.0817 (med 0.8576, IQR 0.0426) | R-NSGA-III × PENALTY: 1.0090±0.1576 (med 1.0242, IQR 0.1766) | R-NSGA-III × KILL: 0.7965±0.0492 (med 0.7867, IQR 0.0886)
igd_plus | NSGA-III × PENALTY: 0.1465±0.0485 (med 0.1380, IQR 0.0653) | NSGA-III × KILL: 0.1671±0.0440 (med 0.1510, IQR 0.0245) | R-NSGA-III × PENALTY: 0.1129±0.0700 (med 0.0916, IQR 0.0886) | R-NSGA-III × KILL: 0.1754±0.0257 (med 0.1863, IQR 0.0323)
ed_media | NSGA-III × PENALTY: 0.6742±0.1047 (med 0.6598, IQR 0.1431) | NSGA-III × KILL: 0.6536±0.0644 (med 0.6487, IQR 0.0503) | R-NSGA-III × PENALTY: 0.5966±0.0768 (med 0.5753, IQR 0.0754) | R-NSGA-III × KILL: 0.6082±0.0713 (med 0.6193, IQR 0.1062)
ed_min   | NSGA-III × PENALTY: 0.4479±0.0636 (med 0.4604, IQR 0.0693) | NSGA-III × KILL: 0.4783±0.0632 (med 0.4720, IQR 0.0557) | R-NSGA-III × PENALTY: 0.3890±0.0903 (med 0.3544, IQR 0.1245) | R-NSGA-III × KILL: 0.4803±0.0452 (med 0.4970, IQR 0.0669)
spacing  | NSGA-III × PENALTY: 0.0758±0.0269 (med 0.0647, IQR 0.0306) | NSGA-III × KILL: 0.0357±0.0066 (med 0.0338, IQR 0.0058) | R-NSGA-III × PENALTY: 0.0741±0.0307 (med 0.0662, IQR 0.0249) | R-NSGA-III × KILL: 0.0343±0.0086 (med 0.0321, IQR 0.0126)

=== INTERAÇÃO 2x2: F1xF2 (Alg × Elit) (n=10 por célula) ===
hv       | NSGA-III × ELIT_ON: 0.9070±0.1213 (med 0.8676, IQR 0.1376) | NSGA-III × ELIT_OFF: 0.8927±0.1600 (med 0.8676, IQR 0.0911) | R-NSGA-III × ELIT_ON: 0.8794±0.1556 (med 0.8253, IQR 0.1593) | R-NSGA-III × ELIT_OFF: 0.9262±0.1640 (med 0.9014, IQR 0.2544)
igd_plus | NSGA-III × ELIT_ON: 0.1545±0.0344 (med 0.1525, IQR 0.0435) | NSGA-III × ELIT_OFF: 0.1591±0.0577 (med 0.1488, IQR 0.0612) | R-NSGA-III × ELIT_ON: 0.1611±0.0597 (med 0.1647, IQR 0.0338) | R-NSGA-III × ELIT_OFF: 0.1271±0.0593 (med 0.1364, IQR 0.0898)
ed_media | NSGA-III × ELIT_ON: 0.6697±0.0776 (med 0.6492, IQR 0.0676) | NSGA-III × ELIT_OFF: 0.6581±0.0961 (med 0.6487, IQR 0.1464) | R-NSGA-III × ELIT_ON: 0.6333±0.0708 (med 0.6408, IQR 0.0568) | R-NSGA-III × ELIT_OFF: 0.5716±0.0627 (med 0.5584, IQR 0.0384)
ed_min   | NSGA-III × ELIT_ON: 0.4575±0.0532 (med 0.4604, IQR 0.0550) | NSGA-III × ELIT_OFF: 0.4687±0.0752 (med 0.4740, IQR 0.0688) | R-NSGA-III × ELIT_ON: 0.4559±0.0825 (med 0.4674, IQR 0.0811) | R-NSGA-III × ELIT_OFF: 0.4134±0.0838 (med 0.4228, IQR 0.1395)
spacing  | NSGA-III × ELIT_ON: 0.0633±0.0343 (med 0.0503, IQR 0.0487) | NSGA-III × ELIT_OFF: 0.0482±0.0189 (med 0.0402, IQR 0.0288) | R-NSGA-III × ELIT_ON: 0.0601±0.0370 (med 0.0497, IQR 0.0352) | R-NSGA-III × ELIT_OFF: 0.0482±0.0211 (med 0.0462, IQR 0.0242)

=== INTERAÇÃO 2x2: F2xF3 (Elit × Rest) (n=10 por célula) ===
hv       | ELIT_ON × PENALTY: 0.9723±0.1508 (med 0.9698, IQR 0.2369) | ELIT_ON × KILL: 0.8140±0.0520 (med 0.8270, IQR 0.0894) | ELIT_OFF × PENALTY: 1.0132±0.1497 (med 1.0202, IQR 0.1685) | ELIT_OFF × KILL: 0.8057±0.0822 (med 0.8431, IQR 0.1058)
igd_plus | ELIT_ON × PENALTY: 0.1434±0.0584 (med 0.1403, IQR 0.0512) | ELIT_ON × KILL: 0.1722±0.0300 (med 0.1686, IQR 0.0327) | ELIT_OFF × PENALTY: 0.1160±0.0636 (med 0.1050, IQR 0.0805) | ELIT_OFF × KILL: 0.1703±0.0417 (med 0.1548, IQR 0.0436)
ed_media | ELIT_ON × PENALTY: 0.6642±0.0899 (med 0.6385, IQR 0.0986) | ELIT_ON × KILL: 0.6388±0.0577 (med 0.6514, IQR 0.0387) | ELIT_OFF × PENALTY: 0.6066±0.1013 (med 0.5753, IQR 0.1287) | ELIT_OFF × KILL: 0.6231±0.0831 (med 0.6022, IQR 0.0878)
ed_min   | ELIT_ON × PENALTY: 0.4350±0.0776 (med 0.4463, IQR 0.0920) | ELIT_ON × KILL: 0.4784±0.0507 (med 0.4843, IQR 0.0748) | ELIT_OFF × PENALTY: 0.4019±0.0866 (med 0.3949, IQR 0.1414) | ELIT_OFF × KILL: 0.4802±0.0589 (med 0.4740, IQR 0.0544)
spacing  | ELIT_ON × PENALTY: 0.0859±0.0343 (med 0.0794, IQR 0.0399) | ELIT_ON × KILL: 0.0375±0.0087 (med 0.0349, IQR 0.0155) | ELIT_OFF × PENALTY: 0.0640±0.0148 (med 0.0615, IQR 0.0182) | ELIT_OFF × KILL: 0.0325±0.0054 (med 0.0318, IQR 0.0039)

=== CONTRASTES CONDICIONAIS (SIMPLES) NAS INTERAÇÕES 2x2 (n=10 vs n=10) ===
                                         contraste      ind  d_mean_pct        U  p_raw    A12         mag
  F1|PENALTY: R-NSGA-III vs NSGA-III (sob PENALTY)       hv      3.3256  58.0000 0.5708 0.5800     Pequena
  F1|PENALTY: R-NSGA-III vs NSGA-III (sob PENALTY) igd_plus    -22.9482  31.0000 0.1620 0.6900       Média
  F1|PENALTY: R-NSGA-III vs NSGA-III (sob PENALTY) ed_media    -11.5017  26.0000 0.0757 0.7400      Grande
  F1|PENALTY: R-NSGA-III vs NSGA-III (sob PENALTY)   ed_min    -13.1635  27.0000 0.0890 0.7300      Grande
  F1|PENALTY: R-NSGA-III vs NSGA-III (sob PENALTY)  spacing     -2.3302  43.0000 0.6232 0.5700     Pequena
        F1|KILL: R-NSGA-III vs NSGA-III (sob KILL)       hv     -3.2326  30.0000 0.1405 0.3000       Média
        F1|KILL: R-NSGA-III vs NSGA-III (sob KILL) igd_plus      4.9729  66.0000 0.2413 0.3400       Média
        F1|KILL: R-NSGA-III vs NSGA-III (sob KILL) ed_media     -6.9425  34.0000 0.2413 0.6600       Média
        F1|KILL: R-NSGA-III vs NSGA-III (sob KILL)   ed_min      0.4214  57.0000 0.6232 0.4300     Pequena
        F1|KILL: R-NSGA-III vs NSGA-III (sob KILL)  spacing     -4.0122  39.0000 0.4274 0.6100     Pequena
        F3|NSGA-III: PENALTY vs KILL (em NSGA-III)       hv     18.6339  79.0000 0.0312 0.7900      Grande
        F3|NSGA-III: PENALTY vs KILL (em NSGA-III) igd_plus    -12.3470  36.0000 0.3075 0.6400     Pequena
        F3|NSGA-III: PENALTY vs KILL (em NSGA-III) ed_media      3.1458  55.0000 0.7337 0.4500 Desprezível
        F3|NSGA-III: PENALTY vs KILL (em NSGA-III)   ed_min     -6.3590  42.0000 0.5708 0.5800     Pequena
        F3|NSGA-III: PENALTY vs KILL (em NSGA-III)  spacing    112.4347  98.0000 0.0003 0.0200      Grande
    F3|R-NSGA-III: PENALTY vs KILL (em R-NSGA-III)       hv     26.6741  86.0000 0.0073 0.8600      Grande
    F3|R-NSGA-III: PENALTY vs KILL (em R-NSGA-III) igd_plus    -35.6613  17.0000 0.0140 0.8300      Grande
    F3|R-NSGA-III: PENALTY vs KILL (em R-NSGA-III) ed_media     -1.9077  45.0000 0.7337 0.5500 Desprezível
    F3|R-NSGA-III: PENALTY vs KILL (em R-NSGA-III)   ed_min    -19.0267  19.0000 0.0211 0.8100      Grande
    F3|R-NSGA-III: PENALTY vs KILL (em R-NSGA-III)  spacing    116.1572 100.0000 0.0002 0.0000      Grande
F2|R-NSGA-III: ELIT_OFF vs ELIT_ON (em R-NSGA-III)       hv      5.3245  58.0000 0.5708 0.5800     Pequena
F2|R-NSGA-III: ELIT_OFF vs ELIT_ON (em R-NSGA-III) igd_plus    -21.1110  35.0000 0.2730 0.6500       Média
F2|R-NSGA-III: ELIT_OFF vs ELIT_ON (em R-NSGA-III) ed_media     -9.7509  24.0000 0.0539 0.7600      Grande
F2|R-NSGA-III: ELIT_OFF vs ELIT_ON (em R-NSGA-III)   ed_min     -9.3183  35.0000 0.2730 0.6500       Média
F2|R-NSGA-III: ELIT_OFF vs ELIT_ON (em R-NSGA-III)  spacing    -19.8604  42.0000 0.5708 0.5800     Pequena
    F2|NSGA-III: ELIT_OFF vs ELIT_ON (em NSGA-III)       hv     -1.5705  46.0000 0.7913 0.4600 Desprezível
    F2|NSGA-III: ELIT_OFF vs ELIT_ON (em NSGA-III) igd_plus      3.0047  52.0000 0.9097 0.4800 Desprezível
    F2|NSGA-III: ELIT_OFF vs ELIT_ON (em NSGA-III) ed_media     -1.7299  46.0000 0.7913 0.5400 Desprezível
    F2|NSGA-III: ELIT_OFF vs ELIT_ON (em NSGA-III)   ed_min      2.4580  57.0000 0.6232 0.4300     Pequena
    F2|NSGA-III: ELIT_OFF vs ELIT_ON (em NSGA-III)  spacing    -23.7547  38.0000 0.3847 0.6200     Pequena
F1|ELIT_OFF: R-NSGA-III vs NSGA-III (sob ELIT_OFF)       hv      3.7487  53.0000 0.8501 0.5300 Desprezível
F1|ELIT_OFF: R-NSGA-III vs NSGA-III (sob ELIT_OFF) igd_plus    -20.1006  36.0000 0.3075 0.6400     Pequena
F1|ELIT_OFF: R-NSGA-III vs NSGA-III (sob ELIT_OFF) ed_media    -13.1504  21.0000 0.0312 0.7900      Grande
F1|ELIT_OFF: R-NSGA-III vs NSGA-III (sob ELIT_OFF)   ed_min    -11.8051  31.0000 0.1620 0.6900       Média
F1|ELIT_OFF: R-NSGA-III vs NSGA-III (sob ELIT_OFF)  spacing     -0.1146  47.0000 0.8501 0.5300 Desprezível
  F1|ELIT_ON: R-NSGA-III vs NSGA-III (sob ELIT_ON)       hv     -3.0431  38.0000 0.3847 0.3800     Pequena
  F1|ELIT_ON: R-NSGA-III vs NSGA-III (sob ELIT_ON) igd_plus      4.3240  58.0000 0.5708 0.4200     Pequena
  F1|ELIT_ON: R-NSGA-III vs NSGA-III (sob ELIT_ON) ed_media     -5.4316  42.0000 0.5708 0.5800     Pequena
  F1|ELIT_ON: R-NSGA-III vs NSGA-III (sob ELIT_ON)   ed_min     -0.3517  53.0000 0.8501 0.4700 Desprezível
  F1|ELIT_ON: R-NSGA-III vs NSGA-III (sob ELIT_ON)  spacing     -4.9684  45.0000 0.7337 0.5500 Desprezível
     F2|PENALTY: ELIT_OFF vs ELIT_ON (sob PENALTY)       hv      4.2105  57.0000 0.6232 0.5700     Pequena
     F2|PENALTY: ELIT_OFF vs ELIT_ON (sob PENALTY) igd_plus    -19.1237  36.0000 0.3075 0.6400     Pequena
     F2|PENALTY: ELIT_OFF vs ELIT_ON (sob PENALTY) ed_media     -8.6803  30.0000 0.1405 0.7000       Média
     F2|PENALTY: ELIT_OFF vs ELIT_ON (sob PENALTY)   ed_min     -7.5962  40.0000 0.4727 0.6000     Pequena
     F2|PENALTY: ELIT_OFF vs ELIT_ON (sob PENALTY)  spacing    -25.5432  30.0000 0.1405 0.7000       Média
           F2|KILL: ELIT_OFF vs ELIT_ON (sob KILL)       hv     -1.0270  54.0000 0.7913 0.5400 Desprezível
           F2|KILL: ELIT_OFF vs ELIT_ON (sob KILL) igd_plus     -1.1378  44.0000 0.6776 0.5600     Pequena
           F2|KILL: ELIT_OFF vs ELIT_ON (sob KILL) ed_media     -2.4549  35.0000 0.2730 0.6500       Média
           F2|KILL: ELIT_OFF vs ELIT_ON (sob KILL)   ed_min      0.3770  48.0000 0.9097 0.5200 Desprezível
           F2|KILL: ELIT_OFF vs ELIT_ON (sob KILL)  spacing    -13.4102  36.0000 0.3075 0.6400     Pequena

  
  === 3-WAY FACTORIAL ANOVA DECOMPOSITION (% Sum of Squares & p-values) ===

--- HV (Total SS = 0.834811) ---
  C(F1_alg)                           : SS% =   0.01% | F(1,32) =   0.0060 | p = 0.9387
  C(F2_elit)                          : SS% =   0.32% | F(1,32) =   0.1854 | p = 0.6697
  C(F3_rest)                          : SS% =  40.08% | F(1,32) =  23.3800 | p = 0.0000
  C(F1_alg):C(F2_elit)                : SS% =   1.12% | F(1,32) =   0.6514 | p = 0.4256
  C(F1_alg):C(F3_rest)                : SS% =   1.05% | F(1,32) =   0.6098 | p = 0.4406
  C(F2_elit):C(F3_rest)               : SS% =   0.73% | F(1,32) =   0.4245 | p = 0.5193
  C(F1_alg):C(F2_elit):C(F3_rest)     : SS% =   1.84% | F(1,32) =   1.0716 | p = 0.3083
  Residual                            : SS% =  54.86%

--- IGD_PLUS (Total SS = 0.111871) ---
  C(F1_alg)                           : SS% =   1.43% | F(1,32) =   0.6491 | p = 0.4264
  C(F2_elit)                          : SS% =   1.93% | F(1,32) =   0.8750 | p = 0.3566
  C(F3_rest)                          : SS% =  15.46% | F(1,32) =   7.0157 | p = 0.0124
  C(F1_alg):C(F2_elit)                : SS% =   3.34% | F(1,32) =   1.5153 | p = 0.2273
  C(F1_alg):C(F3_rest)                : SS% =   3.93% | F(1,32) =   1.7818 | p = 0.1914
  C(F2_elit):C(F3_rest)               : SS% =   1.45% | F(1,32) =   0.6571 | p = 0.4236
  C(F1_alg):C(F2_elit):C(F3_rest)     : SS% =   1.93% | F(1,32) =   0.8761 | p = 0.3563
  Residual                            : SS% =  70.53%

--- ED_MEDIA (Total SS = 0.275381) ---
  C(F1_alg)                           : SS% =  13.72% | F(1,32) =   5.8081 | p = 0.0219
  C(F2_elit)                          : SS% =   4.88% | F(1,32) =   2.0676 | p = 0.1602
  C(F3_rest)                          : SS% =   0.07% | F(1,32) =   0.0308 | p = 0.8617
  C(F1_alg):C(F2_elit)                : SS% =   2.28% | F(1,32) =   0.9675 | p = 0.3327
  C(F1_alg):C(F3_rest)                : SS% =   0.94% | F(1,32) =   0.3977 | p = 0.5328
  C(F2_elit):C(F3_rest)               : SS% =   1.60% | F(1,32) =   0.6773 | p = 0.4166
  C(F1_alg):C(F2_elit):C(F3_rest)     : SS% =   0.93% | F(1,32) =   0.3946 | p = 0.5343
  Residual                            : SS% =  75.57%

--- ED_MIN (Total SS = 0.218662) ---
  C(F1_alg)                           : SS% =   3.71% | F(1,32) =   1.7335 | p = 0.1973
  C(F2_elit)                          : SS% =   1.12% | F(1,32) =   0.5216 | p = 0.4754
  C(F3_rest)                          : SS% =  16.96% | F(1,32) =   7.9321 | p = 0.0082
  C(F1_alg):C(F2_elit)                : SS% =   3.30% | F(1,32) =   1.5431 | p = 0.2232
  C(F1_alg):C(F3_rest)                : SS% =   4.25% | F(1,32) =   1.9877 | p = 0.1682
  C(F2_elit):C(F3_rest)               : SS% =   1.39% | F(1,32) =   0.6490 | p = 0.4264
  C(F1_alg):C(F2_elit):C(F3_rest)     : SS% =   0.83% | F(1,32) =   0.3903 | p = 0.5366
  Residual                            : SS% =  68.44%

--- SPACING (Total SS = 0.032007) ---
  C(F1_alg)                           : SS% =   0.08% | F(1,32) =   0.0610 | p = 0.8065
  C(F2_elit)                          : SS% =   5.68% | F(1,32) =   4.3348 | p = 0.0454
  C(F3_rest)                          : SS% =  49.89% | F(1,32) =  38.0641 | p = 0.0000
  C(F1_alg):C(F2_elit)                : SS% =   0.07% | F(1,32) =   0.0568 | p = 0.8131
  C(F1_alg):C(F3_rest)                : SS% =   0.00% | F(1,32) =   0.0007 | p = 0.9795
  C(F2_elit):C(F3_rest)               : SS% =   2.24% | F(1,32) =   1.7053 | p = 0.2009
  C(F1_alg):C(F2_elit):C(F3_rest)     : SS% =   0.09% | F(1,32) =   0.0708 | p = 0.7919
  Residual                            : SS% =  41.94%

=== CORRELATIONS (SPEARMAN & PEARSON) ACROSS N=40 RUNS ===
  spacing  vs hv      : Pearson r = +0.6708 (p=2.1784e-06) | Spearman rho = +0.6722 (p=2.0311e-06)
  spacing  vs igd_plus: Pearson r = -0.4280 (p=5.8720e-03) | Spearman rho = -0.3966 (p=1.1283e-02)
  spacing  vs ed_media: Pearson r = +0.0151 (p=9.2654e-01) | Spearman rho = -0.0006 (p=9.9725e-01)
  spacing  vs ed_min  : Pearson r = -0.4194 (p=7.0624e-03) | Spearman rho = -0.3319 (p=3.6417e-02)
  spacing  vs n_pontos: Pearson r = -0.3425 (p=3.0487e-02) | Spearman rho = -0.3179 (p=4.5640e-02)
  hv       vs igd_plus: Pearson r = -0.8885 (p=2.0067e-14) | Spearman rho = -0.8644 (p=6.6794e-13)
  [PENALTY] spacing vs hv: Spearman rho = +0.4617 (p=0.0405) | n_pontos mean=106.50±25.81, dup mean=7.75
  [KILL   ] spacing vs hv: Spearman rho = +0.2361 (p=0.3163) | n_pontos mean=121.15±10.86, dup mean=9.00