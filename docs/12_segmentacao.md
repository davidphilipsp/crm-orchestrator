# Segmentação

Este capítulo descreve as estratégias de segmentação para campanhas de CRM.

Objetivo

- Selecionar públicos com maior propensão a responder bem à comunicação.
- Equilibrar volume e risco de queda de taxa de entrega.
- Usar segmentos como mecanismo de personalização e proteção contra fadiga.

Tipos de segmentos

- `Low`, `Medium`, `High`: segmentos básicos por engajamento ou valor.
- Segmentos de boas-vindas e urgência, como `boas_vindas_clube` e `base_geral_urgencia`.
- Segmentos VIP: usuários com maior valor e acesso a ofertas diferenciadas.

Regras de segmentação

- Priorizar segmentos com entregas saudáveis acima do limiar configurado.
- Reduzir exposição de segmentos com evidência de fadiga e queda de taxa.
- Aplicar regras especiais para VIPs, considerando o valor do giro e a margem segura.

Segmentação por comportamento

- Usar histórico de depósito, missão e interação para criar grupos mais precisos.
- Identificar usuários propensos a reativação por meio de atividades recentes ou inatividade curta.
- Segmentar quem já participou de torneios ou missões com sucesso.

Integração com outras áreas

- `segment_planner` deve atualizar segmentos com base em análises e resultados.
- `copy_analyst` deve ajustar copy para cada segmento.
- `calendar_optimizer` deve alinhar segmentos a janelas de campanha.

Evidências e aprendizado

- Documentar performance de segmentos em `memory/memory.json`.
- Validar novas divisões de público antes de torná-las padrão.
- Revisar segmentos periodicamente para capturar mudanças no comportamento.
