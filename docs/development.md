# Desarrollo

## Situacion del repositorio

El repositorio contiene por ahora documentacion y configuracion basica de Python. No hay una aplicacion ejecutable ni estructura de paquetes implementada.

## Entorno local

Preparacion recomendada:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
```

## Herramientas definidas

- `FastAPI` como framework objetivo para la API.
- `Pydantic` para validacion.
- `SQLAlchemy` para acceso a datos.
- `pytest` para pruebas.
- `ruff` para lint y formato.
- `pre-commit` para automatizar checks locales.

## Convenciones propuestas

- Organizar el codigo por modulos de dominio como `auth`, `projects`, `endpoints`, `metrics` y `alerts`.
- Mantener dentro de cada modulo sus contratos HTTP, esquemas, logica y persistencia.
- Documentar decisiones relevantes en `docs/decisions/`.
- Actualizar el roadmap cuando una fase empiece o termine.
- No marcar una decision como implementada hasta que exista codigo y verificacion asociada.

## Huecos por cubrir antes de implementar

- Crear estructura base de `app/` y `modules/`.
- Definir variables de entorno y publicar un `.env.example`.
- Elegir estrategia de configuracion y settings.
- Preparar persistencia real con PostgreSQL.
- Decidir si el MVP necesita colas desde el primer dia o puede arrancar con una version mas simple.

## Verificacion minima esperada cuando haya codigo

- tests unitarios por modulo
- tests de API para endpoints principales
- mocks de integracion HTTP para checks
- checks automaticos de lint y formato
