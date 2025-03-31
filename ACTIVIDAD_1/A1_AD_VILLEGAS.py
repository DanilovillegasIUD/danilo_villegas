# Evidencia de aprendizaje Clases, Objetos y archivos de datos en Python

# Danilo Villegas Restrepo - IUDIGITAL

import numpy as np
import matplotlib.pyplot as plt
import csv
import json
import requests

# Punto 1 Crear una IU que grafique un número arbitrario de polinomios de la forma ax^n donde 𝑎 y n son parámetros.

polinomios = [(2, 2), (-1, 3), (0.5, 4)] 

x = np.linspace(-10, 10, 100)

plt.figure()
for a, n in polinomios:
    y = a * (x ** n)
    plt.plot(x, y, label=f"{a}x^{n}")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Gráfica de Polinomios")
plt.grid()
plt.savefig("grafico_polinomios.png")
print("Grafica generada")

# Punto 2 Escritura de Datos en un Archivo CSV. Escribe un script que guarde una lista de listas en un archivo llamado frutas.csv en tu directorio principal

# Se crea una lista con los datos de las frutas, se crea un objeto donde guardar la lista con una terminacion csv
frutas = [
    ["Manzana", "Roja", "Dulce"],
    ["Platano", "Amarillo", "Dulce"],
    ["Lima", "Verde", "Acida"]
]
archivo_csv = "frutas.csv"
# Aca se crea el archivo csv donde se guarde la lista con el nombre asignado, el modo w es para escribir de "Write" si fuese modo R 
# lo que haria es leer el archivo, tambien se le crean las variables con las que se pueden asociar los datos de la lista.
with open(archivo_csv, mode="w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)  
    escritor.writerow(["Fruta", "Color", "Sabor"])  
    escritor.writerows(frutas)  

# Aca se imprime el mensaje que el archivo fue guardado correctamente

print(f"Archivo {archivo_csv} guardado.")


# Punto 3 Lectura de Datos de un Archivo CSV, Escribe un script que lea los datos del archivo frutas.csv creado en el Reto 1 y los almacene en una lista de listas llamada datos_frutas.

archivo_csv = "frutas.csv"

datos_frutas = []

# Caso contrario al anterior y como se menciono, al usar el modo r, se pasa a leer los datos dentro el archivo .csv
# tambien se le asigna un objeto donde se quedan consigandos los datos cargados para finalmente imprimirlos
with open(archivo_csv, mode="r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo) 
    next(lector)  
    for fila in lector:
        datos_frutas.append(fila)  

print("Datos de frutas:")
for fruta in datos_frutas:
    print(fruta)

# Punto 4 Usa la plataforma JSONPlaceholder y practica lo que aprendiste en la Actividad 2 para inventar tu propia pipeline de acciones en python sobre el conjunto de datos de tu preferencia en la plataforma

# Aca se crea un objeto con una url donde reposan los datos a trabajar

url = "https://jsonplaceholder.typicode.com/comments"

# a continuacion esta la configuracion de la solicitud para el uso de los datos, su tipo de respuesta y el mensaje 
# por posibles errores

try:
    respuesta_api = requests.get(url)
    respuesta_api.raise_for_status()
    lista_comentarios = respuesta_api.json()
except requests.exceptions.RequestException as e:
    print(f"Error al obtener datos de la API: {e}")
    exit()

# aca la intension es identificar la cantidad de usuarios se registran mediante los comentarios realizados 
# dado que existe la posiblidad de que un solo usuario comente mas de una vez, esto lo que hace es identificarlos y contarlos


usuarios_unicos = set(comentario["email"] for comentario in lista_comentarios)
cantidad_usuarios_unicos = len(usuarios_unicos)

archivo_csv = "usuarios_unicos.csv"

# Finalmente crea un archivo csv para guardar los correos de los usuarios unicos.
try:
    with open(archivo_csv, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Email"])
        for email in usuarios_unicos:
            writer.writerow([email])
    print(f"Archivo {archivo_csv} guardado.")
except IOError as e:
    print(f"Error al escribir el archivo CSV: {e}")
    exit()

# aca imprime el resultado del conteo
print(f"Se encontraron {cantidad_usuarios_unicos} usuarios unicos en los comentarios.")
