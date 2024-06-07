from estudiantes import *

# 1-Listar los alumnos por orden ascendente de apellido, si se repite,
# ordenar por nombre. Mostrar legajo, nombre, apellido y edad
def listar_alumnos_en_ascendente(lista: list) -> str:
    """
    Recibe una lista de diccionarios. Ordena por apellido cada elemento
    de manera ascendente. Si hay apellidos iguales, los ordena en ascendente
    por nombre. Muestra el legajo, nombre, apellido y edad de cada uno 
    ordenado.
    """
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i]["apellido"] > lista[j]["apellido"]:
                aux_lista = lista[i]
                lista[i] = lista[j]
                lista[j] = aux_lista
            elif lista[i]["apellido"] == lista[j]["apellido"]:
                if lista[i]["nombre"] > lista[j]["nombre"]:
                    aux_nombre = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux_nombre
    for alumno in lista:
        print(f"Legajo: {alumno['legajo']}, Alumno: {alumno['nombre']} "
        f"{alumno['apellido']}, edad: {alumno['edad']}")
#print(listar_alumnos_en_ascendente(estudiantes))


# 2-Obtener el promedio de notas para cada estudiante
def obtener_promedio_notas(lista: list) -> list:
    """
    Recibe una lista. Saca el promedio de notas de cada estudiante.
    Retorna nombre, apellido y promedio de cada alumno.
    """
    resultados = []
    for estudiante in lista:
        acumulador = 0
        for i in range(len(estudiante["notas"])):
            acumulador += estudiante["notas"][i]
        promedio = acumulador // len(estudiante["notas"])
        apellido = estudiante["apellido"]
        nombre = estudiante["nombre"]
        resultados.append((nombre, apellido, promedio))
    return resultados

def obtener_promedio(lista: list, clave: str, clave_1: str, clave_2: str) -> list:
    """
    Recibe una lista, y tres claves distintas. Saca el promedio segun el dato
    obtenido por parámetro. Retorna una lista, con el promedio sacado y su datos
    correspondientes.
    """
    resultados = []
    for alumno in lista:
        acumulador = 0
        for i in range(len(alumno[clave])):
            acumulador += alumno[clave][i]
        promedio = acumulador / len(alumno[clave])
        dato_1 = alumno[clave_1]
        dato_2 = alumno[clave_2]
        resultados.append((dato_1, dato_2, promedio))
    return resultados
# resultados = obtener_promedio(estudiantes,"notas","nombre","apellido")
# for resultado in resultados:
#     print(f"Alumno: {resultado[0]} {resultado[1]}. Promedio de notas: {resultado[2]:.1f}")



# 3-Listar legajo, nombre, apellido y edad de los estudiantes que cursan el
# programa de “Ingenieria en Informatica”
def listar_datos_alumno(lista: list):
    """
    Recibe una lista. Busca los alumnos que cursan el programa Ingenieria
    informatica. De los alumnos que lo cursan, muestra nombre, apellido, legajo y
    edad.
    """
    print("los alumnos que estudian Ingenieria en informática son:")
    for alumno in lista:
        if alumno["programa"]["nombre"] == "Ingenieria en Informatica":
            legajo = alumno["legajo"]
            nombre = alumno["nombre"]
            apellido = alumno["apellido"]
            edad = alumno["edad"]
            print(f"Alumno/a: {nombre} {apellido}, legajo: {legajo}, edad: {edad}")
#print(listar_datos_alumno(estudiantes))


# 4-Obtener un promedio de edad de los estudiantes. Mostrar nombre y
# apellido
def mostrar_promedio_de_edad(lista: list, clave: str):
    """
    Recibe una lista y un string. Recorre y saca un promedio de edad de todos los 
    alumnos.
    """
    acumulador = 0
    for alumno in lista:
            acumulador += alumno[clave]
            promedio = acumulador // len(lista)
    print(f"El promedio de edad de los estudiantes es {promedio} años.")
#mostrar_promedio_de_edad(estudiantes, "edad")


# 5-Informar el alumno con mayor pomedio de notas. Mostrar nombre y
# apellido
def mostrar_alumno_mayor_promedio() -> list:
    """
    Recorre la lista de los promedios de notas de los alumnos.
    Busca el o los alumnos de mejor promedio y los agrega a una lista.
    Muestra el mayor promedio y los alumnos que lo poseen.
    """
    alumnos = obtener_promedio_notas(estudiantes)
    promedio = None
    alumnos_mayor_promedio = []
    for alumno in alumnos:
        if promedio == None or alumno[2] > promedio:
            promedio = alumno[2]
            alumnos_mayor_promedio.append((alumno[0], alumno[1]))
        elif alumno[2] == promedio:
            alumnos_mayor_promedio.append((alumno[0], alumno[1]))
    print(f"El mayor promedio es {promedio}")
    print("Alumnos con este promedio:")
    return alumnos_mayor_promedio
#print(mostrar_alumno_mayor_promedio())


# 6-Listar nombre y apellido de los alumnos que forman el grupo “Club de
# Informática” con sus respectivos promedios
def listar_alumnos_en_grupo_informatica(lista: list):
    """
    Recibe una lista. Busca los alumnos que están en el grupo 
    club de informática. Muestra los alumnos que estén en este grupo.
    """
    print("Los alumnos que están en el “Club de Informática” son:")
    promedios = obtener_promedio_notas(lista)
    for alumno in lista:
        if "grupos" in alumno:
            for grupo in alumno["grupos"]:
                if grupo["nombre"] == "Club de Informatica":
                    for nombre, apellido, promedio in promedios:
                        if nombre == alumno["nombre"] and apellido == alumno["apellido"]:
                            print(f"{alumno['nombre']} {alumno['apellido']}. " 
                            f"Promedio: {promedio}")
#listar_alumnos_en_grupo_informatica(estudiantes)


# 7-Listar legajo, nombre, apellido y programas que cursan los alumnos
# más jóvenes.
def obtener_alumno_mas_joven(lista: list) -> list:
    """
    Recibe una lista.
    Busca a las personas más jóvenes y las agrega a una lista.
    Retorna la lista.
    """
    menor_edad = None
    alumnos_mas_jovenes = []
    for alumno in lista:
        if menor_edad == None or menor_edad > alumno["edad"]:
            menor_edad = alumno["edad"]
            alumnos_mas_jovenes = [(alumno["nombre"], alumno["apellido"], menor_edad)]
        elif menor_edad == alumno["edad"]:
            alumnos_mas_jovenes.append((alumno["nombre"], alumno["apellido"], menor_edad))
    return alumnos_mas_jovenes

def listar_datos_alumnos_mas_jovenes(lista: list):
    """
    Recibe una lista de todos los alumnos y otra de los alumnos más jóvenes.
    Muestra el legajo, nombre, apellido y programas que cursan los alumnos
    más jóvenes.
    """
    print("Estos son los datos de los alumnos más jóvenes:")
    alumnos_mas_jovenes = obtener_alumno_mas_joven(lista)
    for alumno in lista:
        for i in alumnos_mas_jovenes:
            if (i[0] == alumno["nombre"] and i[1] == alumno["apellido"]
                and i[2] == alumno["edad"]):
                print(f"legajo: {alumno['legajo']}. alumno: {alumno['nombre']} "
                f"{alumno['apellido']}. programa: {alumno['programa']['nombre']},"
                f"{alumno['programa']['nivel']}")
#listar_datos_alumnos_mas_jovenes(estudiantes)