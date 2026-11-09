# Critérios de Sucesso

Este capítulo define como o `crm-orchestrator` mede o sucesso de suas recomendações e operações.

Objetivo

- Definir métricas claras para avaliar o impacto de campanhas e réguas.
- Garantir que o resultado das ações seja mensurável e alinhado ao negócio.

Principais métricas

- GGR incremental: ganho adicional de receita gerado por campanhas.
- Taxa de entrega: proporção de mensagens efetivamente entregues.
- Taxa de conversão: percentual de usuários que executam a ação desejada após o disparo.
- Taxa de conclusão de missão: usuários que completam missões propostas.
- Retenção: usuários ativos após 7 e 14 dias.

Critérios qualitativos

- Clareza das mensagens e relevância do engajamento.
- Conformidade com políticas e respeito a opt-outs.
- Capacidade de iterar e ajustar rapidamente com base em evidências.

Avaliação de hipóteses

- Hipóteses listadas em `memory/hypothesis_log.md` devem ter critérios de validação definidos.
- Resultados devem ser comparados com séries históricas e grupos de controle.
- Hipóteses confirmadas atualizam `memory/memory.json` com padrões e recomendações.

Ciclo de revisão

- Revisar resultados semanais e ajustar regras conforme necessário.
- Documentar aprendizados e anomalias.
- Usar insights para melhorar segmentação, copy e timing.
