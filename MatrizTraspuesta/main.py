matriz = [[1, 4, 2, -1],
          [2, 5, 0, -2],
          [3, 6, 1, 9]]

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