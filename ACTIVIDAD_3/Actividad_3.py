
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

file_path1= "winemag-data-130k-v2.csv"
review = pd.read_csv(file_path1)
print(review.head(20))

review.to_csv("ACTIVIDAD_3/Punto_4_review.csv")
review.to_csv("Punto_4_review.csv")

print("-->> Dataframe del punto 4, extraido de la base de datos de Kaggle guardado en .csv con exito en la carpeta Actividad_3")

# Punto 5. Se muestran las primeras filas del DataFrame generado en el punto anterior. Se guardan en un archivo .csv

file_path2 = "Punto_4_review.csv"
review2 = pd.read_csv(file_path2)
primeras_filas= review2.head(5)
primeras_filas.to_csv("ACTIVIDAD_3/Punto_5_review.csv")

print(review2.head(5))

print("-->> Dataframe del punto 5 con las primeras del DataFrame anterior, se guardó en .csv con exito en la carpeta Actividad_3")


# Punto 6. Se uiliza el metodo .info() y shpe para conocer la cantidad de entradas del dataset de wine review

numero_entradas = review2.shape
entradas_resumen = review.info
resultado = pd.DataFrame({"Numero_entradas (filas, columnas)" : [numero_entradas]})
resultado.to_csv("ACTIVIDAD_3/Punto_6.csv")

resultado2 = pd.DataFrame([entradas_resumen])
resultado2.to_csv("ACTIVIDAD_3/Punto_6_resumen.csv")
print("Se han encontrado un total de entradas de filas y columnas de: ", review.shape)
print("Informacion de los registros:", review.info)

print("-->> Dataframe del punto 6 para averiguar cuántas entradas hay, se guardó en .csv con exito en la carpeta Actividad_3")





