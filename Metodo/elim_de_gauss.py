from numpy import *


def metodo_gauss(matriz, vector):
    dimension = len(matriz)-1

    l = 0
    for j in range(0, dimension):
        k = 0
        print('')
        print('     Columna:  ', l+1)
        for i in range(0, dimension-j):
            num1 = matriz[dimension-1-k, 0+l]
            num2 = matriz[dimension-k, 0+l]
            #print(num1, num2)
            fila1 = matriz[dimension-1-k]*num2
            fila2 = matriz[dimension-k]*num1
            fila_corregida = fila2-fila1
            fila1_v=vector[dimension-1-k]*num2
            fila2_v=vector[dimension-k]*num1
            # matriz[dimension-2-k]=fila1
            vector[dimension-k] = (fila2_v-fila1_v)
            matriz[dimension-k] = fila_corregida
            # print(i)
            # print(fila1,fila2,fila2-fila1)
            print('Coeficientes:  ')
            print(matriz)
            print('Terminos Independientes:  ')
            print(vector)
            if l == dimension-1 and k == 0:
                break
            #print('el K:   ', k)
            k += 1
        l += 1
def solucion(matriz,vector):
    C = (matriz**-1)*vector
    print('')
    print('Resultado de las variables:  ')
    print((C))


