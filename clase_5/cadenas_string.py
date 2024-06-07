# Santiago Vallina
# Ejercicio 1: Desarrollar una función que reciba una letra y una cadena.
# Debe retornar las veces que la letra está incluida en el texto.

def contar_letra_en_string(cadena: str, letra: str) ->str:
    '''
    Recibe una cadena y una letra.
    Acumula la cantidad de veces que se encuentra la letra recibida dentro de
    la cadena.
    Retorna un mensaje diciendo cuantas veces se repite.
    '''
    acumulador = 0
    for i in range(len(cadena)):
        if letra == cadena[i]:
            acumulador += 1
    mensaje = f"La letra {letra} se repite {acumulador} veces."
    return mensaje

# Ejercicio 2: Desarrollar una función que reciba una cadena y dos índices.
# Se debe retornar la cadena que va entre las posiciones indicadas por los índices.
# Si las posiciones no son válidas se debe informar.

def mostrar_posiciones_de_cadena(cadena: str, indice_1: int, indice_2: int) -> str:
    '''
    Recibe una cadena y dos índices.
    Retorna la cadena que va entre las posiciones solicitadas
    '''
    if indice_1 < 0 or indice_2 >= len(cadena) or indice_1 >= indice_2:
        return "Las posiciones indicadas no son válidas."
    return cadena[indice_1: indice_2]

# Ejercicio 3: Desarrollar una función “char_at” que recibe una cadena y un número.
# Se debe retornar el caracter en la posición indicada por el número si ésta es válida.
# **IMPORTANTE: **Las posiciones de los caracteres en un string van del 0 hasta el
# <número de caracteres> - 1.

def char_at() -> str:
    '''
    Recibe una cadena y un número. 
    Retorna el caracter que se encuentra en índice recibido.
    '''
    cadena = str(input("Ingrese una cadena: "))
    largo = len(cadena)
    numero = int(input(f"Ingrese un número de índice del 1 al {largo}: "))
    for letra in range(len(cadena)):
        if numero < 1 or numero > len(cadena):
            return "El índice no es válido"
    return cadena[numero - 1]













