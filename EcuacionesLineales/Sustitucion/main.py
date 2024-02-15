import numpy as np

def pedir_ecuaciones(n):
    A = []
    b = []
    print(f"Introduce las {n} ecuaciones.")
    for i in range(n):
        print(f"Ecuación {i+1}:")
        coeficientes = []
        for j in range(n):
            coeficiente = float(input(f"Introduce el coeficiente {j+1} de la ecuación {i+1}: "))
            coeficientes.append(coeficiente)
        termino_independiente = float(input(f"Introduce el término independiente de la ecuación {i+1}: "))
        A.append(coeficientes)
        b.append(termino_independiente)
    return np.array(A), np.array(b)

def resolver_sistema(A, b):
    try:
        solucion = np.linalg.solve(A, b)
        return solucion
    except np.linalg.LinAlgError:
        return None

def main():
    n = int(input("¿Cuántas incógnitas tiene el sistema de ecuaciones?: "))
    A, b = pedir_ecuaciones(n)
    solucion = resolver_sistema(A, b)
    if solucion is not None:
        print("La solución del sistema es:")
        for i, x in enumerate(solucion, start=1):
            print(f"x{i} = {x}")
    else:
        print("El sistema no tiene solución")

if __name__ == "__main__":
    main()

