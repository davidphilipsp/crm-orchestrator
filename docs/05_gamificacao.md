# Gamificação

Este capítulo descreve a estratégia de gamificação usada pelo `crm-orchestrator` para engajar usuários e impulsionar comportamentos desejados.

Objetivo

- Tornar a jornada mais envolvente por meio de missões e recompensas.
- Incentivar ações valiosas, como depósitos e participação em torneios.
- Aumentar retenção por meio de progressão clara e recompensas percebidas.

Elementos de gamificação

- Missões: tarefas que o usuário deve completar para ganhar recompensas.
- Progresso: comunicação de etapas concluídas e próximas ações.
- Recompensas: giros, bônus ou ofertas com valor vinculado a margem segura.

Regras básicas

- Use triggers de evento para ativar missões: por exemplo, `Gamification: mission completed`.
- Não exponha o mesmo usuário a muitas missões simultâneas para evitar fadiga.
- Ajuste o valor dos giros de acordo com o perfil VIP e a margem definida em `memory/memory.json`.

Dados e evidências

- As regras de valor de giro e segmentação VIP são definidas em `memory/memory.json`.
- Padrões como `val_giro_minimo_vip` e `jogos_com_r2` orientam ofertas mais relevantes.

Integração com o fluxo

- `gamification_manager` cria a lógica de ativação e progressão de missões.
- `journey_builder` integra missões nas jornadas de usuários.
- `analyst` mede o impacto das missões em depósitos e retenção.

Boas práticas

- Documente cada mecânica de missão em `docs/06_missoes_diarias.md`.
- Mantenha a promessa de recompensa clara e realizável.
- Preferir copys de incentivo positivo e progressão incremental.
