import matplotlib.pyplot as plt
import networkx as nx

def solicitar_valores_matriz(filas, columnas):
    matriz = []
    print("Ingresa los valores de la matriz:")
    for i in range(filas):
        fila = input(f"Fila {i+1}: ").split()
        if len(fila) != columnas:
            print("Error: El número de columnas no coincide.")
            return
        # Cambiar int(x) por float(x) para manejar números decimales
        fila = [float(x) for x in fila]
        matriz.append(fila)
    return matriz

def crear_grafo_desde_matriz(matriz):
    G = nx.DiGraph()
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor != 0:  # Si hay una conexión
                G.add_edge(i, j, weight=valor)
    return G

# Solicitar las dimensiones de la matriz al usuario
filas = int(input("Ingresa el número de filas de la matriz: "))
columnas = int(input("Ingresa el número de columnas de la matriz: "))

# Crear la matriz con los valores proporcionados por el usuario
matriz = solicitar_valores_matriz(filas, columnas)

if matriz:
    # Crear el grafo a partir de la matriz de adyacencia
    G = crear_grafo_desde_matriz(matriz)
    
    # Dibujar el grafo
    pos = nx.spring_layout(G)  # Genera una disposición de los nodos.
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='k', linewidths=1, font_size=15, arrows=True)
    
    # Dibujar los pesos de las aristas como etiquetas
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.show()