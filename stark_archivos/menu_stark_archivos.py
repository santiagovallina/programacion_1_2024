# Santiago Vallina
from biblioteca_stark_archivos import *

def opcion_continuar():
    continuar = input("¿Desea continuar? Si/No: ").lower()
    while True:
        if continuar == "si":
            return True
        elif continuar == "no":
            print("¡Hasta luego!")
            return False


def mostrar_menu():
    '''
    Muestra el menú de opciones.
    Pide 
    '''
    menu = \
        """
        A. Leer archivo JSON.
        B. Ordenar héroes por alguna de las claves numéricas (altura, peso y fuerza) de manera
        ascendente
        C. Guardar el listado ordenado en un CSV. Pedir el nombre del archivo al usuario.
        D- Salir
        """
    resultado = leer_json("stark_archivos\data_stark.json", "heroes")
    ordenado = ordenar(resultado, "peso")
    while True:
        print(menu)
        opcion_elegida = input("Elija una opcion: ").upper()
        match opcion_elegida:
            case "A":
                for personaje in resultado:
                    print(personaje)
            case "B":
                print(ordenado)
            case "C":
                guardar_archivo("heroes.csv", ordenado)
            case "H":
                print("Hasta luego :)")
                break
        limpiar_consola()
        if opcion_continuar() == False:
            break
print(mostrar_menu())