from listas import *
from funciones_y_listas import *

# Ejercicio 7: Una startup desea analizar las estadísticas de los usuarios de su sitio de
# compras on-line recientemente lanzado al mercado para ello necesita un programa
# que le permita acceder a los datos relevados.

# Realizar una función con el siguiente Menú de Opciones:

# 1-Importar listas
# 2-Listar los datos de los usuarios de México
# 3-Listar los nombre, mail y teléfono de los usuarios de Brasil
# 4-Listar los datos del/los usuario/s más joven/es
# 5-Obtener un promedio de edad de los usuarios
# 6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
# 7-Listar los datos de los usuarios de México y Brasil cuyo código postal
# sea mayor a 8000
# 8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40
# años.




def importar_listas() -> list:
    opcion = input("¿Desea importar las listas? ingrese si/no").lower()
    while opcion != "si" or opcion != "no":
        opcion = input("Respuesta incorrecta. ingrese si/no").lower()
    if opcion == "si":
        lista_nombres = nombres
        lista_telefonos = telefonos
        lista_mail = mails
        lista_direccion = address
        lista_postal = postalZip
        lista_region = region
        lista_pais = country
        lista_edades = edades
    return (lista_nombres, lista_telefonos, lista_mail, lista_direccion, lista_postal,
            lista_region, lista_pais, lista_edades)



def mostrar_datos_usuario_mexico(nombre: list,telefono: list, mail: list,
    direccion: list,postal: list, zona: list, pais: list, edad: list) -> list:
    '''
    Recibe las listas con los datos de todos los usuarios.
    Recorre las listas. Si el usuario es de México, retorna todos sus datos.
    '''
    usuarios_mexico = []
    for i in range(len(pais)):
        if pais[i] == "Mexico":
            usuarios_mexico.append((nombre[i], telefono[i], mail[i],
                                    direccion[i], postal[i], zona[i], edad[i]))
    return f"Estos son los datos de los usuarios de México: {usuarios_mexico}"


def mostrar_datos_usuarios_brasil(pais: list, nombre: list, mail: list, telefono: list) -> list:
    '''
    Recibe las listas con los datos de todos los usuarios.
    Recorre las listas. Si el usuario es de Brasil,
    retorna su nombre, mail y telefono.
    '''
    usuarios_brasil= []
    for i in range(len(pais)):
        if pais[i] == "Brazil":
            usuarios_brasil.append((nombre[i], telefono[i], mail[i]))
    return f"Estos son los datos de los usuarios de Brasil: {usuarios_brasil}"



def listar_datos_usuario_mas_joven(nombre: list,telefono: list, mail: list,
    direccion: list,postal: list, zona: list, pais: list, edad: list) -> list:
    '''
    Recibe las listas con todos los datos. Del usuario mas joven, muestra 
    todos sus datos.
    '''
    menor_edad = None
    usuarios_mas_jovenes = []
    for i in range(len(edad)):
        if menor_edad == None or menor_edad > edad[i]:
            menor_edad = edad[i]
            usuarios_mas_jovenes.append((nombre[i], telefono[i], mail[i],
                                        direccion[i], postal[i], zona[i], edad[i] ))
        elif edad[i] == menor_edad:
            usuarios_mas_jovenes.append((nombre[i], telefono[i], mail[i],
                                        direccion[i], postal[i], zona[i], edad[i] ))
    return f"Datos usuarios más jóvenes: {usuarios_mas_jovenes}"
#print(listar_datos_usuario_mas_joven(nombres, telefonos, mails, address, postalZip, region, country, edades))

def calcular_promedio(lista_de_edades : list):
    '''
    Recibe una lista. Suma todos los valores. 
    Saca el promedio de todos los números.
    Retorna el número promedio
    '''
    suma = 0
    for i in range(len(lista_de_edades)):
        suma += lista_de_edades[i]
    promedio = suma // len(lista_de_edades)
    return f"el prromedio de edades es: {promedio} años"


def mostrar_datos_mayor_de_brasil(nombre: list,telefono: list, mail: list,
    direccion: list,postal: list, zona: list, pais: list, edad: list) -> list:
    '''
    Recibe las listas con todos los datos. Las recorre y busca al usuario 
    de Brasil de mayor edad. Retorna este usuario y todos sus datos
    '''
    mayor_edad_brasil = []
    mayor_edad = None
    for i in range(len(edad)):
        if pais[i] == "Brazil":
            if mayor_edad == None or mayor_edad < edad[i]:
                mayor_edad = edad[i]
                mayor_edad_brasil.append((nombre[i], telefono[i], mail[i],
                                        direccion[i], postal[i], zona[i], edad[i]))
            elif edad[i] == mayor_edad:
                mayor_edad_brasil.append((nombre[i], telefono[i], mail[i],
                                        direccion[i], postal[i], zona[i], edad[i] ))
    return f"Datos del usuario de Brasil mas grande: {mayor_edad_brasil}"

#print(mostrar_datos_mayor_de_brasil(nombres, telefonos, mails, address, postalZip, region, country, edades))

def mostrar_usuarios_segun_codigo_postal(nombre: list,telefono: list, mail: list,
    direccion: list,postal: list, zona: list, pais: list, edad: list) -> list:
    '''
    Recibe las listas con los datos de los usuarios. 
    Busca a los usuarios que sean de Brasil y Mexico y su codigo
    postal sea mayor a 8000.
    Retorna una lista con todos estos usuarios.
    '''
    postal_actual = None
    usuarios = []
    for i in range(len(pais)):
        if pais[i] == "Brazil" or pais[i] == "Mexico":
            if postal[i] > 8000:
                postal_actual = postal[i]
                usuarios.append((nombre[i], telefono[i], mail[i],
                            direccion[i], postal[i], zona[i], edad[i]))
            elif postal[i] == postal_actual:
                usuarios.append((nombre[i], telefono[i], mail[i],
                            direccion[i], postal[i], zona[i], edad[i]))
    return f"Usuarios de Brasil y México con código postal mayor a 8000: {usuarios}"

#print(mostrar_usuarios_segun_codigo_postal(nombres, telefonos, mails, address, postalZip, region, country, edades))

def mostrar_datos_usuarios_italia(pais: list,edad: list,
                                nombre: list, mail: list, telefono: list) -> list:
    '''
    Recibe las listas con los datos de los usuarios. Las recorre y busca a 
    los italianos mayores de 40 años.
    Retorna una lista de los usuarios que cumplan esta condición.
    '''
    usuarios_italianos = []
    edad_actual = None
    for i in range(len(pais)):
        if pais[i] == "Italy":
            if edad[i] > 40:
                edad_actual = edad[i]
                usuarios_italianos.append((nombre[i], mail[i], telefono[i], edad_actual))
    return usuarios_italianos

#print(mostrar_datos_usuarios_italia(country, edades, nombres, mails,telefonos))









