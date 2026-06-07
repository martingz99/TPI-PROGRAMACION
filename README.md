# TPI-PROGRAMACION
# Sistema de Gestión de Datos de Países

# Descripción

Este proyecto fue desarrollado como Trabajo Práctico Integrador de la materia Programación 1.

El sistema permite gestionar información de países utilizando Python, listas, diccionarios, funciones y archivos CSV. Desde un menú en consola, el usuario puede cargar, buscar, filtrar, ordenar y analizar datos de países.

# Funcionalidades principales

- Cargar datos desde un archivo CSV.
- Agregar nuevos países.
- Actualizar población y superficie de un país.
- Buscar países por nombre.
- Filtrar países por continente.
- Filtrar países por rango de población.
- Filtrar países por rango de superficie.
- Ordenar países por nombre, población o superficie.
- Mostrar estadísticas generales.
- Guardar los cambios en el archivo CSV.

# Estructura de datos utilizada

Cada país se representa mediante un diccionario con los siguientes campos:

```python
{
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "America"
}
