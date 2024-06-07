from copy import deepcopy
from functools import reduce

# SHALLOW COPY =  nombre_de_la_lista[:] o nombre_de_la_lista.copy()
# se usa para no modificar la lista original mientras se usa una copia de la lista.

lista = [1, 2, 3, 4, 5]

copia_lista = lista[:] # opcion 1
copia_lista = lista.copy() # opcion 2
copia_lista[2] = 30
# print(copia_lista)
# print(lista)

# DEEP COPY = En caso de listas compuestas (listas con diccionarios, listas, etc dentro)
# Se usa de la sig manera -> deepcopy(nombre de la lista)
# Hay que importar "from copy import deepcopy"

lista_dos = [
    {"nombre": "pepe", "edad": 34, "trabajo": "mecanico"},
    {"nombre": "maria", "edad": 25, "trabajo": "doctora"},
    {"nombre": "rober", "edad": 51, "trabajo": "kiosquero"}
]

copia_lista_dos = deepcopy(lista_dos)
copia_lista_dos[0]["nombre"] = "Jose"
# print(lista_dos)
# print(copia_lista_dos)


# ENUMERATE = enumera los elementos de la lista
# si le pongo start = un numero, arranca desde ese numero, si no arranca de 0
# for i, e in enumerate(lista_dos, start= 2):
#     print(i, e)


# ZIP() = toma como argumento dos o mas objetos iterables, y retorna un nuevo iterable 
nombres = ["pepe", "maria", "rober"]
apellidos = ["gutierrez", "perez", "acosta"]
edades = [22, 42, 67]

# for e_nombre, e_apellido, e_edad in zip(nombres, apellidos, edades):
#     print(e_nombre, e_apellido, e_edad)


# MAP() = Aplica una funcion sobre los items de un objeto iterable (lista, tupla, etc)
# se usa asi -> map(funcion, objeto iterable)
# Retorna un objeto map que despues se puede castear a una lista o tupla.

def cuadrado(numero):
    return numero * numero

numeros = [1, 2, 3, 4, 5]
resultado = map(cuadrado, numeros)
lista_resultados = list(resultado)
#print(lista_resultados)

# MAP() con un lambda
resultado_lambda = list(map(lambda numero: numero*numero, numeros))
#print(resultado_lambda)



# EXTEND() = permite agregar todos los elementos de un iterable al final de una lista, 
# lo que permite unir 2 listas.
# modo de uso ---> list.extend(nombre del iterable)



# REDUCE() = toma como argumento un conjunto de valores (iterable), y lo reduce a un unico valor
# ese unico valor dependera de la funcion aplicada.
# modo de uso ---> reduce(funcion, iterable, [inicializador]) [inicializador]---> esto es opcional, es el valor inicial, si no se pone esto 
# arranca del primer elemento de la lista  (((((from functools import reduce)))))

def add(a, b):
    return a + b
#print(reduce(add,[10 , 10 , 10, 10]))
#tambien se puede usar con lambda


# FILTER() = permite filtrar elementos de un iterable. como primer argumento se le debe pasar
# una funcion y como segundo un objeto iterable que desea filtrar 
# retorna un iterador cuyos elementos son aquellos que cumplieron con el True de la funcion
#     filter(funcion, iterable)

def es_par(n):
    return n % 2 == 0

lista_pares = list(filter(es_par, numeros))
# print(lista_pares)

lista_pares = list(filter(lambda n: True if n % 2 == 0 else False, numeros))
#print(lista_pares)


# SORT() = solo funciona con lista, ordena la lista que estoy usando
# SORTED() = funciona con cualquier iterable, retorna un nuevo iterable ya ordenado
# tienen argumentos opcionales que son KEY y REVERSE.
# KEY =  tiene el valor de una funcion 
# REVERSE = tiene un valor booleano (true o false)
# Se puede usar len como el valor para el argumento key, key=len indica al programa ordenar
# la lista de nombre por ej por longitud, del mas corto al mas largo.

#SORT
mi_lista = [1, 2, 3, 4]
mi_lista.sort()
#print("lista ordenada: ", mi_lista)

mi_lista.sort(reverse=True)
#print("en versa", mi_lista)


lista_dos = [
    {"nombre": "pepe", "edad": 34, "trabajo": "mecanico"},
    {"nombre": "maria", "edad": 25, "trabajo": "doctora"},
    {"nombre": "rober", "edad": 51, "trabajo": "kiosquero"}
]

lista_dos.sort(key=lambda persona : persona["edad"], reverse=True) #lambda
#print(lista_dos)[


# SORTED
names = ["pepe", "juan", "josep", "ana", "bian"]
names_ordenados = sorted(names) #si quiero que sea de atras para adelante, seria: sorted(names, reverse=True)
#print(names_ordenados)

enunciado = "hola mundo para a todos."
#print(sorted(enunciado.split(), key=len)) 
# convierte el enunciado en una lista gracias al split(), y con el sorted lo ordena, y el parametro
# es key=len


# GET() -> diccionarios. Si a un diccionario le falta una clave, al imprimir los valores de las keys nos da error
lista_tres = [
    {"edad": 34, "trabajo": "mecanico"},
    {"nombre": "maria", "edad": 25, "trabajo": "doctora"},
    {"nombre": "rober", "edad": 51, "trabajo": "kiosquero"}
]
# for e_nombre in lista_tres:
#     print(e_nombre.get("nombre", "SINNOMBRE"))
