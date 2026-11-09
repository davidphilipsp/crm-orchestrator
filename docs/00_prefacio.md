# Prefácio

Bem-vindo ao repositório crm-orchestrator. Este documento serve como prefácio e guia rápido para colaboradores, agentes e leitores que chegam ao projeto pela primeira vez.

Propósito
- Documentar o propósito, escopo e convenções do projeto.
- Orientar agentes automatizados (squads/agents) e humanos sobre onde encontrar informações relevantes.

Como usar estes documentos
- Cada arquivo em `docs/` corresponde a um capítulo do índice principal (CLAUDE.md).
- Leia `memory/` para padrões confirmados por dados e `squad/config.yaml` para a configuração dos agentes.

Fluxo de trabalho recomendado
- `memory/` é append-only: registre hipóteses em `memory/hypothesis_log.md` e padrões confirmados em `memory/memory.json`.
- Alterações na documentação devem ser pequenas, revisadas e versionadas via PR. Se um documento for substituído, preserve histórico e marque versões antigas como deprecadas.

Contribuições e convenções
- Escreva em Português claro e direto.
- Use arquivos Markdown em `docs/` com nomes `NN_titulo.md` seguindo o índice do `CLAUDE.md`.
- Referencie evidências de dados apontando para arquivos em `memory/` quando aplicável.

Referências rápidas
- Índice principal: `CLAUDE.md`
- Memória e hipóteses: `memory/hypothesis_log.md`, `memory/memory.json`
- Squad/agents: `squad/config.yaml`

Próximos passos
- Criar os capítulos sequenciais a partir de `docs/01_contexto.md`. Peça confirmação antes de avançar.
