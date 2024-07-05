import json
import os 

# 1) Cargar archivo: Se pedirá el nombre del archivo y se cargarán en una lista los elementos del
# mismo.
def cargar_archivo(nombre_archivo: str) -> list:
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

lista_archivo = cargar_archivo("recuperatorio_labo_1/compu.json")



# 2) Imprimir lista: Se imprimirá por pantalla la tabla (en forma de columnas) con los datos de los
# servicios.
def imprimir_lista(lista: list):
    """
    Recibe una lista y la imprime en pantalla.
    """
    lista_obtenida = lista
    for diccionario in lista_obtenida:
        print(f"{diccionario}")



# 3) Asignar totales: Se deberá hacer uso de una función lambda que asignará a cada servicio el
# total calculado (totalServicio) de la siguiente forma: cantidad x precioUnitario.
def asignar_totales(lista: list):
    """
    Recorre una lista. Calcula el precio unitario de cada elemento. 
    Muestra los resultados en pantalla.
    """
    lista_obtenida = lista
    for servicio in lista_obtenida:
        servicio["totalServicio"] = float(servicio["cantidad"]) * float(servicio["precioUnitario"])
        print(f"Descripcion:  {servicio['descripcion']}.  Total: {servicio['totalServicio']}")



# 4) Filtrar por tipo: Se deberá generar un archivo igual al original, pero donde solo aparezcan
# servicios del tipo seleccionado.
def filtrar_por_tipo(tipo_a_filtrar: str, lista: list):
    """
    Recibe una clave a filtrar. Agrega a una nueva lista todos los que compartan esta
    clave. Genera un nuevo archivo json con esta lista.
    """
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
def ordenar(clave: str, lista: list) -> list:
    """
    Recibe una clave a ordenar y una lista. Ordena la lista segun la clave obtenida.
    Retorna la lista ordenada.
    """
    resultado_ordenado = sorted(lista, key=lambda x: x[clave])
    nueva_lista = []
    for elemento in resultado_ordenado:
        nueva_lista.append(elemento["descripcion"])
    return nueva_lista


# 6) Guardar servicios: Se deberá guardar el listado del punto anterior en un archivo de tipo json.
def guardar_servicios(clave: str, lista: list):
    """
    Recibe una clave y una lista. Agrega la lista ordenada a un nuevo archivo json.
    """
    lista = ordenar(clave, lista)
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