# SBSE no contexto de microsserviços

Trabalho desenvolvido para a disciplina **Tópicos Avançados em Engenharia de Software II**, do Programa de Pós-Graduação em Ciência da Computação da Universidade Estadual de Maringá (UEM).

## Integrantes

- Hélio Toshio Kamakawa
- Kananda Caroline

## Professores

- Thelma Elita Colanzi
- João Choma Neto

## Tema

O seminário e o relatório abordam *Search-Based Software Engineering* (SBSE) no contexto da identificação de fronteiras de microsserviços. O estudo utiliza como exemplos centrais o **MSExtractor** e o **SAMIM**, duas propostas explicitamente baseadas em busca, e apresenta o **MSDC** como abordagem complementar de otimização multiobjetivo.

## Trabalhos analisados

1. **Improving Microservices Extraction Using Evolutionary Search** — Sellami et al. (2022), trabalho que apresenta o MSExtractor.
2. **A Search-Based Identification of Variable Microservices for Enterprise SaaS** — Khoshnevis (2023), trabalho que apresenta o SAMIM.
3. **Enhancing Automated Microservice Decomposition via Multi-Objective Optimization** — Kinoshita e Kanuka (2024), trabalho que apresenta o MSDC.

Os artigos estão disponíveis na pasta [`referencias`](referencias/).

## Roteiro do trabalho

1. Contexto e motivação para a identificação de fronteiras de microsserviços.
2. Conceitos fundamentais de SBSE:
   - formulação do problema de otimização;
   - espaço de busca;
   - representação das soluções;
   - funções objetivo;
   - geração, avaliação e seleção de candidatos;
   - objetivos conflitantes, *trade-offs*, não dominância e fronteira de Pareto.
3. Monólitos, microsserviços e o banco de dados como dimensão de acoplamento.
4. Apresentação e análise do MSExtractor.
5. Apresentação e análise do SAMIM.
6. Apresentação do MSDC como abordagem complementar.
7. Comparação entre entradas, representações, objetivos, algoritmos, mecanismos de busca e critérios de seleção.
8. Consolidação da estrutura conceitual comum e discussão do papel da otimização como apoio à decisão arquitetural.

## Arquivos

- `apresentacao_helio_kananda.pdf`: versão final dos slides utilizados na apresentação do seminário.
- `relatorio_helio_kananda.pdf`: versão final do relatório produzido a partir do estudo dos artigos e das discussões realizadas no seminário.

## Observação

O relatório e os slides não se limitam ao conteúdo preparado antes da apresentação. Ambos incorporam correções, esclarecimentos e discussões que fizeram parte do seminário, incluindo questões levantadas após a exposição e contribuições dos professores. Essas revisões permitiram ajustar terminologias, explicitar os limites de interpretação dos artigos e aprofundar a comparação entre os trabalhos e os fundamentos de SBSE abordados em aula.
