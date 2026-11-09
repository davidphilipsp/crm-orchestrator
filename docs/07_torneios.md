# Torneios

Este capítulo descreve como o `crm-orchestrator` deve considerar torneios como momentos estratégicos de engajamento.

Objetivo

- Aproveitar picos de interesse e receita gerados por torneios.
- Ajustar ações de CRM para não competir com eventos internos ou externos.
- Usar torneios como gatilho para ofertas de alto valor.

Impacto de torneios

- Torneios podem gerar picos de GGR acima da média (medir no próprio histórico).
- A ativação concurrente de campanha e torneio pode aumentar os resultados quando bem coordenada.
- Campanhas mal sincronizadas podem diluir a taxa de entrega.

Regras de ativação

- Priorizar notificações e ofertas durante janelas de torneio de alta visibilidade.
- Evitar sobrecarregar usuários com mensagens durante eventos críticos.
- Usar a régua de torneio para segmentar usuários com maior propensão a participar.

Coordenação com calendário

- `calendar_optimizer` deve mapear juntas as datas de torneio e outras campanhas.
- `tournament_manager` deve definir quais segmentos e mensagens são mais apropriados.
- A sobreposição de torneios e campanhas de VIP deve ser avaliada cuidadosamente.

Métricas

- Taxa de resposta durante eventos de torneio.
- GGR incremental em comparação com períodos de base.
- Retenção e recompra após torneios.
