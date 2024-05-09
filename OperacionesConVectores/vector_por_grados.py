import matplotlib.pyplot as plt
import networkx as nx
import math


def pitagoras(x1, y1, x2, y2):
    result = ((((y2 - y1) ** 2) + ((x2 - x1) ** 2)) ** 0.5)
    result = round(result, 2)
    return result


def generar_grafo(nodo1, nodo2, x1, y1, x2, y2):
    G = (nx.DiGraph())

    G.add_nodes_from([nodo1, nodo2, ''])

    G.add_edges_from([(nodo1, nodo2, {'weight': pitagoras(x1, y1, x2, y2)}), ('', nodo2, {'weight': (y2 - y1)}), (nodo1,'', {'weight': x2 - x1})])

    posiciones = {nodo1: (x1, y1), nodo2: (x2, y2), '': (x2, y1)}

    nx.draw(G, pos=posiciones, with_labels=True,  node_color='#bbbb22')

    etiquetas_aristas = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edges(G, pos=posiciones, arrows=True)

    nx.draw_networkx_edge_labels(G, pos=posiciones, edge_labels=etiquetas_aristas)

    plt.show()


def transformar_grados(grados, distancia):
    radian = math.radians(grados)
    calculo_sen = math.sin(radian) * distancia
    calculo_cos = math.cos(radian) * distancia
    return calculo_sen, calculo_cos
    
    
    

def main():
    y, x =transformar_grados(45, 15)
    
    generar_grafo('A', 'B', 0, 0, x, y)


if __name__ == '__main__':
    main()