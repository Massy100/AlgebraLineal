def impresion_dos(a1, a2, a3, b1, b2, b3, x, y):
    print('Respuestas del problema:\n', 'X:', x, '\nY:', y, '\n')
    print('Problema:\n', f'{a1}X + {a2}Y = {a3}\n{b1}X + {b2}Y = {b3}\n')
    print('Se multiplican para que Y sea eliminada en la resta:\n', f'{b2} * ({a1}X + {a2}Y = {a3})\n{-a2} * ({b1}X + {b2}Y = {b3})\n')
    print('Se hace la resta de las X y Y eliminando la Y:\n', f'{a1 * b2}X + ---Y = {a3 * b2}\n{b1 * -a2}X + ---Y = {b3 * -a2}\n')
    print('Resultado de la resta:\n', f'{(a1 * b2) + (b1 * -a2)}X = {(a3 * b2) + (b3 * -a2)}\n')
    print('Dividimos para despejar X:\n', f'X = {(a3 * b2) + (b3 * -a2)} / {(a1 * b2) + (b1 * -a2)}\n')
    print('Resultado de X:\n', f'X = {x}\n')
    print('Sustituimos X:\n',f'{a1} * {x} + {a2}Y = {a3}\n')
    print('Despejamos para Y:\n', f'{a2}Y = {a3} - {a1} * {x}\n')
    print('Operamos para encontrar Y:\n', f'Y = ({a3} - {a1} * {x}) / {a2}\n')
    print('Resultado de Y:', f'Y = {y}\n')
    return


seleccion = int(input('Elige si deseas usar 2 o 3 variables, (2) para 2 y (3) para 3: '))
if seleccion == 2:
    a1 = float(input('Escribe X1: '))
    a2 = float(input('Escribe Y1: '))
    a3 = float(input('Escribe coeficiente1: '))
    b1 = float(input('Escribe X2: '))
    b2 = float(input('Escribe Y2: '))
    b3 = float(input('Escribe coeficiente2: '))
    try:
        y = (-((b1 * a3) / a1) + b3) / (b2 + ((b1 * -a2) / a1))
        x = ((-(a2 * y) + a3) / a1)
        resultado1 = round(((a1 * x) + (a2 * y)), 2)
        resultado2 = round(((b1 * x) + (b2 * y)), 2)
        if resultado1 == a3 and resultado2 == b3:
            print('Tiene solucion')
            impresion_dos(a1, a2, a3, b1, b2, b3, x, y)
            print('X:', round(x, 2), '\nY:', round(y, 2))
        else:
            print('no tiene solucion')
    except(ZeroDivisionError):
        print('no tiene solucion')

elif seleccion == 3:
    a1 = float(input('Escribe X1: '))
    a2 = float(input('Escribe Y1: '))
    a3 = float(input('Escribe Z1: '))
    a4 = float(input('Escribe coeficiente1: '))
    b1 = float(input('Escribe X2: '))
    b2 = float(input('Escribe Y2: '))
    b3 = float(input('Escribe Z2: '))
    b4 = float(input('Escribe coeficiente2: '))
    c1 = float(input('Escribe X3: '))
    c2 = float(input('Escribe Y3: '))
    c3 = float(input('Escribe Z3: '))
    c4 = float(input('Escribe coeficiente3: '))
    try:
        d1 = ((a1 * -b3) + (b1 * a3))
        d2 = ((a2 * -b3) + (b2 * a3))
        d3 = ((a4 * -b3) + (b4 * a3))
        e1 = ((b1 * c3) + (c1 * -b3))
        e2 = ((b2 * c3) + (c2 * -b3))
        e3 = ((b4 * c3) + (c4 * -b3))

        y = (-((e1 * d3) / d1) + e3) / (e2 + ((e1 * -d2) / d1))
        x = ((-(d2 * y) + d3) / d1)
        z = ((a4 - (a1 * x) - (a2 * y)) / a3)
        resultado1 = round(a1 * x + a2 * y + a3 * z, 2)
        resultado2 = round(b1 * x + b2 * y + b3 * z, 2)
        resultado3 = round(c1 * x + c2 * y + c3 * z, 2)
        if True:
            print('Tiene solucion')
            print('Se separa la primera y segunda fila y \nse multiplican para poder eliminar la Z:\n', f'{a1}X + {a2}Y + {a3}Z = {a4}')
            print(f'{b1}X + {b2}Y + {b3}Z = {b4}')
            print(f'{c1}X + {c2}Y + {c3}Z = {c4}\n')
            print('Resultado de eliminacion de Z', f'{b3} * ({a1}X + {a2}Y + {a3}Z = {a4})')
            print(f'{-a3} * ({b1}X + {b2}Y + {b3}Z = {b4})\n')
            print(f'{d1}X + {d2}Y = {d3}\n')
            print('Se separa la segunda y tercera fila y \nse multiplican para poder eliminar la Z:\n', f'{c3} * ({b1}X + {b2}Y + {b3}Z = {b4})')
            print(f'{-b3} * ({c1}X + {c2}Y + {c3}Z = {c4})\n')
            print(f'{e1}X + {e2}Y = {e3}\n')
            print('Se operan como sistema con 2 incognitas: ')
            impresion_dos(d1, d2, d3, e1, e2, e3, x, y)
            print('Despejamos para Z:\n', f'({c1} * {x}) + ({c2} * {y}) + {c3}Z = {c4}\n')
            print(f'{c3}Z = {c4} - ({c1} * {x}) - ({c2} * {y})\n')
            print(f'Z = ({c4} - ({c1} * {x}) - ({c2} * {y})) / {c3}\n')
            print(f'Z = {z}\n')
            print('X:', round(x, 2), '\nY:', round(y, 2), '\nZ:', round(z, 2))
    except(ZeroDivisionError):
        print('No tiene solucion, div Cero')
        
     