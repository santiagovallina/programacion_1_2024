import json
import os



# 1) Cargar archivo: Se pedirá el nombre del archivo y se cargarán en una lista
# los elementos del mismo.
def cargar_archivo(nombre_archivo) -> list:
    """
    Recibe el nombre un archivo. Retorna una lista con los datos del archivo
    """
    try:
        with open(nombre_archivo, "r") as archivo:
            data = json.load(archivo)
            print("¡Archivo cargado con éxito!")
            return data
    except FileNotFoundError:
        print("El archivo no existe.")
    except TypeError:
        print("Tipo de dato erroneo")



# 2) Imprimir lista: Se imprimirá por pantalla la tabla (en forma de columnas) con los datos de los
# servicios.
def imprimir_lista():
    lista = cargar_archivo("primer_parcial_labo\data_parcial.json")
    for diccionario in lista:
        print(f"{diccionario}")




# 3) Asignar totales: Se deberá hacer uso de una función lambda que asignará a cada servicio el
# total calculado (totalServicio) de la siguiente forma: cantidad x precioUnitario.
def asignar_totales():
    """
    """
    lista = cargar_archivo("primer_parcial_labo\data_parcial.json")
    print("Descripcion              Cantidad      Precio       Total")
    for servicio in lista:
        servicio["totalServicio"] = float(servicio["cantidad"]) * float(servicio["precioUnitario"])
        print(f"{servicio['descripcion']}              {servicio['cantidad']}      {servicio['precioUnitario']}       {servicio['totalServicio']}")



# 4) Filtrar por tipo: Se deberá generar un archivo igual al original, pero donde solo aparezcan
# servicios del tipo seleccionado.
def filtrar_por_tipo(tipo_a_filtrar: str):
    lista = cargar_archivo("primer_parcial_labo\data_parcial.json")
    nueva_lista = []
    for servicio in lista:
        if servicio["tipo"] == tipo_a_filtrar:
            nueva_lista.append(servicio)
    if nueva_lista:
        nombre_nuevo = f"servicios_tipo_{tipo_a_filtrar}.json"
        with open(nombre_nuevo, "w") as archivo:
            json.dump(nueva_lista, archivo, indent=4)
            print("¡Nuevo archivo guardado con éxito!")



# 5) Mostrar servicios: Se deberá mostrar por pantalla un listado de los servicios ordenados por
# descripción de manera ascendente.
def ordenar(clave):
    lista = cargar_archivo("primer_parcial_labo\data_parcial.json")
    print("Servicios ordenados por descripción:")
    resultado_ordenado = sorted(lista, key=lambda x: x[clave])
    nueva_lista = []
    for elemento in resultado_ordenado:
        nueva_lista.append(elemento["descripcion"])
    return nueva_lista


# 6) Guardar servicios: Se deberá guardar el listado del punto anterior en un archivo de tipo json.
def guardar_servicios():
    lista = ordenar("descripcion")
    with open("Descripcion.json", "w") as archivo:
        json.dump(lista, archivo, indent=4)
        print("¡Nuevo archivo guardado con éxito!")



def limpiar_consola() -> None:
    """
    Imprime un mensaje indicando que limpiará la consola al presionar la tecla enter.
    """
    _ = input("\nPresione enter para continuar... ")
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')

