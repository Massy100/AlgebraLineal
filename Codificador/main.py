def codificar_mensaje(mensaje):
    # Crear un diccionario para mapear cada letra a un número
    alfabeto = "abcdefghijklmnñopqrstuvwxyz "
    mapeo_alfabeto = {letra: str(idx + 1) for idx, letra in enumerate(alfabeto)}
    
    # Codificar el mensaje
    mensaje_codificado = " ".join(mapeo_alfabeto[letra] for letra in mensaje.lower() if letra in mapeo_alfabeto)
    
    return mensaje_codificado

def reordenar(mensaje):
    # Usar el resultado de codificar_mensaje
    mensaje_codificado = codificar_mensaje(mensaje)
    
    # Convertir el mensaje codificado en una lista de números
    numeros_codificados = mensaje_codificado.split()
    
    # Calcular el número de columnas necesario para una matriz de 3 filas
    num_columnas = -(-len(numeros_codificados) // 3)  # Redondeo hacia arriba
    
    # Crear la matriz de 3 filas
    matriz = [["" for _ in range(num_columnas)] for _ in range(3)]
    
    # Rellenar la matriz con los números codificados
    idx = 0
    for columna in range(num_columnas):
        for fila in range(3):
            if idx < len(numeros_codificados):
                matriz[fila][columna] = numeros_codificados[idx]
                idx += 1
    
    return matriz

def multiplicar_matrices(A, B):
    # A es una matriz de m x n, B es una matriz de n x p
    m, n = len(A), len(A[0])
    p = len(B[0])
    # Inicializar la matriz resultado C de tamaño m x p con ceros
    C = [[0 for _ in range(p)] for _ in range(m)]
    
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def matriz_a_texto(matriz):
    # Inicializar la variable de texto resultante
    texto_resultante = ""
    
    # Determinar el número de columnas
    num_columnas = len(matriz[0])
    
    # Recorrer la matriz de arriba hacia abajo y de izquierda a derecha
    for columna in range(num_columnas):
        for fila in range(len(matriz)):
            if matriz[fila][columna] != "":
                texto_resultante += str(matriz[fila][columna]) + " "
    
    return texto_resultante.strip()

def decodificar_mensaje(mensaje_codificado):
    # Crear un diccionario para mapear cada número a una letra, ajustando los números altos
    alfabeto = "abcdefghijklmnñopqrstuvwxyz "
    num_elementos = len(alfabeto)  # 27 letras + espacio = 28
    
    # Dividir el mensaje codificado en una lista de números
    numeros = mensaje_codificado.split()
    
    # Decodificar el mensaje
    mensaje_decodificado = ""
    for numero in numeros:
        numero_ajustado = int(numero)
        
        # Ajustar números negativos y números mayores a la longitud del alfabeto
        if numero_ajustado < 0:
            numero_ajustado = num_elementos + (numero_ajustado % num_elementos)
        numero_ajustado = (numero_ajustado - 1) % num_elementos + 1
        
        # Encontrar la letra correspondiente
        letra_correspondiente = alfabeto[numero_ajustado - 1]  # -1 porque los índices comienzan en 0
        mensaje_decodificado += letra_correspondiente
    
    return mensaje_decodificado

def main():
    # Clave 
    clave = [
    [-1, 1, 1],
    [-2, -3, 1],
    [3, 1, -2]
    ]
    
    # Clave Inversa
    clave_inversa = [
    [5, 3, 4],
    [-1, -1, -1],
    [7, 4, 5]
    ]
    
    # Pedir al usuario que ingrese el mensaje a codificar y reordenar
    mensaje_usuario = input("Ingresa el mensaje a codificar: ")

    # Codificar el mensaje y reordenarlo en la matriz
    matriz_codificada = reordenar(mensaje_usuario)
    
    # Codificar el mensaje
    mensaje_codificado = codificar_mensaje(mensaje_usuario)
    
    # Mostrar el mensaje codificado
    print("Mensaje codificado:", mensaje_codificado)
    
    # Imprimir la matriz
    print("La matriz codificada es:")
    for fila in matriz_codificada:
        print(' '.join(fila))

    # Asegurarse de que los elementos de la matriz sean enteros
    matriz_codificada = [[int(elemento) if elemento else 0 for elemento in fila] for fila in matriz_codificada]

    # Multiplicar la matriz codificada por la clave
    resultado_multiplicacion = multiplicar_matrices(clave, matriz_codificada)

    # Imprimir la matriz resultante de la multiplicación
    print("Matriz resultante de la multiplicación con la clave:")
    for fila in resultado_multiplicacion:
        print(' '.join(map(str, fila)))
        
    # Convertir la matriz resultante de nuevo a texto
    texto_final = matriz_a_texto(resultado_multiplicacion)
    print("Texto resultante de la codificacion:", texto_final)
    
    print("-----------------------------------------------------------")
    
    # Imprimir la matriz resultante de la multiplicación
    print("Matriz decodificada:")
    for fila in resultado_multiplicacion:
        print(' '.join(map(str, fila)))
        
    # Multiplicar la matriz decodificada por la clave inversa
    resultado_multiplicacion_inversa = multiplicar_matrices(clave_inversa, resultado_multiplicacion)
    
    # Imprimir la matriz resultante de la multiplicación
    print("Matriz resultante de la multiplicación con la clave inversa:")
    for fila in resultado_multiplicacion_inversa:
        print(' '.join(map(str, fila)))
        
    # Convertir la matriz resultante de nuevo a texto
    texto_final_inversa = matriz_a_texto(resultado_multiplicacion_inversa)
    print("Texto resultante de la codificacion:", texto_final_inversa)
        
    # Imprimir el mensaje decodificado
    mensaje_decodificado = decodificar_mensaje(texto_final_inversa)
    print("Mensaje decodificado:", mensaje_decodificado)
    
    
main()

