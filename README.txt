Water Quality Analysis by Region
This project is a Python program that performs a regional analysis of water quality using well sample data stored in a CSV file. The program generates graphs related to the quality of potable and non-potable water based on the analyzed characteristics.

Description
The program analyzes water quality based on various parameters, such as:

Turbidity
Disinfection
Microbiology
Based on the results, it classifies the wells into two categories:

Potable Wells
Non-Potable Wells
Input
CSV File: The program requires an input file in CSV format that contains data on well samples.

The data should be organized with the following columns:

Column 1: Region
Column 2: Well
Column 3: Number of Samples
Column 4: Turbidity (NTU)
Column 5: Disinfection (mg/L)
Column 6: Microbiology (col/100ml)
Output
The program will generate a list of wells that meet potable water standards and another list of wells that do not.
It will also create graphs based on the obtained results.
Project Structure
The program is organized into three main sections:

Function Definitions: Contains functions to:

Read and process the CSV file.
Sort the data by well and region.
Analyze turbidity, disinfection, and microbiology parameters.
Main Block: Executes the functions, performs a complete analysis of the data, and returns the results.

Main Functions:

leerArchivo(ubicacion): Reads the CSV file and returns the data as a list.
ordenarPorPozo(listaDeListas): Sorts the data by well.
ordenarPorRegion(listaOrdenada): Sorts the data by region.
analizarTurbiedad(listaOrdenada2, listaMuestras): Analyzes water turbidity.
analizarDesinfeccion(listaOrdenada2, listaMuestras): Analyzes disinfection levels.
analizarMicrobiologico(listaOrdenada2, listaMuestras): Analyzes microbiological parameters.
listaDefinitiva(listaTurbiedad, listaDesinfeccion, listaMicrobiologico): Generates the final list of potable and non-potable wells.