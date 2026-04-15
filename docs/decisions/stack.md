# Decisiones de stack

Este documento registra decisiones tecnicas con su estado actual. No todas estan implementadas; algunas siguen siendo parte del diseno objetivo.

## ADR-001 - FastAPI como framework principal

- Estado: aceptada
- Alcance: API REST

### Decision

Usar `FastAPI` como framework principal para la capa HTTP del backend.

### Motivos

- Buen rendimiento sobre ASGI.
- Tipado y validacion integrados con `Pydantic`.
- Documentacion OpenAPI automatica.
- Buena ergonomia para servicios backend pequenos y medianos.

### Alternativas consideradas

- `Django REST Framework`: mas opinionated, pero mas pesado para un backend centrado en API.
- `Flask`: mas flexible, pero con mas trabajo de integracion.

### Consecuencias

- Habra que tomar decisiones explicitas sobre la organizacion modular del codigo.
- La documentacion tecnica debe dejar claro el patron elegido.

## ADR-002 - SQLAlchemy como capa de acceso a datos

- Estado: aceptada
- Alcance: persistencia

### Decision

Usar `SQLAlchemy` como herramienta principal para modelado y acceso a datos.

### Motivos

- Flexibilidad para consultas complejas.
- Compatibilidad con una organizacion por modulos de dominio.
- Ecosistema maduro.

### Alternativas consideradas

- `SQLModel`: menor boilerplate, pero menos control y menos conveniente si el dominio crece.

### Consecuencias

- El codigo sera algo mas verboso.
- Conviene definir pronto una estrategia de sesiones y transacciones.

## ADR-003 - PostgreSQL como base de datos objetivo

- Estado: propuesta
- Alcance: almacenamiento principal

### Decision

Usar `PostgreSQL` como base de datos principal cuando se implemente la capa de persistencia real.

### Motivos

- Buen soporte para consultas analiticas.
- Solucion solida y conocida para produccion.
- Permite evolucionar hacia agregaciones y optimizaciones mas avanzadas.

### Alternativas consideradas

- `SQLite` para prototipos locales.
- Bases time-series especializadas desde el inicio.

### Consecuencias

- Requerira configuracion de entorno y migraciones.
- Convendra definir indices desde fases tempranas.

## ADR-004 - Celery + Redis para trabajos en background

- Estado: propuesta
- Alcance: checks programados y agregaciones

### Decision

Adoptar `Celery` para ejecucion de tareas asicronas y `Redis` como broker en una fase posterior.

### Motivos

- Permite paralelismo, reintentos y scheduling.
- Encaja con una arquitectura con workers desacoplados.
- Facilita escalar el procesamiento independientemente de la API.

### Alternativas consideradas

- `FastAPI BackgroundTasks`: valida para tareas pequenas, pero insuficiente para un sistema de monitorizacion sostenido.
- Un cron externo simple: mas facil al principio, pero menos flexible.

### Consecuencias

- Aumenta el coste operativo del proyecto.
- Puede no ser necesario en la primera iteracion del MVP si el volumen es bajo.

## ADR-005 - Metricas crudas mas agregaciones

- Estado: propuesta
- Alcance: almacenamiento analitico

### Decision

Persistir resultados crudos de monitorizacion y generar agregados por ventana temporal para lectura.

### Motivos

- Evita calculos pesados en tiempo real.
- Permite balancear precision historica con velocidad de consulta.
- Encaja bien con metricas como `p95`, `p99` o `uptime`.

### Alternativas consideradas

- Calculo bajo demanda en cada consulta.
- Almacenar solo agregados.

### Consecuencias

- Haran falta jobs de agregacion y reglas de retencion.
- Debe definirse bien la granularidad del MVP.

## ADR-006 - TimescaleDB solo si el volumen lo exige

- Estado: abierta
- Alcance: optimizacion futura

### Decision

No adoptar `TimescaleDB` desde el inicio. Revaluarlo cuando exista evidencia de necesidad por volumen o coste de consulta.

### Motivos

- Reduce complejidad en el arranque.
- Mantiene el MVP sobre una base mas simple.

### Consecuencias

- Algunas optimizaciones avanzadas quedaran pospuestas.
- La arquitectura debe evitar acoplamientos tempranos a extensiones especificas.
