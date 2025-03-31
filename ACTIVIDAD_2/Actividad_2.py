# -*- coding: utf-8 -*-

# Evidencia de aprendizaje Numero 2

# Elaborado por Danilo Villegas Restrepo y Mauricio Alejandro Gonzalez Guerra- IUDIGITAL

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Punto 1. Genera un array con valores de 10 a 29
arr1 = np.arange(10, 30)
print(arr1)

# Punto 2. Suma de todos los elementos en un array 10x10 de unos
arr2 = np.ones((10, 10))
print(arr2.sum())

# Punto 3. Producto elemento a elemento de dos arrays aleatorios de tamaño 5
arr3_a = np.random.randint(1, 11, 5)
arr3_b = np.random.randint(1, 11, 5)
print(arr3_a * arr3_b)

# Punto 4: Crea una matriz de 4x4, donde cada elemento es igual a i+j (con i y j siendo el índice de fila y columna, respectivamente) y calcula su inversa.

# Crear la matriz de 4x4 con elementos i + j
n = 4
matriz = np.fromfunction(lambda i, j: i + j, (n, n), dtype=int)

# Convertir la matriz a tipo float para evitar errores numéricos
matriz = matriz.astype(float)

# Calcular la inversa de la matriz usando pseudo-inversa en caso de que no sea invertible
matriz_inversa = np.linalg.pinv(matriz)

print("Matriz Original:")
print(matriz)
print("\nMatriz Inversa:")
print(matriz_inversa)

# Punto 5: Encuentra los valores máximo y mínimo en un array de 100 elementos aleatorios y muestra sus índices

# Generar un array de 100 números aleatorios entre 0 y 100
data = np.random.randint(0, 100, 100)

# Encontrar el índice del valor máximo y mínimo
max_idx = np.argmax(data)
min_idx = np.argmin(data)

# Obtener los valores máximo y mínimo
max_val = data[max_idx]
min_val = data[min_idx]

# Mostrar los resultados
print(f"Valor máximo: {max_val} en el índice {max_idx}")
print(f"Valor mínimo: {min_val} en el índice {min_idx}")

# Punto 6: Crea un array de tamaño 3x1 y uno de 1x3, y súmalos utilizando broadcasting para obtener un array de 3x3

# Crear arrays
array_3x1 = np.array([[1], [2], [3]])  # Matriz columna de 3x1
array_1x3 = np.array([[4, 5, 6]])  # Matriz fila de 1x3

# Sumar usando broadcasting
resultado = array_3x1 + array_1x3

# Mostrar los resultados
print("Array 3x1:")
print(array_3x1)
print("\nArray 1x3:")
print(array_1x3)
print("\nResultado de la suma:")
print(resultado)

# Punto 7: De una matriz 5x5, extrae una submatriz 2x2 que comience en la segunda fila y columna.

# Crear una matriz 5x5 con valores aleatorios entre 0 y 9
matriz_5x5 = np.random.randint(0, 10, (5, 5))

# Extraer la submatriz 2x2 desde la segunda fila y segunda columna
submatriz_2x2 = matriz_5x5[1:3, 1:3]

# Mostrar los resultados
print("Matriz 5x5:")
print(matriz_5x5)
print("\nSubmatriz 2x2 extraída:")
print(submatriz_2x2)

# Punto 8 : Crea un array de ceros de tamaño 10 y usa indexado para cambiar el valor de los elementos en el rango de índices 3 a 6 a 5.

# Crear un array de ceros de tamaño 10
array_ceros = np.zeros(10, dtype=int)

# Modificar los valores en el rango de índices 3 a 6
array_ceros[3:7] = 5

# Mostrar el resultado
print("Array modificado:")
print(array_ceros)

# Punto 9: Dada una matriz de 3x3, invierte el orden de sus filas.

# Crear una matriz 3x3 con valores aleatorios entre 0 y 9
matriz_3x3 = np.random.randint(0, 10, (3, 3))

# Invertir el orden de las filas
matriz_invertida = matriz_3x3[::-1]

# Mostrar los resultados
print("Matriz original:")
print(matriz_3x3)
print("\nMatriz con filas invertidas:")
print(matriz_invertida)

# Punto 10: Dado un array de números aleatorios de tamaño 10, selecciona y muestra solo aquellos que sean mayores a 5.

# Crear un array de 10 números aleatorios entre 0 y 10
array_aleatorio = np.random.randint(0, 10, 10)

# Seleccionar los elementos mayores a 5
mayores_a_5 = array_aleatorio[array_aleatorio > 5]

# Mostrar los resultados
print("Array original:")
print(array_aleatorio)
print("\nElementos mayores a 5:")
print(mayores_a_5)

# Punto 11: Genera dos arrays de tamaño 100 con números aleatorios y crea un gráfico de dispersión.

# Crear dos arrays de números aleatorios de tamaño 100
x = np.random.rand(100)
y = np.random.rand(100)

# Crear gráfico de dispersión
plt.scatter(x, y, alpha=0.7, edgecolors='k')
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráfico de Dispersión")
plt.grid(True)

# Generar el Grafico
plt.savefig("Gráfico de Dispersión.png")
print("Grafica generada")

# Punto 12: Genera un gráfico de dispersión de las variables x y y = sin(x) + ruido Gaussiano.
# Donde x es un array con números entre -2π y 2π. También grafica y = sin(x) en el mismo plot.

# Generar valores de x entre -2π y 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)

# Calcular y = sin(x) y agregar ruido Gaussiano
ruido = np.random.normal(0, 0.2, x.shape)
y_ruidoso = np.sin(x) + ruido

y_sin = np.sin(x)  # Función seno sin ruido

# Crear gráfico de dispersión con la función seno
plt.scatter(x, y_ruidoso, alpha=0.5, label='y = sin(x) + ruido', color='blue')
plt.plot(x, y_sin, label='y = sin(x)', color='red', linewidth=2)

# Configuración del gráfico
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gráfico de Dispersión con Ruido y Función Seno")
plt.legend()
plt.grid(True)

# Generar el Grafico
plt.savefig("Gráfico de Dispersión con Ruido y Función Seno.png")
print("Grafica generada")

# Punto 13: Utiliza la función np.meshgrid para crear una cuadrícula y luego aplica la función
# z = np.cos(x) + np.sin(y) para generar y mostrar un gráfico de contorno.

# Definir el rango de valores para x e y
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.linspace(-2 * np.pi, 2 * np.pi, 100)

# Crear la cuadrícula con np.meshgrid
X, Y = np.meshgrid(x, y)

# Calcular Z usando la función dada
Z = np.cos(X) + np.sin(Y)

# Crear el gráfico de contorno
plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(label='Valor de Z')
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráfico de Contorno de z = cos(x) + sin(y)")

# Generar el Grafico
plt.savefig("Gráfico de Contorno de z = cos(x) + sin(y).png")
print("Grafica generada")

# Punto 14: Crea un gráfico de dispersión con 1000 puntos aleatorios y utiliza la densidad de estos puntos
# para ajustar el color de cada punto.

# Generar 1000 puntos aleatorios
x = np.random.randn(1000)
y = np.random.randn(1000)

# Calcular la densidad de los puntos
xy = np.vstack([x, y])
densidad = gaussian_kde(xy)(xy)

# Crear gráfico de dispersión con colores basados en la densidad
plt.scatter(x, y, c=densidad, cmap='plasma', edgecolor='k', alpha=0.7)
plt.colorbar(label='Densidad')
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráfico de Dispersión con Densidad de Puntos")

# Generar el Grafico
plt.savefig("Gráfico de Dispersión con Densidad de Puntos.png")
print("Grafica generada")

# Punto 15: A partir de la misma función del ejercicio anterior, genera un gráfico de contorno lleno.

# Generar 1000 puntos aleatorios
x = np.random.randn(1000)
y = np.random.randn(1000)

# Calcular la densidad de los puntos
xy = np.vstack([x, y])
densidad = gaussian_kde(xy)(xy)

# Crear un gráfico de contorno lleno basado en la densidad
plt.tricontourf(x, y, densidad, levels=20, cmap='plasma')
plt.colorbar(label='Densidad')
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráfico de Contorno Lleno de la Densidad de Puntos")

# Generar el Grafico
plt.savefig("Gráfico de Contorno Lleno de la Densidad de Puntos.png")
print("Grafica generada")

# Punto 16: Añade etiquetas para los ejes y un título al gráfico de dispersión del ejercicio 12,
# y crea leyendas con código LaTeX.

# Generar 1000 puntos aleatorios
x = np.random.randn(1000)
y = np.random.randn(1000)

# Calcular la densidad de los puntos
xy = np.vstack([x, y])
densidad = gaussian_kde(xy)(xy)

# Crear gráfico de dispersión con etiquetas y leyendas en LaTeX
plt.scatter(x, y, c=densidad, cmap='plasma', edgecolor='k', alpha=0.7, label=r'$Datos\ aleatorios$')
plt.colorbar(label=r'$Densidad$')
plt.xlabel(r'$Eje\ X$')
plt.ylabel(r'$Eje\ Y$')
plt.title(r'$Gráfico\ de\ Dispersión$')
plt.legend()

# Generar el Grafico
plt.savefig("leyendas con código LaTeX.png")
print("Grafica generada")

# Punto 17: Crea un histograma a partir de un array de 1000 números aleatorios generados con una distribución normal.

# Generar 1000 números aleatorios con distribución normal
datos = np.random.randn(1000)

# Crear el histograma
plt.hist(datos, bins=30, density=True, alpha=0.6, color='b', edgecolor='black')

# Etiquetas y título
plt.xlabel("Valor")
plt.ylabel("Densidad")
plt.title("Histograma de una Distribución Normal")

# Generar el gráfico
plt.savefig("Histograma de una Distribución Normal.png")
print("Grafica generada")

# Punto 18: Genera dos sets de datos con distribuciones normales diferentes y muéstralos en el mismo histograma.

# Generar dos conjuntos de datos con distribuciones normales diferentes
datos1 = np.random.normal(loc=0, scale=1, size=1000)  # Media 0, desviación estándar 1
datos2 = np.random.normal(loc=3, scale=1.5, size=1000)  # Media 3, desviación estándar 1.5

# Crear el histograma
plt.hist(datos1, bins=30, alpha=0.6, color='b', edgecolor='black', label='Media=0, Std=1')
plt.hist(datos2, bins=30, alpha=0.6, color='r', edgecolor='black', label='Media=3, Std=1.5')

# Etiquetas y título
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.title("Histogramas de Distribuciones Normales Diferentes")
plt.legend()

# Generar el gráfico
plt.savefig("Histogramas de Distribuciones Normales Diferentes.png")
print("Grafica generada")

# Punto 19: Experimenta con diferentes valores de bins (por ejemplo, 10, 30, 50) en un histograma y observa cómo cambia la representación.

# Generar dos conjuntos de datos con distribuciones normales diferentes
datos1 = np.random.normal(loc=0, scale=1, size=1000)  # Media 0, desviación estándar 1
datos2 = np.random.normal(loc=3, scale=1.5, size=1000)  # Media 3, desviación estándar 1.5

# Definir diferentes valores de bins
bins_values = [10, 30, 50]

# Crear subgráficos para diferentes valores de bins
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for ax, bins in zip(axes, bins_values):
    ax.hist(datos1, bins=bins, alpha=0.6, color='b', edgecolor='black', label='Media=0, Std=1')
    ax.hist(datos2, bins=bins, alpha=0.6, color='r', edgecolor='black', label='Media=3, Std=1.5')
    ax.set_xlabel("Valor")
    ax.set_ylabel("Frecuencia")
    ax.set_title(f"Histograma con {bins} bins")
    ax.legend()

# Ajustar el diseño y generar el gráfico
plt.tight_layout()
plt.savefig("Valores de bins punto 19.png")
print("Grafica generada")

# Punto 20: Experimenta con diferentes valores de bins (por ejemplo, 10, 30, 50) en un histograma y observa cómo cambia la representación.

# Generar dos conjuntos de datos con distribuciones normales diferentes
datos1 = np.random.normal(loc=0, scale=1, size=1000)  # Media 0, desviación estándar 1
datos2 = np.random.normal(loc=3, scale=1.5, size=1000)  # Media 3, desviación estándar 1.5

# Definir diferentes valores de bins
bins_values = [10, 30, 50]

# Crear subgráficos para diferentes valores de bins
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for ax, bins in zip(axes, bins_values):
    ax.hist(datos1, bins=bins, alpha=0.6, color='b', edgecolor='black', label='Media=0, Std=1')
    ax.hist(datos2, bins=bins, alpha=0.6, color='r', edgecolor='black', label='Media=3, Std=1.5')

    # Calcular y agregar líneas verticales para la media
    media1 = np.mean(datos1)
    media2 = np.mean(datos2)
    ax.axvline(media1, color='b', linestyle='dashed', linewidth=2, label='Media datos1')
    ax.axvline(media2, color='r', linestyle='dashed', linewidth=2, label='Media datos2')

    ax.set_xlabel("Valor")
    ax.set_ylabel("Frecuencia")
    ax.set_title(f"Histograma con {bins} bins")
    ax.legend()

# Ajustar el diseño y generar el gráfico
plt.tight_layout()
plt.savefig("Valores de bins punto 20.png")
print("Grafica generada")

# Punto 21: Crea histogramas superpuestos para los dos sets de datos del ejercicio 17, usando colores y transparencias diferentes para distinguirlos.

# Generar dos conjuntos de datos con distribuciones normales diferentes
datos1 = np.random.normal(loc=0, scale=1, size=1000)  # Media 0, desviación estándar 1
datos2 = np.random.normal(loc=3, scale=1.5, size=1000)  # Media 3, desviación estándar 1.5

# Crear histograma superpuesto
plt.figure(figsize=(8, 6))
plt.hist(datos1, bins=30, alpha=0.5, color='blue', edgecolor='black', label='Media=0, Std=1')
plt.hist(datos2, bins=30, alpha=0.5, color='red', edgecolor='black', label='Media=3, Std=1.5')

# Calcular y agregar líneas verticales para la media
media1 = np.mean(datos1)
media2 = np.mean(datos2)
plt.axvline(media1, color='blue', linestyle='dashed', linewidth=2, label='Media datos1')
plt.axvline(media2, color='red', linestyle='dashed', linewidth=2, label='Media datos2')

# Etiquetas y título
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.title("Histogramas Superpuestos de Distribuciones Normales")
plt.legend()

# Generar el gráfico
plt.savefig("Histogramas Superpuestos de Distribuciones Normales punto 21.png")
print("Grafica generada")