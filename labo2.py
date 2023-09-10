import numpy as np
import pandas as pd

# Crear un arreglo de texto con 6 elementos
arreglo_texto = np.array(["Texto 1", "Texto 2", "Texto 3", "Texto 4", "Texto 5", "Texto 6"])

# Renombrar los índices
nuevos_indices = ["Índice A", "Índice B", "Índice C", "Índice D", "Índice E", "Índice F"]

# Asignar los nuevos índices al arreglo
arreglo_texto = np.array(arreglo_texto)
arreglo_texto = np.column_stack((nuevos_indices, arreglo_texto))

# Imprimir los datos
for fila in arreglo_texto:
    print(fila)

# Crear un diccionario con 3 elementos de texto y sus valores numéricos
datos = {
    "Texto 1": 10,
    "Texto 2": 20,
    "Texto 3": 30
}

# Crear un arreglo de texto con índices y valores numéricos
arreglo_texto = np.array([(clave, valor) for clave, valor in datos.items()])

# Imprimir los datos con un separador
for fila in arreglo_texto:
    print(f"{fila[0]}: {fila[1]}")
    print("-" * 20)

# Generar un arreglo de 10 números aleatorios entre 1 y 100 (puedes ajustar los límites según tu preferencia)
arreglo_numeros = np.random.randint(1, 100, 10)

# Imprimir todos los números
print("Todos los números:")
print(arreglo_numeros)

# Imprimir los primeros 5 números
print("\nLos primeros 5 números:")
print(arreglo_numeros[:5])

# Imprimir los últimos 5 números
print("\nLos últimos 5 números:")
print(arreglo_numeros[5:])

# Imprimir los 2 primeros números
print("\nLos 2 primeros números:")
print(arreglo_numeros[:2])

# Crear un diccionario con datos
datos = {
    'Texto': ["Texto 1", "Texto 2", "Texto 3", "Texto 4", "Texto 5", "Texto 6"],
    'Valor Numerico': [10, 20, 30, 40, 50, 60]
}

# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(datos)

# Cambiar el orden de las columnas
df = df[['Valor Numerico', 'Texto']]

# Imprimir el DataFrame
print(df)


# Leer el archivo CSV usando pandas
data = pd.read_csv('Ventas.csv')

# Imprimir los datos utilizando NumPy
datos_numpy = np.array(data)
print("Datos con NumPy:")
print(datos_numpy)

# Imprimir los datos utilizando pandas
print("\nDatos con pandas:")
print(data)

# Crear el primer DataFrame
data1 = {
    'Texto1': ["A", "B", "C", "D", "E", "F"],
    'Valor1': [10, 20, 30, 40, 50, 60]
}
df1 = pd.DataFrame(data1)

# Crear el segundo DataFrame
data2 = {
    'Texto2': ["G", "H", "I", "J", "K", "L"],
    'Valor2': [70, 80, 90, 100, 110, 120]
}
df2 = pd.DataFrame(data2)

# Imprimir los datos del primer DataFrame
print("Datos del primer DataFrame:")
print(df1)

# Imprimir los datos del segundo DataFrame
print("\nDatos del segundo DataFrame:")
print(df2)

# Agregar el segundo DataFrame al primero
df1 = pd.concat([df1, df2], axis=1)

# Imprimir los datos después de agregar el segundo DataFrame
print("\nDatos después de agregar el segundo DataFrame:")
print(df1)

# Crear un DataFrame con las ventas del primer trimestre
data = {
    'Mes': ['Enero', 'Febrero', 'Marzo'],
    'Ventas': [10000, 12000, 15000]
}

df = pd.DataFrame(data)

# Imprimir los datos
print(df)

# Leer el archivo CSV
archivo_csv = "Ventas.csv"  # Reemplaza con la ruta correcta a tu archivo CSV
df = pd.read_csv(archivo_csv)

# Imprimir el número de registros y campos
num_registros, num_campos = df.shape

print(f"Número de registros: {num_registros}")
print(f"Número de campos: {num_campos}")










