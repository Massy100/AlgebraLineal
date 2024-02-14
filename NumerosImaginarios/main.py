def operar_numeros_complejos(num1, num2, operacion):
    if operacion == 'suma':
        return num1 + num2
    elif operacion == 'resta':
        return num1 - num2
    elif operacion == 'multiplicacion':
        return num1 * num2
    elif operacion == 'division':
        return num1 / num2 if num2 != 0 else "Error: División por cero."
    elif operacion == 'potencia':
        return num1 ** num2
    elif operacion == 'raiz':
        return num1 ** (1/num2)
    else:
        return "Operación no soportada."

def solicitar_numero(complejo=True):
    if complejo:
        real = float(input("Ingrese la parte real: "))
        imaginaria = float(input("Ingrese la parte imaginaria: "))
        return complex(real, imaginaria)
    else:
        return float(input("Ingrese la potencia: "))

def mostrar_menu():
    print("\nOperaciones con números complejos")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz")
    print("7. Salir")
    opcion = input("Elige una operación (1-7): ")
    return opcion

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == '7':
            print("Saliendo del programa.")
            break

        num1 = solicitar_numero(complejo=True)
        if opcion in ['5', '6']: 
            num2 = solicitar_numero(complejo=opcion == '6')
        else:
            num2 = solicitar_numero(complejo=True)

        operaciones = {
            '1': 'suma',
            '2': 'resta',
            '3': 'multiplicacion',
            '4': 'division',
            '5': 'potencia',
            '6': 'raiz'
        }

        resultado = operar_numeros_complejos(num1, num2, operaciones[opcion])
        print(f"Resultado: {resultado}\n")

if __name__ == "__main__":
    main()


