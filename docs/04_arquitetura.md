# Arquitetura

Este capítulo descreve a arquitetura conceitual do `crm-orchestrator`.

Visão geral

O sistema é composto por três camadas principais:

1. Ingestão de dados
- `src/extract.py`: lê dados brutos de `data/raw/` e valida campos essenciais.
- Prepara arquivos para transformação.

2. Transformação e preparação
- `src/transform.py`: limpa, mapeia segmentos e normaliza atributos.
- Escreve resultados em `data/interim/` para análise e scoring.

3. Análise e recomendações
- `src/analyze.py`: usa dados transformados para gerar insights, validar hipóteses e produzir recomendações.
- `src/score_copy.py`: avalia texto, canal e segmento para sugestão de copy.

Memória e governança

- `memory/hypothesis_log.md`: registro de hipóteses e experimentos.
- `memory/memory.json`: padrões confirmados, regras, evidências e parâmetros operacionais.
- `docs/`: documentação de princípios, réguas, compliance e uso.

Squad e responsabilidades

- Cada agente em `squad/config.yaml` representa uma responsabilidade do fluxo.
- O `data_engineer` mantém a qualidade dos dados.
- O `analyst` valida hipóteses e insumos.
- O `segment_planner` define públicos.
- O `calendar_optimizer`, `gamification_manager` e `tournament_manager` organizam timing e ações.
- O `compliance_tc` garante conformidade.

Fluxo de execução

1. Captura e validação de dados brutos.
2. Transformação e normalização dos dados.
3. Análise de padrões e geração de regras.
4. Recomendação de disparos e copy.
5. Registro de resultados e atualização da memória.

Integração operacional

- O projeto deve ser modular para permitir atualizações incrementais.
- Regras de disparo e segmentação são desacopladas da lógica de dados.
- Documentação e memória mantêm a explicabilidade do sistema.
