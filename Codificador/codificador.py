# Clave 
clave = [
    [2, 1, 3],
    [2, -1, 2],
    [1, 2, 2]
    ]
    
# Clave Inversa
clave_inversa = [
    [-6, 4, 5],
    [-2, 1, 2],
    [5, -3, -4]
    ]

def codificar_mensaje(mensaje):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz "
    mapeo_alfabeto = {letra: str(idx + 1) for idx, letra in enumerate(alfabeto)}
    mensaje_codificado = " ".join(mapeo_alfabeto[letra] for letra in mensaje.lower() if letra in mapeo_alfabeto)
    print(f"Mensaje codificado: {mensaje_codificado}")  # Debugging
    return mensaje_codificado

def reordenar(mensaje):
    mensaje_codificado = codificar_mensaje(mensaje)
    numeros_codificados = [int(num) for num in mensaje_codificado.split()]
    num_columnas = -(-len(numeros_codificados) // 3)
    matriz = [[0 for _ in range(num_columnas)] for _ in range(3)]
    idx = 0
    for columna in range(num_columnas):
        for fila in range(3):
            if idx < len(numeros_codificados):
                matriz[fila][columna] = numeros_codificados[idx]
                idx += 1
    print(f"Matriz reordenada: {matriz}")  # Debugging
    return matriz

def multiplicar_matrices(A, B):
    m, n = len(A), len(A[0])
    p = len(B[0])
    C = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += int(A[i][k]) * int(B[k][j])
    print(f"Resultado de la multiplicación: {C}")  # Debugging
    return C

def matriz_a_texto(matriz):
    texto_resultante = ""
    num_columnas = len(matriz[0])
    for columna in range(num_columnas):
        for fila in range(len(matriz)):
            if matriz[fila][columna] != "":
                texto_resultante += str(matriz[fila][columna]) + " "
    print(f"Texto de la matriz: {texto_resultante.strip()}")  # Debugging
    return texto_resultante.strip()

def decodificar_mensaje(mensaje_codificado):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz "
    num_elementos = len(alfabeto) + 1  # 27 letras + espacio = 28
    
    numeros = mensaje_codificado.split()
    mensaje_decodificado = ""

    for numero in numeros:
        numero_ajustado = int(numero)
        
        if numero_ajustado == 0:
            mensaje_decodificado += ' '  # Tratar los ceros como espacios
        else:
            # Ajustar números negativos y números mayores a la longitud del alfabeto
            if numero_ajustado < 0:
                numero_ajustado += num_elementos
            if numero_ajustado >= num_elementos:
                numero_ajustado -= num_elementos
            
            letra_correspondiente = alfabeto[(numero_ajustado - 1) % len(alfabeto)]
            mensaje_decodificado += letra_correspondiente

    return mensaje_decodificado
    
def texto_a_matriz(texto):
    # Dividir el texto en números, asumiendo que está separado por espacios
    numeros = list(map(int, texto.split()))

    # Asumiendo que siempre debemos tener 3 filas
    num_filas = 3
    # Calcula el número de columnas necesarias
    num_columnas = -(-len(numeros) // num_filas)  # Cielo de la división

    # Crear la matriz con 3 filas inicialmente vacías
    matriz = [[0 for _ in range(num_columnas)] for _ in range(num_filas)]

    # Llenar la matriz con los números codificados, ajustando en columnas de izquierda a derecha
    idx = 0
    for num in numeros:
        fila = idx % num_filas  # Determina la fila actual basada en el índice
        columna = idx // num_filas  # Determina la columna actual basada en el índice
        matriz[fila][columna] = num
        idx += 1

    return matriz

def matriz_inversa_descifrado(texto_cifrado):
    # Asumiendo que texto_cifrado es el resultado directo de la codificación
    # Convertir este texto cifrado de nuevo a la matriz numérica adecuada para descifrar
    matriz_cifrada = texto_a_matriz(texto_cifrado) 

    # Multiplicar por la clave inversa
    resultado_multiplicacion_inversa = multiplicar_matrices(clave_inversa, matriz_cifrada)

    # Convertir resultado a texto
    texto_final_inversa = matriz_a_texto(resultado_multiplicacion_inversa)
    mensaje_decodificado = decodificar_mensaje(texto_final_inversa)

    return mensaje_decodificado

def matriz_inversa_cifrado(mensaje_usuario):
    matriz_codificada = reordenar(mensaje_usuario)
    resultado_multiplicacion = multiplicar_matrices(clave, matriz_codificada)
    texto_final = matriz_a_texto(resultado_multiplicacion)
    
    resultado_multiplicacion_inversa = multiplicar_matrices(clave_inversa, resultado_multiplicacion)
    texto_final_inversa = matriz_a_texto(resultado_multiplicacion_inversa)
    mensaje_decodificado = decodificar_mensaje(texto_final_inversa)
    
    return texto_final, mensaje_decodificado

def cifrar_mensaje(mensaje_usuario):
    matriz_codificada = reordenar(mensaje_usuario)
    resultado_multiplicacion = multiplicar_matrices(clave, matriz_codificada)
    texto_cifrado = matriz_a_texto(resultado_multiplicacion)
    return texto_cifrado

def descifrar_mensaje(texto_cifrado):
    # Convertir el texto cifrado de nuevo a la matriz numérica adecuada para descifrar
    matriz_cifrada = texto_a_matriz(texto_cifrado)

    # Multiplicar por la clave inversa
    resultado_multiplicacion_inversa = multiplicar_matrices(clave_inversa, matriz_cifrada)

    # Convertir resultado a texto
    texto_descifrado = matriz_a_texto(resultado_multiplicacion_inversa)
    mensaje_descifrado = decodificar_mensaje(texto_descifrado)

    return mensaje_descifrado






