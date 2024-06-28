from biblioteca_parcial import *

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
    Muestra el menú de opción. Pide números para elegir la opción deseada.
    Muestra la opción elegida.
    '''
    menu = \
        """
        1) Cargar archivo: Se pedirá el nombre del archivo y se cargarán en una lista los elementos
        del mismo.
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
    #lista_json = cargar_archivo(nombre_archivo)
    while True:
        print(menu)
        opcion_elegida = input("Elija una opcion: ")
        match opcion_elegida:
            case "1":
                nombre_archivo = input("Ingrese el nombre del archivo: ")
                cargar_archivo(nombre_archivo)
            case "2":
                imprimir_lista()
            case "3":
                asignar_totales()
            case "4":
                numero_de_tipo = input("Ingrese que tipo desea filtrar: ")
                filtrar_por_tipo(str(numero_de_tipo))
            case "5":
                lista = ordenar("descripcion")
                for dato in lista:
                    print(dato)
            case "6":
                print(guardar_servicios())
            case "7":
                print("Hasta luego :)")
                break
        limpiar_consola()
        if opcion_continuar() == False:
            break
print(mostrar_menu())