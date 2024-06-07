# Nombre: Santiago
# Apellido: Vallina 

from listas import *

# #Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los
# guarde en una lista y la retorne. El programa principal debe invocar a la función y
# mostrar por pantalla el retorno.

def pedir_nombres(cantidad: int) -> None:
    ''' 
    Pide un número que será la cantidad de nombres.
    los guarda en una lista. 
    muestra la lista.
    '''
    lista_nombres = []
    for i in range(cantidad):
        nombre = input(f"Ingrese un nombre: ")
        lista_nombres.append(nombre)
    return lista_nombres



# Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida
# posición y número a guardar al usuario, lo guarde en una lista en la posición
# solicitada aleatoriamente y la retorne. El programa principal debe invocar a la
# función y mostrar por pantalla el retorno.

def opcion_de_continuar():
    '''
    Valida entre dos opciones.
    Retorna True si la opción elegida es si.
    Retorna False si es cualquier otra opción.
    '''
    while True:
        opcion = input("Desea ingresar un nuevo número: si / no: ").lower()
        if opcion == "si":
            return True
        else: 
            return False

def modificar_lista():
    ''' 
    Inicializa un lista de 10 números en 0. 
    Pide al usuario posición y número para modificar en la lista.
    retorna la lista actualizada.
    '''
    lista_numeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    continuar = True
    while continuar:
        posicion = int(input("Ingrese la posición que desea cambiar del 0 al 9: "))
        while posicion < 0 or posicion > 9:
            posicion = int(input("Ingrese la posición que desea cambiar del 0 al 9: "))
        numero = int(input("Ingrese el número que desea agregar a la lista: "))
        lista_numeros[posicion] = numero
        print(f"La lista actualizada es: {lista_numeros}")
        if not opcion_de_continuar():
            break
    return lista_numeros



# Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango
# especificado, validar los números solicitados dentro de ese rango, guardar en una
# lista y retornarla. El programa principal debe invocar a la función y mostrar por
# pantalla el retorno.

def validar_numero(desde: int, hasta: int):
    ''' 
    Pide un número por consola. Valida dentro de un rango.
    Retorna el número validado.
    '''
    numero_obtenido = int(input("Ingrese un numero: "))
    while numero_obtenido < desde or numero_obtenido > hasta:
        numero_obtenido = int(input("Ingrese nuevamente: "))
    return numero_obtenido

def pedir_y_guardar_numeros_en_lista():
    '''
    Recibe como parámetro la cantidad de números de la lista.
    Valida los números. Los agrega a una lista.
    Retorna la lista.
    '''
    lista_numeros = []
    for i in range(10):
        numeros = validar_numero(0, 1000)
        lista_numeros.append(numeros)
        if not opcion_de_continuar():
            break
    return lista_numeros



# Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números
# y un número especificado. La misma debe buscar el número especificado en la lista
# y retornar “True” si existe.

def buscar_numero_en_lista(lista : list, numero : int) -> bool:
    '''
    Recibe por parámetro una lista y un número especificado.
    Verifica si el número está en la lista.
    Si está en la lista devuelve True.
    Si no está en la lista devuelve False.
    '''
    if numero in lista:
        return True
    else:
        return False


# Ejercicio 5: Dadas las siguientes listas:
# Desarrollar una función que reciba por parámetro la lista de edades, busque a las
# personas de menor edad (puede ser más de una) y las retorne. El programa
# principal deberá mostrar nombre y edad de los menores.

lista_nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro",
"Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
lista_edades_ = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def buscar_menor_edad(lista_nombre: list, lista_edad : list):
    '''
    Recibe una lista de edades y una de nombres como parámetro.
    Busca el o los menores de edad.
    Muestra el nombre y edad del más joven.
    '''
    menor_numero = None
    personas_menores = []
    for i in range(len(lista_edad)):
        if menor_numero == None or menor_numero > lista_edad[i]:
            menor_numero = lista_edad[i]
            persona_mas_joven = personas_menores.append(lista_nombre[i])
        elif lista_edad[i] == menor_numero:
            personas_menores.append(lista_nombre[i])
    mensaje = print(f"Las personas más jóvenes son: {', '.join(personas_menores)} y su edad es {menor_numero}")
    return mensaje




# Ejercicio 6: Analizar los datos del archivo listas_personas.py. Utilizando el archivo
# listas_personas.py. Importar los nombres a una lista. Realizar una función que
# muestre los mismos.

def mostrar_lista(lista_nombres : list) -> list:
    '''
    Recibe y muestra una lista.
    '''
    return lista_nombres









