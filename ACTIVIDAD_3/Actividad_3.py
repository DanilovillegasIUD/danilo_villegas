
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

file_path1= "data_vinos_2.csv"
review = pd.read_csv(file_path1, sep=';')

print(review.head(10))

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

# Punto 7. Conocer el precio promedios de los vinos.

promedio = round(review2['price'].mean(),3)
resultado_promedio = pd.DataFrame({"Moneda":["$"],"Precio_promedio": [promedio] })
resultado_promedio.to_csv("ACTIVIDAD_3/Punto_7.csv")

print("El precio promedio de los vinos es de: $",promedio)
print("-->> Dataframe del punto 7 con el precio promedio de los vinos, se guardó en .csv con exito en la carpeta Actividad_3")

# Punto 8. Se busca el precio pagado mas alto por un vino

mayor_precio = round(review2['price'].max(),3)
vino_mayor_precio = review2[review2['price'] == mayor_precio]
variedad = vino_mayor_precio['variety'].iloc[0]  # Tomar la primera coincidencia

precio_alto = pd.DataFrame ({"Precio_mas_alto":[mayor_precio], "Variedad": [variedad]})

precio_alto.to_csv("ACTIVIDAD_3/Punto_8.csv")

print(f"El vino de mayor precio pagadp es de ${mayor_precio} y su variedad es: {variedad}.")
print("-->> Dataframe del punto 8 con el precio mas alto pagado por un vino, se guardó en .csv con exito en la carpeta Actividad_3")

# Punto 9. DataFrame de Vinos de California

california = pd.DataFrame(review2[review2['province'] == 'California'])
vinos_california = california.info

vinos_california_dataframe = pd.DataFrame([vinos_california])
vinos_california_dataframe.to_csv("ACTIVIDAD_3/Punto_9.csv")

print("-->> Dataframe del punto 9 con los vinos de california, se guardó en .csv con exito en la carpeta Actividad_3")

# Punto 10. Informacion completa del vino mas caro con idxmax()

max_precio = review2['price'].idxmax()
vino_caro = review2.loc[max_precio]

vino_caro_dataframe = pd.DataFrame([vino_caro])
vino_caro_dataframe.to_csv("ACTIVIDAD_3/Punto_10.csv")

print(vino_caro)
print("-->> Dataframe del punto 10 con la informacion completa del vino mas caro, se guardó en .csv con exito en la carpeta Actividad_3")

# Punto 11. Buscar las variedades de uvas mas comunes en California

uvas_comunes = california['variety'].value_counts()
uvas_comunes1 = pd.DataFrame({"Variedad":uvas_comunes.index, "Cantidad":uvas_comunes.values})

uvas_comunes1.to_csv("ACTIVIDAD_3/Punto_11.csv")

print("las uvas mas comunes en California son:", uvas_comunes)
print("-->> Dataframe del punto 11 con los tipos de uva mas comunes en california, se guardó en .csv con exito en la carpeta Actividad_3")

# Punto 12. Sacar DataFrame con los 10 tipos de una mas comunes en california

uvas_comunes = california['variety'].value_counts()
primeras_10 = uvas_comunes1.head(10)

primeras_10.to_csv("ACTIVIDAD_3/Punto_12.csv")

print(uvas_comunes.head(10))
print("-->> Dataframe del punto 12 con los 10 tipos de uva mas comunes en california, se guardó en .csv con exito en la carpeta Actividad_3")






