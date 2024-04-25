matriz = [[0.7, 0.2, 0.1],
          [0.3, 0.4, 0.3],
          [0.2, 0.3, 0.5]]

def trasponer(m):
    t = []
    for i in range(len(m[0])):
        t.append([])
        for j in range(len(m)):
            t[i].append(m[j][i])
    return t  

matriz_trasponer = trasponer(matriz)
for fila in matriz_trasponer:
    print(fila)
    print() 