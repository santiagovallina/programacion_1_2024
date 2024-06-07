# Santiago Vallina
from estanteria_biblioteca import *



def opcion_continuar():
    continuar = input("¿Desea continuar? Si/No: ").lower()
    while True:
        if continuar == "si":
            return True
        elif continuar == "no":
            return False
        else: 
            continuar = input("Error. ¿Desea continuar? Si/No: ").lower()

def mostrar_menu_(lista):
    '''
    Imprime el menú. Pide una opción. Desarrolla la función que se 
    encuentra en el índice obtenido.
    '''
    menu = \
        """
        1- Reponer mercadería (productos existentes)
        2- Vender mercadería (producto existente, solo si alcanza el stock)
        3- Listar inventario
        4- Salir
        """
    while True:
        print(menu)
        opcion_elegida = input("Elija una opcion: ")
        match opcion_elegida:
            case "1":
                print(reponer_mercaderia(lista))
            case "2":
                print(vender_mercaderia(lista))
            case "3":
                print((listar_productos(lista)))
            case "4":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción inválida.")
        if not opcion_continuar():
            print("¡Hasta luego!")
            break

print(mostrar_menu_(estanteria))