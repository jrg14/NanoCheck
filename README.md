# NanoCheck

NanoCheck es un backend orientado a la monitorizacion de endpoints HTTP y al analisis de metricas operativas. El proyecto esta en fase de definicion: hoy el repositorio recoge la direccion tecnica, el alcance del MVP y las decisiones principales de arquitectura, pero todavia no incluye una implementacion funcional de la API ni de los workers.

## Estado actual

- Repositorio inicial con documentacion de producto y arquitectura.
- Base de configuracion Python con `FastAPI`, `Pydantic` y `SQLAlchemy`.
- Roadmap definido para evolucionar hacia una plataforma de monitorizacion.

## Objetivo del proyecto

El objetivo es construir un sistema capaz de:

- registrar endpoints por proyecto
- ejecutar checks periodicos
- almacenar metricas crudas y agregadas
- exponer indicadores como latencia, disponibilidad y tasa de error
- generar insights y alertas a partir de degradaciones observadas

## Stack actual del repositorio

El stack presente en el repositorio a fecha de hoy es:

- API: `FastAPI`
- Modelado y validacion: `Pydantic`
- Acceso a datos: `SQLAlchemy`
- Calidad: `pytest`, `ruff`, `pre-commit`

Tecnologias como `PostgreSQL`, `Redis`, `Celery` o `TimescaleDB` forman parte de la direccion tecnica prevista, pero aun no estan integradas en el codigo de este repositorio.

## Estructura

```text
.
|-- README.md
|-- pyproject.toml
`-- docs/
    |-- README.md
    |-- architecture.md
    |-- development.md
    |-- domain-model.md
    |-- mvp.md
    |-- decisions/
    |   `-- stack.md
    `-- roadmap/
        `-- goals.md
```

## Desarrollo local

El proyecto aun no tiene codigo ejecutable, pero la base de entorno puede prepararse desde ya:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
```

Cuando se implemente la aplicacion, este `README` deberia ampliarse con:

- comando de arranque de la API
- variables de entorno requeridas
- estrategia de migraciones
- ejecucion de tests

## Documentacion

- [Indice de documentacion](docs/README.md)
- [Arquitectura](docs/architecture.md)
- [Decisiones de stack](docs/decisions/stack.md)
- [Roadmap](docs/roadmap/goals.md)
- [Desarrollo](docs/development.md)
- [Modelo de dominio](docs/domain-model.md)
- [Alcance MVP](docs/mvp.md)

