import Metodo.elim_de_gauss
from numpy import *

#datos de prueba
A = matrix([[1,2,-1,3],[2,0,2,-1],[-1,1,1,-1],[3,3,-1,2]])
B = matrix([[-8],[13],[8],[-1]])
Metodo.elim_de_gauss.metodo_gauss(A, B)
Metodo.elim_de_gauss.solucion(A,B)





