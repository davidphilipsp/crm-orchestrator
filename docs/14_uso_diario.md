# Uso Diário

Este capítulo descreve como usar o `crm-orchestrator` no dia a dia operacional.

Objetivo

- Tornar a operação diária previsível e eficiente.
- Definir etapas claras para leitura, execução e revisão.

Fluxo diário

1. Verificar dados brutos e fontes de entrada.
2. Executar extração e transformação de dados.
3. Rodar análises e scoring de campanhas.
4. Revisar recomendações e planejar disparos.
5. Atualizar memória e documentação com novos insights.

Atividades regulares

- `data_engineer`: validação de dados e preparação de arquivos.
- `analyst`: revisão de métricas e validação de hipóteses.
- `copy_analyst`, `journey_builder` e `segment_planner`: ajustes de campanha.
- `compliance_tc`: verificação de listas de bloqueio e limites de contato.

Checklist diário

- [ ] Conferir se os dados brutos foram recebidos.
- [ ] Verificar integrações de `data/raw/`.
- [ ] Validar segmentação e regras de disparo propostas.
- [ ] Confirmar se a comunicação está alinhada com o calendário.
- [ ] Registrar qualquer mudança relevante em `memory/`.

Boas práticas

- Use logs e documentação para rastrear alterações.
- Mantenha a revisão de compliance como parte do processo padrão.
- Atualize os capítulos de `docs/` quando surgir nova informação importante.
