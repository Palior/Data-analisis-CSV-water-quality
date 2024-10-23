# Análisis de Calidad del Agua por Regiones

Este proyecto es un programa escrito en Python que realiza el análisis de la calidad del agua por regiones, utilizando datos de muestras de pozos almacenados en un archivo CSV. El programa genera gráficos relacionados con la calidad del agua potable y no potable, según las características analizadas.

## Autor
- Pablo Lizama

## Versión
- Python 3.7.1

## Descripción

El programa analiza la calidad del agua en base a distintos parámetros como:
- Turbiedad
- Desinfección
- Microbiología

A partir de los resultados, clasifica los pozos en dos categorías:
1. **Pozos Potables**
2. **Pozos No Potables**

### Entrada
- **Archivo CSV**: El programa requiere un archivo de entrada en formato CSV que contiene datos de muestras de pozos.
  
  Los datos deben estar organizados con las siguientes columnas:
  - Columna 1: Región
  - Columna 2: Pozo
  - Columna 3: Cantidad de Muestras
  - Columna 4: Turbiedad (NTU)
  - Columna 5: Desinfección (mg/L)
  - Columna 6: Microbiología (col/100ml)

### Salida
- El programa generará una lista de pozos que cumplen con los requisitos de agua potable y otra lista de pozos que no cumplen.
- También se realizarán gráficas en base a los resultados obtenidos.

## Estructura del Proyecto

El programa se organiza en tres bloques principales:

1. **Definición de Funciones**: Contiene funciones para:
   - Leer y procesar el archivo CSV.
   - Ordenar los datos por pozo y región.
   - Analizar los parámetros de turbiedad, desinfección y microbiología.
   
2. **Bloque Principal**: Ejecuta las funciones, realiza el análisis completo de los datos y devuelve los resultados.

3. **Funciones Principales**:
   - `leerArchivo(ubicacion)`: Lee el archivo CSV y devuelve los datos como lista.
   - `ordenarPorPozo(listaDeListas)`: Ordena los datos por pozo.
   - `ordenarPorRegion(listaOrdenada)`: Ordena los datos por región.
   - `analizarTurbiedad(listaOrdenada2, listaMuestras)`: Analiza la turbiedad del agua.
   - `analizarDesinfeccion(listaOrdenada2, listaMuestras)`: Analiza los niveles de desinfección.
   - `analizarMicrobiologico(listaOrdenada2, listaMuestras)`: Analiza los parámetros microbiológicos.
   - `listaDefinitiva(listaTurbiedad, listaDesinfeccion, listaMicrobiologico)`: Genera la lista final de pozos potables y no potables.
