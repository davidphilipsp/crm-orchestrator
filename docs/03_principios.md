# Princípios

Este capítulo descreve os princípios que guiam o desenvolvimento, análise e operação do `crm-orchestrator`.

1. Orientação por dados
- As recomendações devem ser fundamentadas em evidências, métricas e padrões históricos.
- Toda regra operacional deve estar associada a um racional documentado em `memory/memory.json` ou `memory/hypothesis_log.md`.

2. Transparência e rastreabilidade
- Documente decisões em `docs/` e evidências em `memory/`.
- Use nomes claros para segmentos, triggers e variáveis de campanha.

3. Iteração controlada
- Hipóteses são registradas, avaliadas e atualizadas sem apagar histórico.
- Novas regras devem ser testadas em experimentos A/B antes de virar padrão.

4. Segurança de operação
- Evite ações de alto risco sem validação de compliance.
- A parte de compliance deve estar documentada em `docs/10_compliance.md` e referenciada nas regras de disparo.

5. Modularidade e separação de responsabilidades
- Modelos de dados, regras de negócio e recomendações devem ser mantidos em camadas distintas.
- `squad/config.yaml` define agentes com responsabilidades claras para copy, jornada, análise, segmentação e compliance.

6. Simplicidade e legibilidade
- Prefira abordagens simples e fáceis de explicar.
- Regra complexa demais deve ser desmembrada em partes menores.

7. Aprendizado contínuo
- Padrões confirmados e dados validados são incorporados à memória do projeto.
- Registre insights de campanha de forma que possam ser reutilizados em novas execuções.

8. Foco em objetivo de negócio
- As ações devem priorizar crescimento saudável do GGR e retenção, dentro de limites de margem seguros.
- A recomendação ideal considera custo da oferta, valor esperado e perfil do usuário.
