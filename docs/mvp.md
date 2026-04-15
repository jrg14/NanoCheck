# MVP de NanoCheck

## Objetivo

Delimitar una primera version pequena pero util, para evitar que el roadmap crezca mas rapido que la implementacion.

## Alcance incluido

El MVP deberia permitir:

- registrar usuarios
- crear proyectos
- registrar endpoints HTTP
- ejecutar checks periodicos
- guardar metricas crudas
- consultar metricas basicas por endpoint

## Metricas minimas

- tiempo de respuesta medio
- numero de checks ejecutados
- porcentaje de exito
- tasa de error
- disponibilidad en una ventana temporal

## Alcance excluido inicialmente

Estas capacidades pueden esperar a fases posteriores:

- comparativas avanzadas entre ventanas
- deteccion sofisticada de tendencias
- dashboard frontend completo
- websocket en tiempo real
- billing simulado
- uso de `TimescaleDB`

## Criterio de salida del MVP

Se considerara alcanzado cuando:

- exista una API funcional para proyectos y endpoints
- los checks puedan ejecutarse sin intervencion manual
- las metricas basicas puedan consultarse via API
- haya pruebas minimas para flujo feliz y errores principales
- el despliegue local sea reproducible
