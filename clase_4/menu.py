# Santiago Vallina
from biblioteca import *
from ordenamientos import *

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
    '''
    menu = \
        """
        1-Importar listas
        2-Listar los datos de los usuarios de México
        3-Listar los nombre, mail y teléfono de los usuarios de Brasil
        4-Listar los datos del/los usuario/s más joven/es
        5-Obtener un promedio de edad de los usuarios
        6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
        7-Listar los datos de los usuarios de México y Brasil cuyo código postal
        sea mayor a 8000
        8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40
        años.
        9-Listar los datos de los usuarios de México ordenados por nombre
        10-Listar los datos del/los usuario/s más joven/es ordenados por edad de
        manera ascendente.
        11-Listar los datos de los usuarios de México y Brasil cuyo código postal
        sea mayor a 8000 ordenado por nombre y edad de manera descendente.
        """
    
    while True:
        print(menu)
        opcion_elegida = input("Elija una opcion: ")
        match opcion_elegida:
            case "1":
                print(importar_listas())
                print(opcion_continuar())
            case "2":
                print(mostrar_datos_usuario_mexico(nombres ,telefonos, mails,
                address ,postalZip, region, country, edades))
                print(opcion_continuar())
            case "3":
                print(mostrar_datos_usuarios_brasil(country, nombres, mails, telefonos))
                print(opcion_continuar())
            case "4":
                print(listar_datos_usuario_mas_joven(nombres, telefonos, mails, address,
                        postalZip, region, country, edades))
                print(opcion_continuar())
            case "5":
                print(calcular_promedio(edades))
                print(opcion_continuar())
            case "6":
                print(mostrar_datos_mayor_de_brasil(nombres, telefonos, mails, address,
                        postalZip, region, country, edades))
                print(opcion_continuar())
            case "7":
                print(mostrar_usuarios_segun_codigo_postal(nombres, telefonos, mails, address,
                        postalZip, region, country, edades))
                print(opcion_continuar())
            case "8":
                print(mostrar_datos_usuarios_italia(country, edades, nombres,
                        mails, telefonos))
                print(opcion_continuar())
            case "9":
                print(ordenar_nombres_mexico(nombres,telefonos, mails,
                address, postalZip, region, country, edades))
                print(opcion_continuar())
            case "10":
                print(listar_datos_usuario_mas_joven(nombres,telefonos, mails,
                address, postalZip, region, country, edades))
                print(opcion_continuar())
            case "11":
                print(mostrar_datos_mexico_y_brasil_con_codigo_mayor_a_ochomil(nombres,
                telefonos, mails, address, postalZip, region, country, edades))
                print(opcion_continuar())
            case "12":
                print("Hasta luego :)")
                break

print(mostrar_menu())