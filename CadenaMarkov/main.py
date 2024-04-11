def trasponer(m):
    t = []
    for i in range(len(m[0])):
        t.append([])
        for j in range(len(m)):
            t[i].append(m[j][i])
    return t

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila_actual = []
        print(f"Ingresando valores para la fila {i + 1}:")
        for j in range(columnas):
            valor = float(input(f"Ingresa el valor para el elemento [{i + 1}, {j + 1}]: "))
            fila_actual.append(valor)
        matriz.append(fila_actual)
    return matriz

def multiplicar_matrices(a, b):
    resultado = []
    for i in range(len(a)):
        fila_resultado = []
        for j in range(len(b[0])):
            suma = 0
            for k in range(len(b)):
                suma += a[i][k] * b[k][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    return resultado

# Solicitar las dimensiones de la matriz al usuario
filas = int(input("Por favor, ingresa el número de filas de la matriz: "))
columnas = int(input("Ahora, ingresa el número de columnas de la matriz: "))

# Crear la matriz con los valores proporcionados por el usuario
matriz = crear_matriz(filas, columnas)

# Solicitar las condiciones iniciales y convertirlas en una matriz 3x1
condiciones_iniciales = input("Ingresa las condiciones iniciales (3 números separados por espacios): ")
condiciones_iniciales_array = [[float(numero)] for numero in condiciones_iniciales.split()]

# Mostrar la matriz original
print("\nMatriz Original:")
for fila in matriz:
    print(fila)

# Trasponer la matriz 
matriz_trasponer = trasponer(matriz)
print("\nMatriz Traspuesta:")
for fila in matriz_trasponer:
    print(fila)

if len(condiciones_iniciales_array) != 3:
    print("Error: Debes ingresar exactamente 3 números para las condiciones iniciales.")
else:
    # Multiplicar la matriz TRASPUESTA por las condiciones iniciales
    resultado_multiplicacion = multiplicar_matrices(matriz_trasponer, condiciones_iniciales_array)

    # Preguntar al usuario cuántas veces quiere realizar la multiplicación
    veces = int(input("¿Cuántas veces deseas multiplicar la matriz traspuesta por el resultado obtenido? "))

    # Imprimir el resultado inicial de la multiplicación
    print("\nResultado inicial de la multiplicación de la MATRIZ TRASPUESTA por las condiciones iniciales:")
    for fila in resultado_multiplicacion:
        print(fila)
    
    # Realizar las multiplicaciones adicionales según lo especificado por el usuario
    for i in range(veces - 1):  # Restamos 1 porque ya hemos realizado la primera multiplicación
        resultado_multiplicacion = multiplicar_matrices(matriz_trasponer, resultado_multiplicacion)
        print(f"\nResultado después de la iteración {i + 2}:")
        for fila in resultado_multiplicacion:
            print(fila)




