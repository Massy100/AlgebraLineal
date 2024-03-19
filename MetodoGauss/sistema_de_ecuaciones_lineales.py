import Metodo.elim_de_gauss
from numpy import *

#datos de prueba
A = matrix([[2,-1,1],[4,2,1],[-2,3,2]])
B = matrix([[5],[9],[3]])
Metodo.elim_de_gauss.metodo_gauss(A, B)
Metodo.elim_de_gauss.solucion(A,B)





