# Contexto

O `crm-orchestrator` é um orquestrador de CRM para um operador de iGaming (brand-a). Ele combina análise de dados reais, recomendações acionáveis e validação de hipóteses para apoiar campanhas de engajamento, reativação e otimização de jornada.

Objetivos do projeto

- Capturar regras e padrões de comportamento de campanhas com base em dados históricos.
- Produzir recomendações de disparo e copy com justificativas quantitativas.
- Monitorar hipóteses de negócio e registrar resultados em uma memória de aprendizado.
- Facilitar a integração entre análise, engenharia de dados e operações de CRM.

Fontes de informação

- `memory/memory.json` contém padrões confirmados, regras, limites de ação e evidências de desempenho.
- `memory/hypothesis_log.md` lista hipóteses abertas, critérios de validação e status de experimentos.
- `squad/config.yaml` descreve agentes e seus contextos de trabalho.
- `README.md` mostra o fluxo básico de uso e os comandos de execução.

Escopo principal

- Analisar arquivos de dados de disparo (`data/raw/disparador.csv`).
- Avaliar copy e segmentação por canal, segmento e dia. Exemplo: SMS para segmentos `Low`, `Medium`, `High`.
- Validar regras de calendário, campanhas, missões e estruturas de recompensa.
- Documentar e preservar decisões em `memory/`.

Público-alvo

- analistas de CRM
- desenvolvedores de dados
- responsáveis por automação de jornadas
- gerentes de campanha

Valores centrais

- Transparência: cada recomendação deve ter justificativa baseada em dados.
- Iteração: hipóteses são registradas, testadas e atualizadas continuamente.
- Segurança de operação: regras formais de compliance e de geração de disparos devem ser documentadas.

Leitura recomendada

- `docs/03_principios.md`: princípios de operação e governança.
- `docs/08_disparos.md`: como funcionam os disparos e as regras de envío.
- `docs/11_dados.md`: fontes de dados, pipelines e formatos suportados.
