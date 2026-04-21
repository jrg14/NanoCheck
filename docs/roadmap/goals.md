# Roadmap de NanoCheck

## Objetivo

Convertir el repositorio desde su estado actual de definicion tecnica a un backend funcional capaz de monitorizar endpoints y exponer metricas utiles.

## Estado de partida

Situacion actual del repo:

- [x] Vision del producto documentada
- [x] Direccion tecnica inicial documentada
- [x] Configuracion basica de dependencias Python
- [x] API implementada
- [x] Persistencia implementada
- [ ] Scheduler y workers implementados
- [ ] Tests funcionales

## Fase 1 - Fundamentos del backend

- Objetivo: crear una aplicacion ejecutable con estructura clara.
- Dependencias: ninguna.
- Entregables:
  - [ ] estructura base de `app/` y `modules/`
  - [x] app `FastAPI` inicial
  - [x] modulo de configuracion
  - [ ] `README` con arranque real
  - [ ] pipeline minima de lint y tests

## Fase 2 - Identidad y dominio base

- Objetivo: modelar usuarios, proyectos y endpoints.
- Dependencias: Fase 1.
- Entregables:
  - [x] modelo `User`
  - [ ] modelo `Project`
  - [ ] modelo `Endpoint`
  - [ ] CRUD de proyectos
  - [ ] CRUD de endpoints
  - [ ] validaciones de URL, metodo y frecuencia

## Fase 3 - Persistencia real

- Objetivo: conectar el dominio con almacenamiento relacional.
- Dependencias: Fase 2.
- Entregables:
  - [ ] configuracion de base de datos
  - [ ] modelos ORM
  - [ ] estrategia de sesiones
  - [ ] migraciones
  - [ ] tests de repositorio

## Fase 4 - Checks automatizados

- Objetivo: ejecutar monitorizacion periodica y guardar resultados.
- Dependencias: Fase 3.
- Entregables:
  - [ ] definicion de `Metric`
  - [ ] worker de checks
  - [ ] scheduler
  - [ ] manejo de timeout y errores de red
  - [ ] persistencia de metricas crudas

## Fase 5 - Metricas del MVP

- Objetivo: exponer indicadores utiles sobre los checks ejecutados.
- Dependencias: Fase 4.
- Entregables:
  - [ ] latencia media
  - [ ] disponibilidad
  - [ ] tasa de error
  - [ ] numero de checks
  - [ ] endpoint de consulta por ventana temporal

## Fase 6 - Calidad operativa

- Objetivo: llevar el sistema a un nivel mantenible.
- Dependencias: Fase 5.
- Entregables:
  - [ ] tests por modulo
  - [ ] tests de API
  - [ ] tests de workers con mocks HTTP
  - [ ] logging estructurado
  - [ ] manejo global de excepciones

## Fase 7 - Escalado analitico

- Objetivo: reducir coste de lectura y preparar volumen.
- Dependencias: Fase 6.
- Entregables:
  - [ ] agregaciones por ventana
  - [ ] indices principales
  - [ ] endpoints optimizados para metricas
  - [ ] decision de retencion de metricas

## Fase 8 - Alertas e insights

- Objetivo: generar valor adicional a partir de degradaciones.
- Dependencias: Fase 7.
- Entregables:
  - [ ] reglas de alerta
  - [ ] eventos de alerta
  - [ ] deduplicacion o cooldown
  - [ ] comparativa entre ventanas

## Backlog posterior al MVP

- [ ] dashboard frontend
- [ ] websocket en tiempo real
- [ ] `TimescaleDB`
- [ ] rate limiting
- [ ] API keys por proyecto
- [ ] sistema de billing simulado

## Definicion de done del MVP

El MVP estara listo cuando se cumplan todas estas condiciones:

- [ ] se puedan crear proyectos y endpoints via API
- [ ] los checks se ejecuten de forma automatica
- [ ] las metricas basicas se persistan correctamente
- [ ] exista al menos un endpoint para consultar resultados agregados
- [ ] haya cobertura minima sobre API, modulos y workers
- [ ] el entorno local sea reproducible con instrucciones verificables
