# Santiago Vallina
from data_stark import lista_personajes
from copy import deepcopy
import os


copia_lista_personajes = deepcopy(lista_personajes)
# A. Listar ordenado por Nombre. Lista todos los datos de cada superhéroe ordenados por
# Nombre de manera ascendente.
def ordenar_iterable(lista: list, clave: str, opcion_reverse: bool) -> list:
    """
    Recibe una lista de diccionarios, la clave que busco y un booleano.
    Si la clave pasada por parámetro está en el diccionario, lo agrega a una nueva
    lista. Ordena la lista en ascendente si la opción es True y en descendente si la opción
    es False. Retorna la lista ordenada.
    """
    print("Esta es la lista ordenada:")
    lista_ordenada = []
    for personaje in lista:
        lista_ordenada.append(personaje[clave])
    lista_ordenada = sorted(lista_ordenada, reverse=opcion_reverse)
    return lista_ordenada



# B. Listar Masculinos débiles. Recorrer la lista y determinar cuál es el superhéroe más débil de
# género M.
def listar_por_clave(lista: list, clave: str, valor: str) -> list:
    """
    Recibe una lista de diccionarios, una clave a buscar, y un valor a buscar.
    Retorna una lista con los diciconarios que contengan este valor.
    """
    return [personaje for personaje in lista if personaje.get(clave) == valor]



def sacar_menor(lista: list, clave: str, valor: str, clave_2: str, clave_3: str) -> list:
    """
    Recibe una lista de diccionarios, tres claves a buscar y un valor.
    De la clave a buscar saca el o los menores. 
    Retorna una lista de diccionarios con los datos de los menores.
    """
    listado = listar_por_clave(lista, clave, valor)
    menor_fuerza = None
    mas_debiles = []
    for personaje in listado:
        fuerza = int(personaje[clave_2])
        if menor_fuerza == None or fuerza < menor_fuerza:
            menor_fuerza = fuerza
            mas_debiles.append((menor_fuerza, personaje[clave_3]))
        elif fuerza == menor_fuerza:
            mas_debiles.append((menor_fuerza, personaje[clave_3]))
    return mas_debiles




# C. Cantidad por color de ojos. Determinar cuántos superhéroes tienen cada tipo de color de
# ojos.
# D. Listar por color de Pelo. Listar todos los superhéroes agrupados por color de pelo.
# E. Listar inteligencia. Listar todos los superhéroes agrupados por tipo de inteligencia.
def listar_cantidad_o_nombre_por_dato(lista: list, clave: str,clave_2: str, opcion: bool) -> dict:
    """
    Recibe una lista de diccionaros, dos claves a buscar y un booleano.
    Ordena los datos obtenidos segun opcion obtenida.
    Retorna un diccionario con los datos.
    """
    tipos = {}
    for i in lista:
        dato = i.get(clave, "Sin datos")
        if dato == "" or dato is None:
            dato = "Sin datos"
        if dato in tipos:
            if opcion == True:
                tipos[dato].append(i[clave_2])
            else:
                tipos[dato] += 1
        else:
            if opcion == True:
                tipos[dato] = [i[clave_2]]
            else:
                tipos[dato] = 1
    return tipos



# F. Listar Promedio. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
# género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género
# femenino
def sacar_promedio(lista: list, clave_genero: str, valor: str, clave_fuerza: str) -> int:
    """
    Recibe una lista de diccionarios, dos claves y un valor.
    Saca el promedio segun una clave y un valor.
    Retorna el número promedio.
    """
    contador = 0
    suma = 0
    for i in lista:
        if i[clave_genero] == valor:
            suma += int(i.get(clave_fuerza))
            contador += 1
    promedio = suma // contador
    return promedio

def mostrar_datos_mayores_al_promedio(lista: list, clave_fuerza: str, clave_nombre: str, clave_peso: str,
    clave_genero: str, valor: str) -> dict:
    """
    Recibe una lista de diccionarios, cuatro claves a buscar y un valor.
    Retorna los datos del que tengo numero mayor al promedio recibido
    """
    datos_a_mostrar = {}
    promedio = sacar_promedio(lista, clave_genero, valor, clave_fuerza)
    for i in lista:
        if int(i[clave_fuerza]) > promedio:
            nombre = i[clave_nombre]
            peso = i[clave_peso]
            datos_a_mostrar[nombre] = peso
    return datos_a_mostrar



# F. Asignar IMC. Calcular el índice de masa corporal de cada superhéroe y guardarla en un
# nuevo campo. Se deberá hacer uso de una función lambda que asignará a cada superhéroe el
# IMC calculado.

def calcular_imc(lista: list, clave_peso: str, clave_altura: str):
    """
    Recibe una lista de diccionarios y dos claves.
    Calcula el índice de masa corporal y lo agrega a cada diccionario.
    Retorna la lista.
    """
    for i in lista:
        peso = float(i[clave_peso])
        altura = float(i[clave_altura])
        i['imc'] = (lambda peso, altura: peso / (altura ** 2))(peso, altura)
    return lista



def limpiar_consola() -> None:
    """
    Imprime un mensaje indicando que limpiará la consola al presionar la tecla enter.
    """
    _ = input("\nPresione enter para continuar... ")
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')