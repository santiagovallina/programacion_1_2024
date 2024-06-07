# Santiago Vallina

# Ejercicio 1: Dadas las siguientes listas:
# Desarrollar una función que realice el ordenamiento de las listas por nombre de
# manera ascendente.

nombre_ =["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria",
"Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edad = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def ordenar_en_ascendente(lista : list, lista_2) -> list:
    '''
    Recibe dos listas . Las recorre y 
    las ordena de manera ascendente mediante el método burbujeo.
    '''
    for i in range(len(lista) - 1):
        for k in range(i + 1,(len(lista))):
            if lista[i] > lista[k]:
                aux_lista = lista[i]
                aux_lista_2 = lista_2[i]
                lista[i] = lista[k]
                lista_2[i] = lista_2[k]
                lista[k] = aux_lista
                lista_2[k] = aux_lista_2
    return lista


def ordenar_en_descendente(lista : list, lista_2: list) -> list:
    '''
    Recibe dos listas . Las recorre y 
    las ordena de manera descendente mediante el método burbujeo.
    '''
    for i in range(len(lista) - 1):
        for k in range(i + 1,(len(lista))):
            if lista[i] < lista[k]:
                aux_lista = lista[i]
                aux_lista_2 = lista_2[i]
                lista[i] = lista[k]
                lista_2[i] = lista_2[k]
                lista[k] = aux_lista
                lista_2[k] = aux_lista_2
    return lista


# Ejercicio 2: Dadas las siguientes listas:
# Desarrollar una función que realice el ordenamiento de las listas por nombre de
# manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera
# descendente.

nombre_materias = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales",
"Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos",
"Base de Datos", "Ergonomia", "Naturaleza"]
puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

def ordenar_lista_ascendente_y_luego_descendente(lista: list, lista_2: list) -> list:
    '''
    Recibe dos listas. Ordena la primera de manera ascendente. 
    En caso de tener dos valores iguales, ordena los items de estos
    en la segunda lista de manera descendente.
    Retorna las dos listas ordenadas.
    '''
    lista = ordenar_en_ascendente(lista, lista_2)
    for i in range(len(lista) - 1):
        for k in range(i + 1,(len(lista))):
            if lista[i] == lista[k]:
                if lista_2[i] > lista_2[k]:
                    aux_lista = lista[i]
                    aux_lista_2 = lista_2[i]
                    lista[i] = lista[k]
                    lista_2[i] = lista_2[k]
                    lista[k] = aux_lista
                    lista_2[k] = aux_lista_2
    return (lista, lista_2)





# Ejercicio 3: Dadas las siguientes listas:
# Desarrollar una función que realice el ordenamiento de las listas por apellido de
# manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera
# ascendente, si el nombre también es el mismo, debe ordenar por lista_3 de manera
# descendente.

estudiantes =["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria",
"Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
apellidos =["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez",
"Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

def ordenar_tres_listas(lista_1 :list, lista_2 : list, lista_3: list) -> list:
    '''
    Recibe tres listas. Ordena la primera en forma ascendente.
    Si hay elementos iguales en la primer lista, los ordena
    de forma ascendente según la segunda lista. Si en esta hay dos elementos iguales, 
    los ordena de forma descendente según la tercer lista.
    Retorna las 3 listas ordenadas.
    '''
    for i in range(len(lista_1) + 1):
        for k in range(i + 1, len(lista_1)):
            if lista_1[i] > lista_1[k]:
                aux_lista_1 = lista_1[i]
                aux_lista_2 = lista_2[i]
                aux_lista_3 = lista_3[i]
                lista_1[i] = lista_1[k]
                lista_1[k] = aux_lista_1
                lista_2[i] = lista_2[k]
                lista_2[k] = aux_lista_2
                lista_3[i] = lista_3[k]
                lista_3[k] = aux_lista_3
            if lista_1[i] == lista_1[k]:
                if lista_2[i] > lista_2[k]:
                    aux_lista_1 = lista_1[i]
                    aux_lista_2 = lista_2[i]
                    aux_lista_3 = lista_3[i]
                    lista_1[i] = lista_1[k]
                    lista_1[k] = aux_lista_1
                    lista_2[i] = lista_2[k]
                    lista_2[k] = aux_lista_2
                    lista_3[i] = lista_3[k]
                    lista_3[k] = aux_lista_3
                if lista_2[i] == lista_2[k]:
                    if lista_3[i] < lista_3[k]:
                        aux_lista_1 = lista_1[i]
                        aux_lista_2 = lista_2[i]
                        aux_lista_3 = lista_3[i]
                        lista_1[i] = lista_1[k]
                        lista_1[k] = aux_lista_1
                        lista_2[i] = lista_2[k]
                        lista_2[k] = aux_lista_2
                        lista_3[i] = lista_3[k]
                        lista_3[k] = aux_lista_3
    return (lista_1, lista_2, lista_3)





# 9-Listar los datos de los usuarios de México ordenados por nombre

def ordenar_nombres_mexico(lista_nombres: list, lista_telefonos: list, lista_mails: list,
    lista_address: list, lista_postal: list, lista_region: list, lista_country: list,
    lista_edades: list) -> list:
    '''
    Recibe 8 listas. Las recorre, valida si los usuarios son mexicanos.
    Ordena los nombres de manera ascendente mediante el método burbujeo.
    Retorna las listas con los datos de todos los usuarios.
    '''
    nueva_lista = []
    for i in range(len(lista_country)):
        if lista_country[i] == "Mexico":
            nueva_lista.append((lista_nombres[i], lista_telefonos[i], lista_mails[i],
            lista_address[i], lista_postal[i], lista_region[i], lista_edades[i]))
    return ordenar_en_ascendente(nueva_lista, lista_country)

#print(ordenar_nombres_mexico(nombres,telefonos, mails, address, postalZip, region, country, edades))


# 10-Listar los datos del/los usuario/s más joven/es ordenados por edad de
# manera ascendente (Si la edad se repite, ordenar por nombre de manera
# ascendente)

def listar_datos_usuario_mas_joven(lista_nombres: list, lista_telefonos: list, lista_mails: list,
    lista_address: list, lista_postal: list, lista_region: list, lista_country: list,
    lista_edades: list) -> list:
    '''
    Recibe 8 listas con los datos de los usuarios. Ordena a los usuarios de forma ascendente
    según su edad. En caso de que la edad sea la misma los ordena de forma ascendente
    según su nombre. Retorna los menores con todos sus datos.
    '''
    nueva_lista = ordenar_en_ascendente(lista_edades, lista_nombres)
    lista_menores = []
    for i in range(len(nueva_lista)):
        if nueva_lista[i] == nueva_lista[0]:
            lista_menores.append((nueva_lista[i],lista_nombres[i], lista_telefonos[i], lista_mails[i],
            lista_address[i], lista_postal[i], lista_region[i]))
            ordenar_en_ascendente(lista_menores, lista_nombres)
    return lista_menores

# print(listar_datos_usuario_mas_joven(nombres,telefonos, mails, address, postalZip, region, country, edades))


# 11-Listar los datos de los usuarios de México y Brasil cuyo código postal
# sea mayor a 8000 ordenado por nombre y edad de manera descendente

def mostrar_datos_mexico_y_brasil_con_codigo_mayor_a_ochomil(lista_nombres: list,
    lista_telefonos: list, lista_mails: list, lista_address: list, lista_postal: list,
    lista_region: list, lista_country: list, lista_edades: list) -> list:
    '''
    Recibe 8 listas. Si en la lista paises, están los elementos Mexico y
    Brasil, y en la lista postalZaip su valor es mayor a 8000,
    ordena a estos de forma descendente.
    Retorna las listas ordenadas.
    '''
    nueva_lista = []
    for i in range(len(lista_country)):
        if lista_country[i] == "Mexico" or lista_country[i] == "Brazil":
            if lista_postal[i] > 8000:
                nueva_lista.append((lista_nombres[i], lista_telefonos[i], lista_mails[i],
                lista_address[i], lista_postal[i], lista_region[i], lista_country[i], lista_edades[i]))
                ordenar_en_descendente(nueva_lista, lista_country)
    return nueva_lista






