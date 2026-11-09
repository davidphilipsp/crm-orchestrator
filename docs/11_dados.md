# Dados

Este capítulo descreve as fontes de dados, formatos e pipelines usados pelo `crm-orchestrator`.

Fontes de dados

- `data/raw/disparador.csv`: dados de disparo e atributos de usuário.
- Outros arquivos CSV ou fontes conectadas que alimentam o processo de análise.

Pipeline de dados

- Extração: `src/extract.py` processa entradas brutas e normaliza dados.
- Transformação: `src/transform.py` limpa, mapeia segmentos e prepara variáveis de campanha.
- Análise: `src/analyze.py` executa validações, score e recomendações.
- Copy scoring: `src/score_copy.py` avalia texto, canal, segmento e dia.

Formatos e convenções

- Use nomes de colunas consistentes e legíveis para atributos de usuário e campanha.
- Valores de segmentos devem seguir convenções claras (`Low`, `Medium`, `High`).
- Datas devem ser armazenadas em formato ISO (`YYYY-MM-DD`) quando possível.

Qualidade de dados

- Verificar duplicatas e valores ausentes antes de rodar análises.
- Mapear segmentos e eventos de forma estável para evitar alterações intempestivas.
- Registrar suposições de dados e transformações em `docs/11_dados.md` quando existirem.

Evidências e aprendizado

- Resultados de validação devem ser usados para atualizar `memory/memory.json`.
- Hipóteses de comportamento devem ser documentadas em `memory/hypothesis_log.md`.
- Use `data/interim/` e `outputs/` para armazenar dados processados e relatórios.
