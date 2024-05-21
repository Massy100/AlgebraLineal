import math

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