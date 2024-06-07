import os

def opcion_continuar():
    continuar = input("¿Desea continuar? Si/No: ").lower()
    while True:
        if continuar == "si":
            return True
        elif continuar == "no":
            return False
        else: 
            continuar = input("Error. ¿Desea continuar? Si/No: ").lower()

def mostrar_menu():
    '''
    '''
    menu = \
        """
        """
    
    while True:
        print(menu)
        opcion_elegida = input("Elija una opcion: ")
        match opcion_elegida:
            case "1":
                print()
                print(opcion_continuar())
            case "2":
                print()
                print(opcion_continuar())
            case "3":
                print()
            case "4":
                print()
                print(opcion_continuar())
            case "5":
                print()
                print(opcion_continuar())
            case "6":
                print()
                print(opcion_continuar())
            case "7":
                print()
                print(opcion_continuar())
            case "8":
                print()
                print(opcion_continuar())
            case "9":
                print()
                print(opcion_continuar())
            case "10":
                print()
                print(opcion_continuar())
            case "11":
                print()
                print(opcion_continuar())
            case "12":
                print("Hasta luego :)")
                break


def importar_listas() -> list:
    opcion = input("¿Desea importar las listas? ingrese si/no").lower()
    while opcion != "si" or opcion != "no":
        opcion = input("Respuesta incorrecta. ingrese si/no").lower()
    if opcion == "si":
        pass
    return ()


def ordenar_en_ascendente(lista : list, lista_2) -> list:
    '''
    Recibe dos listas . Las recorre y 
    las ordena de manera ascendente mediante el método burbujeo.
    '''
    for i in range(len(lista) - 1):
        for k in range(i + 1,(len(lista))):
            if lista[i] > lista[k]:
                aux_lista = lista[i]
                lista[i] = lista[k]
                lista[k] = aux_lista
    return lista

def ordenar_en_descendente(lista : list, lista_2) -> list:
    '''
    Recibe dos listas . Las recorre y 
    las ordena de manera ascendente mediante el método burbujeo.
    '''
    for i in range(len(lista) - 1):
        for k in range(i + 1,(len(lista))):
            if lista[i] < lista[k]:
                aux_lista = lista[i]
                lista[i] = lista[k]
                lista[k] = aux_lista
    return lista


def validar_numero(desde: int, hasta: int):
    ''' 
    Pide un número por consola. Valida dentro de un rango.
    Retorna el número validado.
    '''
    numero_obtenido = int(input("Ingrese un numero: "))
    while numero_obtenido < desde or numero_obtenido > hasta:
        numero_obtenido = int(input("Ingrese nuevamente: "))
    return numero_obtenido


#import os
def limpiar_consola() -> None:
    """
    Imprime un mensaje indicando que limpiará la consola al presionar la tecla enter.
    """
    _ = input("\nPresione enter para continuar... ")
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')


def ordenar(lista: list ,clave: str) -> list:
    """
    Recibe una lista de diccionarios y una clave. Ordena los diccionarios
    según la clave recibida. Retorna la lista ordenada.
    """
    resultado_ordenado = sorted(lista, key=lambda heroe: heroe[clave])
    contenido_a_guardar = ""
    for elemento in resultado_ordenado:
        contenido_a_guardar += "{},{},{},{},{},{}\n".format(
            elemento["nombre"],
            elemento["identidad"],
            elemento["altura"],
            elemento["fuerza"],
            elemento["peso"],
            elemento["inteligencia"])
    return contenido_a_guardar