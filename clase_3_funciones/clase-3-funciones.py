# Nombre: Santiago
# Apellido: Vallina

# Ejercicio 3-1: Crear una función que muestre por pantalla el número que recibe
# como parámetro.
def mostrar_numero(numero: int):
    return numero

# Ejercicio 3-2: Crear una función que pida el ingreso de un número y lo retorne.
def retornar_numero():
    numero = int(input("Ingrese un numero: "))
    return numero

# Ejercicio 3-3: Crear una función que permita determinar si un número es par o no. La
# función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el
# programa principal realizando la invocación o llamada.
def determinar_numero_par(numero: int):
    numero_par = True
    if numero % 2 == 0:
        numero_par = True
    else:
        numero_par = False
    return numero_par

# Ejercicio 3-4: Especializar la función del punto 3.1 y 3.2 para que valide el número en
# un rango determinado pasado por parámetro “desde”-“hasta”.

def validar_numero(desde: int, hasta: int):
    numero_obtenido = int(input("Ingrese un numero: "))
    while numero_obtenido < desde or numero_obtenido > hasta:
        print("Intente nuevamente, debe estar en el parametro.")
        numero_obtenido = retornar_numero()
    return mostrar_numero(numero_obtenido)


# Ejercicio 3-5: Realizar un programa en donde se puedan utilizar los prototipos de la
# función Restar en sus 4 combinaciones.
#  Restar1(int, int)->int:
#  Restar2()->int:
#  Restar3(int, int):
#  Restar4():

def restar_1(numero_1 : int, numero_2 : int) -> int:
    resta = numero_1 - numero_2
    return resta

def restar_2() -> int:
    numero_1 = int(input("Ingrese un numero: "))
    numero_2 = int(input("Ingrese un numero: "))
    resta = numero_1 - numero_2
    return resta

def restar_1(numero_1 : int, numero_2 : int):
    resta = numero_1 - numero_2 
    print(resta)

def restar_4():
    numero_1 = int(input("Ingrese un numero: "))
    numero_2 = int(input("Ingrese un numero: "))
    resta = numero_1 - numero_2
    print(resta)


# Ejercicio 3-6: Realizar un programa que: asigne a la variable numero1 un valor
# solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a
# dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado
# por pantalla. Atención: pueden reutilizarse funciones ya creadas.

def realizar_descuento(numero: int) -> int:
    descuento = int(numero * 0.95)
    return descuento

def validar_y_realizar_descuento():
    numero_1 = validar_numero(10, 100)
    descuento = realizar_descuento(numero_1)
    print(f"El valor asignado es {numero_1}")
    print(f"El valor con el 5% de descuento es {mostrar_numero(descuento)}")


# Ejercicio 3-7: Realizar un programa que: asigne a las variables numero1 y numero2
# los valores solicitados al usuario, valide los mismos entre 10 y 100, asigne a la
# variable operacion el valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice
# la operación de dichos valores a través de una función. Mostrar el resultado por
# pantalla.

def sumaro_o_restar():
    numero_uno = validar_numero(9, 101)
    numero_dos = validar_numero(9, 101)
    operacion = input("Ingrese S si desea sumar, ingrese R si desea restar: ").lower()
    while operacion != "s" and operacion != "r":
        operacion = input("Opción incorrecta, ingrese S o R: ").lower()
    if operacion == "s":
        operacion = numero_uno + numero_dos
    elif operacion == "r":
        operacion = numero_uno - numero_dos
    return operacion

