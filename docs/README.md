# Documentacion de NanoCheck

Este directorio concentra la documentacion funcional y tecnica del proyecto. La idea es separar con claridad tres capas:

- que queremos construir
- por que tomamos determinadas decisiones
- en que punto real esta el repositorio

## Mapa de documentos

- [architecture.md](architecture.md): arquitectura objetivo del sistema y flujo entre componentes.
- [development.md](development.md): convenciones de trabajo, entorno local y huecos pendientes para empezar a desarrollar.
- [domain-model.md](domain-model.md): entidades principales del dominio y relaciones previstas.
- [mvp.md](mvp.md): alcance minimo del producto y criterios de corte.
- [decisions/stack.md](decisions/stack.md): decisiones tecnicas con estado, alternativas y consecuencias.
- [roadmap/goals.md](roadmap/goals.md): roadmap ejecutable por fases con entregables y dependencias.

## Estado documental

La documentacion actual describe una vision tecnica y de producto para un repositorio que todavia esta en fase inicial. Cuando aparezca codigo funcional, estos documentos deberian actualizarse para reflejar:

- lo que ya esta implementado
- lo que sigue siendo una decision abierta
- lo que se ha descartado

## Criterio editorial

Para mantener la documentacion util:

- el `README` de raiz debe explicar el estado real del repo
- las decisiones tecnicas deben indicar si estan propuestas, aceptadas o implementadas
- el roadmap debe usarse para planificar trabajo, no para describir ideas sueltas
