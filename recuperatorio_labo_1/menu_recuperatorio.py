from biblioteca_recuperatorio import *


def mostrar_menu():
    '''
    Muestra el menú de opción. Pide números para elegir la opción deseada.
    Muestra la opción elegida.
    '''
    menu = \
        """
        1) Cargar archivo: Se pedirá el nombre del archivo y se cargarán en una lista los elementosdel
        mismo.
        2) Imprimir lista: Se imprimirá por pantalla la tabla (en forma de columnas) con los datos de los
        servicios.
        3) Asignar totales: Se deberá hacer uso de una función lambda que asignará a cada servicio el
        total calculado (totalServicio) de la siguiente forma: cantidad x precioUnitario.
        4) Filtrar por tipo: Se deberá generar un archivo igual al original, pero donde solo aparezcan
        servicios del tipo seleccionado.
        5) Mostrar servicios: Se deberá mostrar por pantalla un listado de los servicios ordenados por
        descripción de manera ascendente.
        6) Guardar servicios: Se deberá guardar el listado del punto anterior en un archivo de tipo json.
        7) Salir.
        """
    while True:
        print(menu)
        opcion_elegida = input("Elija una opcion: ")
        match opcion_elegida:
            case "1":
                nombre_archivo = str(input("Ingrese el nombre del archivo: "))
                cargar_archivo(nombre_archivo)
            case "2":
                imprimir_lista(lista_archivo)
            case "3":
                asignar_totales(lista_archivo)
            case "4":
                tipo = input("Ingrese que tipo desea filtrar: ").capitalize()
                filtrar_por_tipo(tipo, lista_archivo)
            case "5":
                lista = ordenar("descripcion", lista_archivo)
                print("Servicios ordenados por descripción:")
                for dato in lista:
                    print(dato)
            case "6":
                print(guardar_servicios("descripcion", lista_archivo))
            case "7":
                print("Hasta luego :)")
                break
        limpiar_consola()
print(mostrar_menu())