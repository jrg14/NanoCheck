# Arquitectura de NanoCheck

## Objetivo

NanoCheck busca monitorizar endpoints HTTP de forma periodica, persistir resultados historicos y exponer metricas agregadas para consumo por clientes o paneles de observabilidad.

## Estado actual

Esta arquitectura describe el sistema objetivo. A fecha de hoy el repositorio no implementa aun estos componentes, por lo que debe leerse como una referencia de diseno y no como una descripcion del runtime existente.

## Componentes previstos

### API

Responsable de:

- autenticacion y autorizacion
- CRUD de proyectos y endpoints
- consulta de metricas e insights
- configuracion de reglas de alerta

### Scheduler

Responsable de disparar checks periodicos sobre los endpoints registrados. Puede implementarse con `Celery Beat` u otra estrategia equivalente.

### Workers

Responsables de:

- ejecutar requests HTTP
- medir tiempos y capturar resultados
- clasificar exito o fallo
- persistir metricas crudas
- lanzar procesos de agregacion

### Base de datos

Responsable de almacenar:

- entidades de negocio (`User`, `Project`, `Endpoint`)
- eventos de monitorizacion (`Metric`)
- tablas agregadas para consulta rapida
- reglas y eventos de alerta

## Organizacion interna del codigo

La organizacion recomendada para NanoCheck es por modulos de dominio, no por capas tecnicas globales. En lugar de tener directorios horizontales como `services/` o `repositories/`, cada modulo agrupa sus piezas relacionadas.

Una estructura orientativa podria ser:

```text
app/
|-- core/
|-- modules/
|   |-- auth/
|   |   |-- api.py
|   |   |-- schemas.py
|   |   |-- models.py
|   |   `-- logic.py
|   |-- projects/
|   |-- endpoints/
|   |-- metrics/
|   `-- alerts/
`-- workers/
```

Cada modulo puede contener su propia API, esquemas, modelos, casos de uso y acceso a datos, manteniendo las dependencias lo mas cerca posible del dominio al que sirven.

## Flujo principal

1. Un usuario registra un proyecto y uno o varios endpoints.
2. El scheduler programa checks segun la frecuencia definida.
3. Un worker ejecuta el check y persiste el resultado crudo.
4. Procesos de agregacion calculan ventanas horarias o diarias.
5. La API expone metricas, tendencias y alertas sobre esos datos.

## Principios de diseno

- Organizacion por modulos de dominio con limites claros.
- Cohesion alta dentro de cada modulo y bajo acoplamiento entre modulos.
- Procesamiento asincrono para checks y agregaciones.
- Lectura optimizada mediante datos agregados.
- Evolucion incremental: primero MVP funcional, despues escalado.

## Riesgos y decisiones abiertas

- `Celery + Redis` anade complejidad operativa si el MVP sigue siendo pequeno.
- `TimescaleDB` puede ser innecesario en una primera version.
- La definicion exacta de `success`, `failure` y `uptime` debe fijarse pronto porque condiciona metricas y alertas.
- La estrategia de retencion de metricas crudas aun no esta definida.
