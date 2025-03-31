
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


