# Missões Diárias

Este capítulo detalha as missões diárias e como elas devem ser usadas para engajamento contínuo.

Objetivo

- Criar pontos de contato diários que incentivem comportamento recorrente.
- Usar missões como caminho para retenção e depósito.
- Manter a jornada clara e motivadora.

Tipos de missões

- Missões de ativação: completar a primeira ação do dia.
- Missões de progresso: avançar em objetivos semanais ou mensais.
- Missões de recompensa: ganhar giros ou ofertas por cumprir metas.

Lógica de envio

- Disparar mensagens de missão quando o usuário estiver elegível e não tiver recebido uma missão semelhante nas últimas 24 horas.
- Priorizar missões que ofereçam progresso claro.
- Ajustar a sequência de missões de acordo com a resposta do usuário.

Regras de recompensa

- Giros e valores devem respeitar a margem segura definida em `memory/memory.json`.
- VIPs devem receber ofertas com valor mínimo configurado (`VIP_MIN_SPIN_VALUE`).
- Recompensas devem ser percebidas como alcançáveis e atraentes.

Métricas de sucesso

- Taxa de conclusão de missão.
- Impacto na próxima ação de depósito.
- Retenção do usuário nos dias seguintes.

Integração operacional

- `gamification_manager` define a mecânica das missões.
- `journey_builder` incorpora missões às jornadas de CRM.
- `analyst` monitora o impacto e ajusta as missões com base em dados.
