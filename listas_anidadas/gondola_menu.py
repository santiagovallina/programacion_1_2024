#Santiago Vallina
from gondola_biblioteca import *


def opcion_continuar():
    continuar = input("¿Desea continuar? Si/No: ").lower()
    while True:
        if continuar == "si":
            return True
        elif continuar == "no":
            return False
        else: 
            continuar = input("Error. ¿Desea continuar? Si/No: ").lower()



def mostrar_menu(lista):
    '''
    Imprime el menú. Pide una opción. Desarrolla la función que se 
    encuentra en el índice obtenido.
    '''
    alta_realizada = False
    
    menu = \
        """
        1-Alta de productos (producto nuevo)
        2-Baja de productos (producto existente)
        3-Modificar productos (cantidad, ubicación)
        4-Listar productos
        5-Lista de productos ordenado por nombre
        6-Salir
        """
    
    while True:
        print(menu)
        opcion_elegida = input("Elija una opcion: ")
        match opcion_elegida:
            case "1":
                print(agregar_productos(lista))
                alta_realizada = True
            case "2":
                if not alta_realizada:
                    print("Debe realizar un alta de productos primero!")
                else:
                    print(eliminar_productos(lista))
            case "3":
                if not alta_realizada:
                    print("Debe realizar un alta de productos primero")
                else:
                    print((modificar_productos(lista)))
            case "4":
                print(listar_productos(lista))
            case "5":
                print(ordenar_por_nombre(lista))
            case "6":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción inválida.")
        if not opcion_continuar():
            print("¡Hasta luego!")
            break

print(mostrar_menu(gondola))


