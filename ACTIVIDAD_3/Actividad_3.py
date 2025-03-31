
#**********   Evidencia de Aprendizaje Numero 3 -IUDIGITAL DE ANTOQUIA  **************

# Realizado por: DANILO VILLEGAS RESTREPO y MAURICIO GONZALEZ GUERRA


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import kagglehub
import os

# Punto 1. Se genera DataFrame de Frutas y se guardan en un archivo .csv

Datos_frutas = pd.DataFrame({
    "Granadilla": [20, 49],
"Tomates": [50, 100]
                })
print (Datos_frutas)
Datos_frutas.to_csv("ACTIVIDAD_3/Punto_1.csv")

print("-->> Dataframe del punto 1 guardado en .csv con exito en carpeta Actividad_3")

# Punto 2. Se genera DataFrame con las ventas de frutas en año 2021 y 2022. Se guardan en un archivo .csv

Venta_frutas = pd.DataFrame({
    "": ["Ventas2021", "ventas2022"],
    "Granadilla": [20, 49],
"Tomates": [50, 100],
                })
print (Venta_frutas)
Venta_frutas.to_csv("ACTIVIDAD_3/Punto_2.csv")



