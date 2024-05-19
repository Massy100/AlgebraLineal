import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx
import math


def pitagoras(x1, y1, x2, y2):
    result = ((((y2 - y1) ** 2) + ((x2 - x1) ** 2)) ** 0.5)
    result = round(result, 2)
    return result


def generar_grafo(nodo1, nodo2, x1, y1, x2, y2, grado):
    G = (nx.DiGraph())

    G.add_nodes_from([nodo1, nodo2, ''])

    G.add_edges_from([(nodo1, nodo2, {'weight': pitagoras(x1, y1, x2, y2)}),(nodo1, nodo1,{'weight': grado}), ('', nodo2, {'weight': (y2 - y1)}), (nodo1,'', {'weight': x2 - x1})])

    posiciones = {nodo1: (x1, y1), nodo2: (x2, y2), '': (x2, y1)}

    nx.draw(G, pos=posiciones, with_labels=True,  node_color='#bbbb22')

    etiquetas_aristas = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edges(G, pos=posiciones, arrows=True)

    nx.draw_networkx_edge_labels(G, pos=posiciones, edge_labels=etiquetas_aristas)

    plt.show()


def transformar_grados(grados, distancia):
    radian = math.radians(grados)
    calculo_sen = math.sin(radian) * distancia
    calculo_cos = math.cos(radian) * distancia
    return round(calculo_sen, 2), round(calculo_cos, 2)



def generar_instrucciones(magnitud, grados, extra1, extra2, extra3, lugar, singox, signoy):
    grados_rad = math.radians(grados)
    texto = (f'Pasos:\n'
             f'1. Encontrar X y Y por medio de seno y conseno (en radianes){extra1}: \n'
             f'Y = {magnitud} * sen({grados_rad})\n'
             f'Y = {magnitud} * {round(math.sin(grados_rad), 2)}\n'
             f'Y = {round(magnitud * math.sin(grados_rad), 2)}\n'
             f'X = {magnitud} * cos({grados_rad})\n'
             f'X = {magnitud} * {round(math.cos(grados_rad), 2)}\n'
             f'X = {round(magnitud * math.cos(grados_rad), 2)}\n'
             f'2. Apuntar segun las condiciones dadas{extra2}: \n'
             f'En este caso se nos brindó de {lugar} asi que usaremos {round(magnitud * math.cos(grados_rad), 2) * singox} para X y {round(magnitud * math.sin(grados_rad), 2) * signoy} para Y\n'
             f'3. Finalmente graficamos{extra3}: ')

    return texto


def main():
    def medir_objetos():
        cont = 0
        if caja_eje_y.get() == '':
            cont += 1
        if caja_eje_x.get() == '':
            cont += 1
        if caja_grados.get() == '':
            cont += 1
        if caja_magnitud.get() == '':
            cont += 1
        if cont > 2:
            messagebox.showerror("Error", "Datos insuficientes.")
            return True
        if cont < 2:
            messagebox.showerror("Error", "Los datos pueden ser contradictorios.")
            return True
        return False

    def obtener_grados():
        try:
            if caja_magnitud.get() == '':
                grados = math.atan(float(caja_eje_y.get()) / float(caja_eje_x.get()))

            elif caja_eje_x.get() == '':
                grados = math.asin(float(caja_eje_y.get()) / float(caja_magnitud.get()))

            elif caja_eje_y.get() == '':
                grados = math.acos(float(caja_eje_x.get()) / float(caja_magnitud.get()))

            else:
                grados = 45

            return grados

        except(Exception):
            messagebox.showerror("Error", "Error inesperado se preselccionara 45 grados.")
            return 45

    def obtener_magnitud(grados):
        rad_grado = math.radians(grados)
        if caja_grados.get() == '':
            magnitud = math.sqrt(float(caja_eje_x.get()) ** 2 + float(caja_eje_y.get()) ** 2)

        elif caja_eje_x.get() == '':
            magnitud = float(caja_eje_y.get()) / math.sin(rad_grado)

        elif caja_eje_y.get() == '':
            magnitud = float(caja_eje_x.get()) / math.cos(rad_grado)

        else:
            magnitud = 1
        return magnitud

    def crear_vector_grados_y_magnitud():

        try:
            if medir_objetos():
                int('a')

            if caja_grados.get() == '':

                grados = round(math.degrees(obtener_grados()), 2)
                print('grados vacio', grados)
            else:
                grados = float(caja_grados.get())
            if caja_magnitud.get() == '':

                magnitud = round(obtener_magnitud(grados), 2)
                print('magnitud vacio', magnitud)
            else:
                magnitud = float(caja_magnitud.get())




            if 0 > grados or grados > 90:
                messagebox.showerror("Error", "Los grados no pueden ser mayores a 90 o menor a 0")
                return


            seleccion = combo.get()



            if seleccion == "N a E":
                if caja_magnitud.get() != '' and caja_grados.get() != '':
                    grados = 90 - grados

                    y, x = transformar_grados(grados, magnitud)

                    texto = generar_instrucciones(magnitud, grados,
                                                  f', dado que usamos los grados desde el eje x a 90 le restamos el angulo actual de {90 - grados} y nos queda {grados}',
                                                  ' da a arriba a la derecha', '', 'N a E', 1, 1)
                else:
                    y, x = transformar_grados(grados, magnitud)

                    texto = generar_instrucciones(magnitud, grados,
                                                  f', dado que no tenemos grados los obtenemos gracias a la atan({y} / {x}) que en este caso nos queda {grados}\n ademas se usaran desde el eje x',
                                                  ' da a arriba a la derecha', '', 'N a E', 1, 1)

                muestra.set(value=texto)

                generar_grafo('A', 'B', 0, 0, x, y, grados)


            elif seleccion == "E a N":
                y, x = transformar_grados(grados, magnitud)

                texto = generar_instrucciones(magnitud, grados,
                                              f', dado que usamos los grados desde el eje x actual se mantiene de {grados}',
                                              ' da a arriba a la derecha', '', 'E a N', 1, 1)

                muestra.set(value=texto)

                generar_grafo('A', 'B', 0, 0, x, y, grados)

            elif seleccion == "E a S":
                y, x = transformar_grados(grados, magnitud)

                texto = generar_instrucciones(magnitud, grados,
                                              f', dado que usamos los grados desde el eje x actual se mantiene de {grados}',
                                              ' da a abajo a la derecha', ' con Y en negativo por la direccion E a S', 'E a S', 1, -1)

                muestra.set(value=texto)

                generar_grafo('A', 'B', 0, 0, x, -y, grados)

            elif seleccion == "S a E":
                if caja_magnitud.get() != '' and caja_grados.get() != '':
                    grados = 90 - grados

                    y, x = transformar_grados(grados, magnitud)

                    texto = generar_instrucciones(magnitud, grados,
                                                  f', dado que usamos los grados desde el eje x a 90 le restamos el angulo actual de {90 - grados} y nos queda {grados}',
                                                  ' da a abajo a la derecha', ' con Y en negativo por la direccion S a E', 'N a E', 1, -1)
                else:
                    y, x = transformar_grados(grados, magnitud)

                    texto = generar_instrucciones(magnitud, grados,
                                                  f', dado que no tenemos grados los obtenemos gracias a la atan({y} / {x}) que en este caso nos queda {grados} \nademas se usaran desde el eje x',
                                                  ' da a abajo a la derecha',
                                                  ' con Y en negativo por la direccion S a E', 'N a E', 1, -1)

                muestra.set(value=texto)

                generar_grafo('A', 'B', 0, 0, x, -y, grados)

            elif seleccion == "S a O":
                if caja_magnitud.get() != '' and caja_grados.get() != '':
                    grados = 90 - grados

                    y, x = transformar_grados(grados, magnitud)

                    texto = generar_instrucciones(magnitud, grados,
                                              f', dado que usamos los grados desde el eje x a 90 le restamos el angulo actual de {90 - grados} y nos queda {grados}',
                                              ' da a abajo a la izquierda', ' con X y Y en negativo por la direccion S a O',
                                              'N a E', -1, -1)
                else:
                    y, x = transformar_grados(grados, magnitud)

                    texto = generar_instrucciones(magnitud, grados,
                                                  f', dado que no tenemos grados los obtenemos gracias a la atan({y} / {x}) que en este caso nos queda {grados} \nademas se usaran desde el eje x',
                                                  ' da a abajo a la izquierda',
                                                  ' con X y Y en negativo por la direccion S a O',
                                                  'N a E', -1, -1)


                muestra.set(value=texto)

                generar_grafo('A', 'B', 0, 0, -x, -y, grados)

            elif seleccion == "O a S":
                y, x = transformar_grados(grados, magnitud)

                texto = generar_instrucciones(magnitud, grados,
                                              f', dado que usamos los grados desde el eje x actual se mantiene de {grados}',
                                              ' da a abajo a la izquierda', ' con X y Y en negativo por la direccion S a O',
                                              'S a O', -1, -1)

                muestra.set(value=texto)

                generar_grafo('A', 'B', 0, 0, -x, -y, grados)

            elif seleccion == "O a N":
                y, x = transformar_grados(grados, magnitud)

                texto = generar_instrucciones(magnitud, grados,
                                              f', dado que usamos los grados desde el eje x actual se mantiene de {grados}',
                                              ' da a arriba a la izquierda',
                                              ' con X en negativo por la direccion O a N',
                                              'O a N', -1, 1)

                muestra.set(value=texto)

                generar_grafo('A', 'B', 0, 0, -x, y, grados)

            elif seleccion == "N a O":
                if caja_magnitud.get() != '' and caja_grados.get() != '':
                    grados = 90 - grados

                    y, x = transformar_grados(grados, magnitud)

                    texto = generar_instrucciones(magnitud, grados,
                                                  f', dado que usamos los grados desde el eje x a 90 le restamos el angulo actual de {90 - grados} y nos queda {grados}',
                                                  ' da a arriba a la izquierda',
                                                  ' con X en negativo por la direccion N a O',
                                                  'N a O', -1, 1)
                else:
                    y, x = transformar_grados(grados, magnitud)

                    texto = generar_instrucciones(magnitud, grados,
                                                  f', dado que no tenemos grados los obtenemos gracias a la atan({y} / {x}) que en este caso nos queda {grados} \nademas se usaran desde el eje x',
                                                  ' da a arriba a la izquierda',
                                                  ' con X en negativo por la direccion N a O',
                                                  'N a O', -1, 1)

                muestra.set(value=texto)

                generar_grafo('A', 'B', 0, 0, -x, y, grados)


            else:

                messagebox.showerror("Error", "Debe elegir una direccion para el vector.")

        except(Exception):
            messagebox.showerror("Error", "Debe ingresar dimensiones válidas al crear el vector.")

    ventana = tk.Tk()
    ventana.title("Vector por TODO")

    texto_eje_x = tk.Label(ventana, text="Distancia en X del vector")
    texto_eje_x.pack()

    caja_eje_x = tk.Entry(ventana, width=30)
    caja_eje_x.pack(pady=10)

    texto_eje_y = tk.Label(ventana, text="Distancia en Y del vector")
    texto_eje_y.pack()

    caja_eje_y = tk.Entry(ventana, width=30)
    caja_eje_y.pack()

    texto_grados = tk.Label(ventana, text="Grados del vector")
    texto_grados.pack()

    caja_grados = tk.Entry(ventana, width=30)
    caja_grados.pack(pady=10)

    texto_magnitud = tk.Label(ventana, text="Magnitud del vector")
    texto_magnitud.pack()

    caja_magnitud = tk.Entry(ventana, width=30)
    caja_magnitud.pack(pady=10)

    texto_seleccion = tk.Label(ventana, text="Elige la direccion")
    texto_seleccion.pack()

    combo = ttk.Combobox(
        state="readonly",
        values=["N a E", "E a N", "E a S", "S a E", "S a O", "O a S", "O a N", "N a O"]
    )
    combo.pack()

    espacio_estetico = tk.Label(ventana, text="")
    espacio_estetico.pack()

    muestra = tk.StringVar()
    muestra.set("")

    boton_obtener_texto = tk.Button(ventana, text="Crear vector", command=crear_vector_grados_y_magnitud)
    boton_obtener_texto.pack()

    label_muestra = tk.Label(ventana, textvariable=muestra)
    label_muestra.pack()






    ventana.mainloop()




if __name__ == '__main__':
    main()