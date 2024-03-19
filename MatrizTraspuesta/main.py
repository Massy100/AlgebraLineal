matriz = [[3, 1, -2, 0],
          [6, -1, 4, 2],
          [-1, 0, 5, 7],
          [2, 3 , -4, 1]]

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