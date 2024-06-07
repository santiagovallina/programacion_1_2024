import json
import os


# 1) Cargar archivo: Se pedirá el nombre del archivo y se cargarán en una lista
# los elementos del mismo.
def cargar_archivo(archivo: str) -> list:
    """
    Recibe el nombre un archivo. Retorna una lista con los datos del archivo
    """
    lista = []
    try:
        with open(archivo, "r") as archivo:
            data = json.load(archivo)
            print("¡Archivo cargado con éxito!")
            return data
    except FileNotFoundError:
        print("El archivo no existe.")
    except TypeError:
        print("Tipo de dato erroneo")





# 2) Imprimir lista: Se imprimirá por pantalla la tabla (en forma de columnas) con los datos de los
# servicios.
def imprimir_lista(lista: list):
    for diccionario in lista:
        print(f"{diccionario}")




# 3) Asignar totales: Se deberá hacer uso de una función lambda que asignará a cada servicio el
# total calculado (totalServicio) de la siguiente forma: cantidad x precioUnitario.
def asignar_totales(lista: list):
    """
    """
    for servicio in lista:
        servicio["totalServicio"] = float(servicio["cantidad"]) * float(servicio["precioUnitario"])
    return lista






# 5) Mostrar servicios: Se deberá mostrar por pantalla un listado de los servicios ordenados por
# descripción de manera ascendente.
def ordenar(lista: list ,clave: str) -> list:
    """
    Recibe una lista de diccionarios y una clave. Ordena los diccionarios
    según la clave recibida. Retorna la lista ordenada.
    """
    resultado_ordenado = sorted(lista, key=lambda x: x[clave])
    contenido_a_guardar = ""
    for elemento in resultado_ordenado:
        contenido_a_guardar += "{},{},{},{},{},{}\n".format(
            elemento["id_servicio"],
            elemento["descripcion"],
            elemento["tipo"],
            elemento["precioUnitario"],
            elemento["cantidad"],
            elemento["totalServicio"])
    return contenido_a_guardar



def limpiar_consola() -> None:
    """
    Imprime un mensaje indicando que limpiará la consola al presionar la tecla enter.
    """
    _ = input("\nPresione enter para continuar... ")
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')

