# Réguas

Este capítulo descreve as réguas de decisão e as condições que orientam o fluxo de campanhas e jornadas.

Definição

- Réguas são conjuntos de regras que mapeiam eventos, segmentos, canais e ações.
- Cada régua representa um caminho de ativação ou uma lógica de progressão de campanha.

Componentes principais

- Evento de entrada: trigger que aciona a régua, por exemplo `mission completed`, `deposit made` ou `segment entered`.
- Condições: atributos do usuário, performance da campanha e limites de frequência.
- Ações: disparos de SMS, atualizações de jornada, ou envio de sinal para ferramenta de automação.

Régua de missões

- Iniciar após evento `Gamification: mission unlocked` ou `mission completed`.
- Enviar mensagem de progresso somente se o usuário não recebeu disparo semelhante nas últimas 24 horas.
- Ajustar a copy quando a mesma régua for reutilizada por mais de 3 dias consecutivos.

Régua de reativação

- Acionar para usuários com inatividade de 7+ dias e potencial de redepositar.
- Priorizar ofertas com valor de giro e margem segura conforme `memory/memory.json`.
- Evitar chamadas para usuários já expostos a campanhas recentes ou com baixa taxa de entrega.

Régua de VIP

- Usuários VIP devem receber ofertas diferenciadas com giros de valor mínimo configurado (`VIP_MIN_SPIN_VALUE`).
- A possibilidade de reativação deve ser ponderada com o custo do giro e o perfil de depósito.
- Regras de prioridade vigência/valor para evitar saturação de VIPs.

Régua de calendário

- Sincronizar ações com eventos de torneio e picos previstos de GGR.
- Reduzir mensagens a usuários em dias de baixa entrega ou quando campanhas concorrentes estão ativas.
- Estabelecer limites diários e semanais para cada segmento, apoiados por métricas de taxa de entrega.

Governança de réguas

- Todo ajuste de régua deve ser documentado em `docs/` e referenciado em `memory/memory.json`.
- Revisar a eficácia das réguas em ciclos de 7–14 dias.
- Alterações só devem ser aplicadas após validação quantitativa ou aprovação de compliance.
