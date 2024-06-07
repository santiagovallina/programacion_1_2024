# Santiago Vallina

# Ejercicio 1: Desarrollar una función que Invierte el orden de los caracteres en una
# cadena.
def invertir_orden_caracteres(cadena: str) -> str:
    '''Recibe una cadena. La retorna invertida.'''
    return cadena[::-1]
#print(invertir_orden_caracteres("hola como estas"))


# Ejercicio 2: Desarrollar una función que cuente cuántas palabras hay en una cadena.
def contar_palabras_cadena(cadena: str) -> str:
    '''
    '''
    palabras = cadena.split()
    cantidad = len(palabras)
    return cantidad
#print(contar_palabras_cadena("hola que tal"))


# Ejercicio 3: Desarrollar una función que reemplaza una palabra específica por otra
# en una cadena.
def reemplazar_palabra(cadena: str) -> str:
    print(cadena)
    palabra = input("Ingrese la palabra que desea reemplazar: ")
    if palabra not in cadena:
        palabra = input("Esa palabra no se encuentra en la cadena, ingrese de nuevo: ")
    nueva_palabra = input("Ingrese la palabra que va en su lugar: ")
    cadena = cadena.replace(palabra, nueva_palabra)
    return cadena
# print(reemplazar_palabra("Hola que tal"))


# Ejercicio 4: Desarrollar una función que convierta los elementos de lista_peli en una
# cadena y muestre:
# ej. "Se recomienda ver "Matrix", "El Padrino" y "Titanic" "" para cada elemento
lista_peli = [
["Matrix", "El Padrino", "Titanic"],
["Forrest Gump", "Pulp Fiction", "Gladiador"],
["Blade Runner", "El Rey León", "Volver al Futuro"],
["La La Land", "El Gran Lebowski", "Blade Runner"],
["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
["Harry Potter", "Forrest Gump", "Pulp Fiction"],
["Titanic", "Star Wars", "El Señor de los Anillos"],
["The Truman Show", "The Shape of Water", "The Big Lebowski"],
["Forrest Gump", "The Godfather", "Goodfellas"],
["The Terminator", "The Sixth Sense", "The Great Gatsby"]
]

def recomendar_peliculas(lista):
    for peliculas in lista:
        cadena_peliculas = ", ".join(peliculas[:-1]) + " y " + peliculas[-1]
        print(f"Se recomienda ver {cadena_peliculas}")
#print(recomendar_peliculas(lista_peli))


# Ejercicio 5: Desarrollar una función que capitalice palabras en una cadena.
def capitalizar_palabras(cadena: str) -> str:
    print(cadena)
    palabras = cadena.split()
    palabra = input("Ingrese la palabra que desea capitalizar: ")
    if palabra in palabras:
        palabras[palabras.index(palabra)] = palabra.capitalize()
    else:
        print("La palabra no está en la cadena.")
    cadena = " ".join(palabras)
    return cadena
#print(capitalizar_palabras("Hola soy santi"))


# Ejercicio 6: Desarrollar una función que verifique si una cadena es un palíndromo:
# Palíndromo: Palabra o frase cuyas letras están dispuestas de tal manera que resulta
# la misma leída de izquierda a derecha que de derecha a izquierda; por ejemplo,
# anilina.
def verificar_palabra_palindromo(cadena: str) -> str:
    cadena_reversa = invertir_orden_caracteres(cadena)
    if cadena_reversa == cadena:
        print("Esta palabra es un palíndromo")
    else:
        print("Esta palabra no es un palíndromo")
#print(verificar_palabra_palindromo("aca"))


# Ejercicio 7: Desarrollar una función “ordenar” que recibe un string y un número (1 o
# -1). Se debe retornar el string ordenado de manera ascendente (si recibió 1 por
# parámetros) o descendente (si recibió -1)
# Nota: Determinar parámetros y retornos de manera que las funciones sean
# genéricas y reutilizables.
def ordenar() -> str:
    cadena = str(input("Ingrese la cadena a ordenar: "))
    numero = int(input("Ingrese 1 para ordenar de forma ascendente o -1 para ordenar de forma descendente: "))
    while numero != 1 and numero != -1:
        numero = int(input("Error, ingrese 1 o -1: "))
    lista_cadena = list(cadena)
    for i in range(len(lista_cadena) - 1):
        for j in range(i + 1, len(lista_cadena)):
            if numero == 1:
                if lista_cadena[i] > lista_cadena[j]:
                    aux_cadena = lista_cadena[i]
                    lista_cadena[i] = lista_cadena[j]
                    lista_cadena[j] = aux_cadena
            elif numero == -1:
                if lista_cadena[i] < lista_cadena[j]:
                    aux_cadena = lista_cadena[i]
                    lista_cadena[i] = lista_cadena[j]
                    lista_cadena[j] = aux_cadena
    return "".join(lista_cadena)

#print(ordenar())








