#Santiago Vallinna
import json
import os

# 1.Crear la función leer_json() que va a recibir el nombre y extensión de donde se ubica el
# archivo a leer (Ruta absoluta o relativa), y también el nombre de la lista a leer por ejemplo en la
# imagen anterior la lista está en la clave “heroes” Si el archivo existe deberia leer el archivo json
# y retornar la lista obtenida.
# Si el achivo no existe deberia retornar False (USAR EXCEPCIONES)

def leer_json(archivo: str, clave_lista: str):
    """
    Recibe el nombre de un archivo y la clave de una lista.
    Si la lista está en el archivo, la muestra
    """
    try:
        with open(archivo, "r") as archivo:
            data = json.load(archivo)
            if clave_lista in data:
                return data[clave_lista]
            else:
                return False
    except FileNotFoundError:
        print("El archivo no existe.")
    except TypeError:
        print("Tipo de dato erroneo")
    except IndexError:
        print("Error de indice.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON '{archivo}'.")



# 2. Crear la función generar_csv()
# La función va a recibir el nombre y extensión del archivo csv de los superhéroes (Puede ser ruta
# absoluta o relativa) y la lista de los mismos. Si la lista no está vacía la función deberá guardar
# en un string la información en formato csv (separado con comas) con la cabecera
# correspondiente.
# Una vez generado el string debería usar la función del siguiente punto (3) para guardar ese
# string generado al archivo. Si la lista está vacía retornar False

def generar_csv(nombre_archivo: str, lista: list):
    """
    Recibe un nombre para el archivo a crear y una lista de diccionarios.
    Crea un archivo CSV con los datos obtenidos.
    """
    if not lista:
        print("La lista de superhéroes está vacía. No se generará el archivo CSV.")
        return False
    columnas = ["nombre", "identidad", "altura", "fuerza", "peso", "inteligencia"]
    with open(nombre_archivo, "w") as archivo:
        archivo.write(",".join(columnas) + "\n")
        for e_tema in lista:
            linea = "{0},{1},{2},{3},{4},{5}\n".format(
                                e_tema["nombre"],
                                e_tema["identidad"],
                                e_tema["altura"], 
                                e_tema["fuerza"],
                                e_tema["peso"],
                                e_tema["inteligencia"])
            archivo.write(linea)
    print("¡Archivo CSV generado con éxito!")



# 3. Crear la función 'guardar_archivo' la cual recibirá por parámetro un string que indicará el
# nombre con el cual se guardará el archivo junto con su extensión (ejemplo: 'archivo.csv') y
# como segundo parámetro tendrá un string el cual será el contenido a guardar en dicho archivo.
# Debe abrirse el archivo en modo escritura+, ya que en caso de no existir, lo creara y en caso de
# existir, lo va a sobreescribir La función debera retornar True si no hubo errores, caso contrario
# False (VALIDAR CON EXCEPCIONES), además en caso de éxito, deberá imprimir un
# mensaje respetando el formato:
# Se creó el archivo: nombre_archivo.csv



def guardar_archivo(nombre_archivo: str, contenido: str):
    """
    Recibe un string como nombre del archivo a crear, y un contenido a agregar.
    Agrega 
    """
    try:
        with open(nombre_archivo, "w+") as archivo:
            archivo.write(contenido)
        print(f"Se creó el archivo: {nombre_archivo}")
        return True
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el directorio o el archivo: {nombre_archivo}")
        return False
    except PermissionError:
        print(f"Error: No tiene permisos para escribir en el directorio: {nombre_archivo}")
        return False



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





def limpiar_consola() -> None:
    """
    Imprime un mensaje indicando que limpiará la consola al presionar la tecla enter.
    """
    _ = input("\nPresione enter para continuar... ")
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')