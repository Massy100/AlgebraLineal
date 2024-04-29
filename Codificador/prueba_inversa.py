import numpy as np

# Definición de la clave y la clave inversa proporcionada
clave = np.array([
    [2, 1, 3],
    [2, -1, 2],
    [1, 2, 2]
])

clave_inversa_proporcionada = np.array([
    [-6, 4, 5],
    [-2, 1, 2],
    [5, -3, -4]
])

# Calculando la inversa de la clave usando NumPy
clave_inversa_calculada = np.linalg.inv(clave)

# Imprimiendo las claves para comparación
print("Clave Inversa Calculada:")
print(clave_inversa_calculada)

print("\nClave Inversa Proporcionada:")
print(clave_inversa_proporcionada)

# Verificación de que la clave inversa proporcionada es correcta
producto_identidad = np.dot(clave, clave_inversa_proporcionada)
print("\nProducto de la Clave por su Inversa Proporcionada (debería ser la matriz identidad):")
print(producto_identidad)

# Verificamos si el producto es la matriz identidad
es_correcta = np.allclose(producto_identidad, np.eye(3), atol=1e-10)
print("\n¿La clave inversa proporcionada es correcta?", "Sí" if es_correcta else "No")
