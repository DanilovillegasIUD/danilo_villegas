
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

print("-->> Dataframe del punto 2 guardado en .csv con exito en carpeta Actividad_3")

# Punto 3. Se muestra el DataFrame con los utensilios de cocina. Se guardan en un archivo .csv

cocina = pd.DataFrame({
    "Utensilio": ["Cuchara", "Tenedor", "Cuchillo", "Plato"],
    "Cantidad": [3, 2, 4, 5],
    "Medida": ["unidades", "unidades", "unidades", "unidades"]
})

print (cocina)
cocina.to_csv("ACTIVIDAD_3/Punto_3.csv")

print("-->> Dataframe del punto 3 guardado en .csv con exito en carpeta Actividad_3")

# Punto 4. se descarga el dataset "wine review" desde kaggle, guardandolo en el entorno de trabajo, para cargarlo
# en un nuevo DataFrame. Se guardan en un archivo .csv

file_path1= "data_vinos.csv"
review = pd.read_csv(file_path1)
print(review.head(20))

review.to_csv("ACTIVIDAD_3/Punto_4_review.csv")
review.to_csv("Punto_4_review.csv")










