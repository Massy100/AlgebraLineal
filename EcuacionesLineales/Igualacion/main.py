def sustitucion_dos(a1, a2, a3, b1, b2, b3):
    
    print(f"Sistema de ecuaciones:")
    print(f"{a1}X + {a2}Y = {a3}")
    print(f"{b1}X + {b2}Y = {b3}\n")

    y = (a3 - a1 * b3 / b1) / (a2 - a1 * b2 / b1)
    print(f"Y = ({a3} - {a1} * {b3} / {b1}) / ({a2} - {a1} * {b2} / {b1})")
    print(f"Y = {y}\n")

    print(f"{b1}X + {b2}({y}) = {b3}")

    x = (b3 - b2 * y) / b1
    print(f"X = ({b3} - {b2} * {y}) / {b1}")
    print(f"X = {x}\n")

    if round(a1 * x + a2 * y, 2) == a3 and round(b1 * x + b2 * y, 2) == b3:
        print("La solución es.")
        print(f"X = {x}, Y = {y}")
    else:
        print("La ecuacion no tiene solucion.")


def sustitucion_tres(a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4):
    print("Sistema de ecuaciones:")
    print(f"{a1}X + {a2}Y + {a3}Z = {a4}")
    print(f"{b1}X + {b2}Y + {b3}Z = {b4}")
    print(f"{c1}X + {c2}Y + {c3}Z = {c4}\n")

    y = (a4 - a1 * c4 / c1 - a3 * c3 / c1) / (a2 - a1 * c2 / c1)
    print(f"Y = ({a4} - {a1} * {c4} / {c1} - {a3} * {c3} / {c1}) / ({a2} - {a1} * {c2} / {c1})")
    print(f"Y = {y}\n")

    x = (b4 - b2 * y - b3 * c4 / c3 - b1 * y * c1 / c3) / (b1 - b3 * c1 / c3)
    print(f"X = ({b4} - {b2} * {y} - {b3} * {c4} / {c3} - {b1} * {y} * {c1} / {c3}) / ({b1} - {b3} * {c1} / {c3})")
    print(f"X = {x}\n")

    z = (c4 - c1 * x - c2 * y) / c3
    print(f"Z = ({c4} - {c1} * {x} - {c2} * {y}) / {c3}")
    print(f"Z = {z}\n")

    if round(a1 * x + a2 * y + a3 * z, 2) == a4 and round(b1 * x + b2 * y + b3 * z, 2) == b4 and round(
            c1 * x + c2 * y + c3 * z, 2) == c4:
        print("La solución es.")
        print(f"X = {x}, Y = {y}, Z = {z}")
    else:
        print("La ecuacion no tiene solucion.")


seleccion = int(input("Elige si deseas usar 2 o 3 variables (2 para 2 y 3 para 3): "))

if seleccion == 2:
    print("ECUACION 1")
    a1 = float(input("Escribe el coeficiente X1: "))
    a2 = float(input("Escribe el coeficiente Y1: "))
    a3 = float(input("Escribe el resultado =: "))

    print("ECUACION 2")
    b1 = float(input("Escribe el coeficiente X1: "))
    b2 = float(input("Escribe el coeficiente Y1: "))
    b3 = float(input("Escribe el resultado =: "))

    sustitucion_dos(a1, a2, a3, b1, b2, b3)

elif seleccion == 3:

    print("ECUACION 1")
    a1 = float(input("Escribe el coeficiente X1: "))
    a2 = float(input("Escribe el coeficiente Y1: "))
    a3 = float(input("Escribe el coeficiente Z1: "))
    a4 = float(input("Escribe el resultado =: "))

    print("ECUACION 2")
    b1 = float(input("Escribe el coeficiente X1: "))
    b2 = float(input("Escribe el coeficiente Y1: "))
    b3 = float(input("Escribe el coeficiente Z1: "))
    b4 = float(input("Escribe el resultado =: "))
    
    print("ECUACION 3")
    c1 = float(input("Escribe el coeficiente X1: "))
    c2 = float(input("Escribe el coeficiente Y1: "))
    c3 = float(input("Escribe el coeficiente Z1: "))
    c4 = float(input("Escribe el resultado =: "))

    sustitucion_tres(a1, a2, a3, a4, b1, b2, b3, b4,c1,c2,c3,c4)