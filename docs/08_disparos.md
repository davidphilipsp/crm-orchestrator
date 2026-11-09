# Disparos

Este capítulo descreve como o `crm-orchestrator` deve pensar, validar e recomendar disparos de CRM.

Objetivo dos disparos

- Ativar engajamento e reativação de usuários.
- Preservar margem e evitar excesso de exposição para evitar fadiga.
- Sincronizar campanhas com calendário de produtos e eventos promocionais.

Canais suportados

- SMS: principal canal de ação rápida para missões e alertas.
- Outros canais podem ser adicionados conforme integrados ao pipeline.

Segmentos e prioridade

- `Low`, `Medium`, `High` são exemplos de segmentos de base.
- Preferir mensagens de missão para segmentos mais sensíveis à oferta.
- Ajustar frequência por taxa de entrega e evidências de fadiga.

Regras de envio

- Não disparar mensagens redundantes para o mesmo usuário em curto prazo.
- Para campanhas de SMS D1–D5, avaliar se há gap de comunicação e priorizar missões de abertura.
- A regra de copy deve mudar após máximo 3 dias consecutivos para o mesmo segmento, segundo `memory/memory.json`.

Critérios de decisão

- Se a taxa de entrega do segmento estiver acima do limiar configurado, o disparo pode ser considerado seguro.
- Se a taxa cair progressivamente (por exemplo, `boas_vindas_clube` vs `base_geral_urgencia`), reduzir frequência ou trocar copy.
- Utilizar valores de giros e margens definidos em `memory/memory.json` para calibrar custo de oferta.

Exemplos de disparo

- Envio de SMS de missão nos primeiros 5 dias do mês quando há gap em `D1-D5` e torneios ativos.
- Série de mensagens de progressão de missão com trigger de evento `Gamification: mission completed`.
- Ação diferenciada para VIPs com giros de valor mínimo configurado (`VIP_MIN_SPIN_VALUE`).

Validação e controle

- Cada disparo recomendado deve ter justificativa baseada em histórico e regras de compliance.
- Documentar no `memory/` sempre que uma nova regra de disparo for confirmada ou invalidada.
- Revisar periodicamente a performance de cada copy e segmento para ajustar o modelo.
