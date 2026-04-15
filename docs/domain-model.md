# Modelo de dominio

## Objetivo

Definir las entidades principales del sistema antes de construir la API y la persistencia.

## Entidades previstas

### User

Representa al propietario de proyectos y configuraciones.

Campos orientativos:

- `id`
- `email`
- `password_hash`
- `created_at`

### Project

Agrupa endpoints bajo un mismo contexto funcional o de negocio.

Campos orientativos:

- `id`
- `user_id`
- `name`
- `description`
- `created_at`

### Endpoint

Recurso monitorizado por el sistema.

Campos orientativos:

- `id`
- `project_id`
- `name`
- `url`
- `method`
- `check_interval_seconds`
- `timeout_seconds`
- `expected_status_code`
- `is_active`

### Metric

Resultado crudo de una ejecucion de monitorizacion.

Campos orientativos:

- `id`
- `endpoint_id`
- `checked_at`
- `response_time_ms`
- `status_code`
- `is_success`
- `error_type`
- `error_message`

### AggregatedMetric

Vista materializada o tabla agregada para consultas por ventana temporal.

Campos orientativos:

- `endpoint_id`
- `bucket_start`
- `bucket_granularity`
- `request_count`
- `success_count`
- `error_count`
- `avg_latency_ms`
- `p95_latency_ms`
- `p99_latency_ms`

### AlertRule

Configuracion declarativa para disparar alertas.

Campos orientativos:

- `id`
- `project_id`
- `metric_type`
- `threshold`
- `window`
- `cooldown_seconds`
- `is_active`

### AlertEvent

Evento generado cuando una regla detecta una condicion de riesgo.

Campos orientativos:

- `id`
- `alert_rule_id`
- `endpoint_id`
- `triggered_at`
- `status`
- `payload`

## Relaciones

- Un `User` tiene muchos `Project`.
- Un `Project` tiene muchos `Endpoint`.
- Un `Endpoint` tiene muchas `Metric`.
- Un `Project` tiene muchas `AlertRule`.
- Una `AlertRule` puede generar muchos `AlertEvent`.

## Notas abiertas

- Falta decidir si `expected_status_code` sera unico o un conjunto de codigos validos.
- Falta decidir si las alertas se configuran por proyecto o por endpoint.
- Falta decidir la granularidad exacta de las agregaciones del MVP.
