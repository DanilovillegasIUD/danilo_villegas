import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import csv
import json
import requests


# Punto 1

# La siguiente clase agrupa las funciones que generan una ventana emergente con 2 botones y los ubica en la ventana

class Graficador:
    def __init__(self, root):
        self.root = root
        self.root.title("Graficador de Polinomios")
        self.polinomios = []  

        
        tk.Label(root, text="Parametro (a):").pack()
        self.a_entry = tk.Entry(root)
        self.a_entry.pack()

        tk.Label(root, text="Exponente (n):").pack()
        self.n_entry = tk.Entry(root)
        self.n_entry.pack()

        
        tk.Button(root, text="Agrega un polinomio", command=self.agregar_polinomio).pack()
        tk.Button(root, text="Graficar", command=self.graficar).pack()

# En la siguiente funcion se piden los valores de a y n para guardarlos en un polinomio despues de pulsar el boton dado
# para luego crear la funcion del tipo ax^n
    def agregar_polinomio(self):
        """Agrega un polinomio a la lista."""
        try:
            a = float(self.a_entry.get())
            n = int(self.n_entry.get())
            self.polinomios.append((a, n))
            print(f"Agregado: {a}x^{n}")
        except ValueError:
            print("Error: Ingresaste un valor no numerico, solo numeros por favor.")

# en la siguiente funcion le crea la accion de graficar los polinomios en un plano xy en un rango de x de -10 a 10 
# y una amplitud en y de 100.

    def graficar(self):
        """Dibuja los polinomios en un gráfico."""
        x = np.linspace(-10, 10, 100)
        for a, n in self.polinomios:
            y = a * (x ** n)
            plt.plot(x, y, label=f"{a}x^{n}")

        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.show()

# A continuacion llama las funciones para abrir la ventana emergente
root = tk.Tk()
app = Graficador(root)
root.mainloop()

# Punto 2

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


# Punto 3

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

# Punto 4

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