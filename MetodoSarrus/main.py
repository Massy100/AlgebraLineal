fila1 = [2, 3, -1]
fila2 = [4,-1, 2]
fila3 = [3, 2, 1]
fila_extra = [7, -1, 4]


def imprecion(fila1, fila2, fila3):
    print(f'Columna 1: {fila1} '
          f'Columna 2: {fila2} '
          f'Columna 3: {fila3}')
    print('(' +
          str((f'({fila1[0]} * {fila2[1]} * {fila3[2]})')) +
          ' + ' +
          str((f'({fila1[1]} * {fila2[2]} * {fila3[0]})')) +
          ' + ' +
          str((f'({fila1[2]} * {fila2[0]} * {fila3[1]})')) +
          ') - (' +
          str((f'({fila1[2]} * {fila2[1]} * {fila3[0]})')) +
          ' + ' +
          str((f'({fila1[0]} * {fila2[2]} * {fila3[1]})')) +
          ' + ' +
          str((f'({fila1[1]} * {fila2[0]} * {fila3[2]})')) +
          ')')

    print('(' +
          str((fila1[0] * fila2[1] * fila3[2])) +
          ' + ' +
          str((fila3[0] * fila1[1] * fila2[2])) +
          ' + ' +
          str((fila2[0] * fila3[1] * fila1[2])) +
          ') - (' +
          str((fila1[2] * fila2[1] * fila3[0])) +
          ' + ' +
          str((fila2[2] * fila3[1] * fila1[0])) +
          ' + ' +
          str((fila3[2] * fila1[1] * fila2[0])) +
          ')')
    print(str(((fila1[0] * fila2[1] * fila3[2]) + (fila2[0] * fila3[1] * fila1[2]) + (fila3[0] * fila1[1] * fila2[2]))) +
          ' - ' +
          str(((fila1[2] * fila2[1] * fila3[0]) + (fila2[2] * fila3[1] * fila1[0]) + (fila3[2] * fila1[1] * fila2[0]))))
    presult = ((fila1[0] * fila2[1] * fila3[2]) + (fila2[0] * fila3[1] * fila1[2]) + (fila3[0] * fila1[1] * fila2[2])) - ((fila1[2] * fila2[1] * fila3[0]) + (fila2[2] * fila3[1] * fila1[0]) + (fila3[2] * fila1[1] * fila2[0]))
    print(presult)
    return presult


delta = imprecion(fila1, fila2, fila3)
print(f'Delta = {delta}')
x = imprecion(fila_extra, fila2, fila3)
print(f'X = {x} / {delta}')
print(f'X = {x / delta}')
y = imprecion(fila1, fila_extra, fila3)
print(f'y = {y} / {delta}')
print(f'y = {y / delta}')
z = imprecion(fila1, fila2, fila_extra)
print(f'Z = {z} / {delta}')
print(f'Z = {z / delta}')