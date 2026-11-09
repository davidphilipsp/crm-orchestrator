# Compliance

Este capítulo descreve as regras de compliance e os cuidados necessários para operações de CRM.

Princípios de compliance

- Proteção do usuário: não enviar mensagens excessivas ou indesejadas.
- Conformidade com bloqueios: respeitar listas de exclusão e políticas de opt-out.
- Transparência de oferta: não prometer benefícios que não podem ser entregues.

Regras principais

- Não enviar SMS a usuários que optaram por sair ou estão em listas de bloqueio.
- Respeitar limites de frequência de canal, especialmente para SMS e notificações instantâneas.
- Garantir que as ofertas de giros e bônus estejam dentro das margens definidas em `memory/memory.json`.

Checklist de compliance

- [ ] Verificar lista de opt-out antes de cada disparo.
- [ ] Confirmar que a campanha não viola regras sobre frequência de mensagens.
- [ ] Registrar justificativa de cada ação de disparo quando houver exceção.
- [ ] Revisar copy de SMS para evitar linguagem enganosa ou sensível.

Integração com squad

- `compliance_tc` deve ser consultado para aprovar réguas e ofertas de alto impacto.
- `copy_analyst` deve aplicar as diretrizes de compliance nas mensagens.
- `journey_builder` deve garantir que a jornada respeite listas de exclusão e limites de contato.

Validação de novos casos

- Qualquer nova condição de exceção deve ser documentada em `docs/10_compliance.md`.
- Regras de compliance devem ser testadas em ambiente controlado antes de irem para produção.
- Exceções somente com aprovação formal e registro de evidência.
