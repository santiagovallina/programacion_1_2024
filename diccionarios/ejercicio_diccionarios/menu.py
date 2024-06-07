from biblioteca_diccionarios import *

def opcion_continuar():
    continuar = input("¿Desea continuar? Si/No: ").lower()
    while True:
        if continuar == "si":
            return True
        elif continuar == "no":
            print("¡Hasta luego!")
            return False


def mostrar_menu():
    '''
    Muestra el menú de opciones.
    Pide 
    '''
    menu = \
        """
        1- Listar los alumnos por orden ascendente de apellido, si se repite,
        ordenar por nombre. Mostrar legajo, nombre, apellido y edad
        2- Obtener el promedio de notas para cada estudiante
        3- Listar legajo, nombre, apellido y edad de los estudiantes que cursan el
        programa de “Ingenieria en Informatica”
        4- Obtener un promedio de edad de los estudiantes. Mostrar nombre y
        apellido
        5- Informar el alumno con mayor pomedio de notas. Mostrar nombre y
        apellido
        6- Listar nombre y apellido de los alumnos que forman el grupo “Club de
        Informática” con sus respectivos promedios
        7- Listar legajo, nombre, apellido y programas que cursan los alumnos
        más jóvenes.
        8- Salir
        """
    
    while True:
        print(menu)
        opcion_elegida = input("Elija una opcion: ")
        match opcion_elegida:
            case "1":
                listar_alumnos_en_ascendente(estudiantes)
            case "2":
                resultados = obtener_promedio(estudiantes,"notas","nombre","apellido")
                for resultado in resultados:
                    print(f"Alumno: {resultado[0]} {resultado[1]}. Promedio de notas: {resultado[2]:.1f}")
            case "3":
                listar_datos_alumno(estudiantes)
            case "4":
                mostrar_promedio_de_edad(estudiantes, "edad")
            case "5":
                for i, j in mostrar_alumno_mayor_promedio():
                    print(f"{i} {j}")
            case "6":
                listar_alumnos_en_grupo_informatica(estudiantes)
            case "7":
                listar_datos_alumnos_mas_jovenes(estudiantes)
            case "8":
                print("Hasta luego :)")
                break
        if opcion_continuar() == False:
            break
print(mostrar_menu())