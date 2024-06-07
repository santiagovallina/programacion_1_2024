#Clase 1

# 1) Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
#sueldo para esa persona.

def mostrar_aumento_sueldo():
    nombre = input("Ingrese su nombre: ")
    sueldo = int(input("Ingrese su sueldo: "))
    aumento_sueldo = (sueldo * 10) / 100
    sueldo_total = sueldo + aumento_sueldo
    print(f"Su sueldo ahora es de {sueldo_total}")


# 2) Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
# adolescente (entre 13 y 17 años) o niño (menor a 13 años).

def pedir_edad ():
    edad = int(input("Ingrese su edad: "))
    while edad < 0:
        edad = int(input("Ingrese su edad: "))
    if edad > 18:
        print("Usted es mayor de edad")
    elif edad >= 13 and edad <= 17:
        print("Usted es adolescente")
    else: 
        print("Usted es un niño")

# Ejercicio 3:
# Ingresar 5 números enteros, distintos de cero.
# Informar:
# a. Cantidad de pares e impares.
# b. El menor número ingresado.
# c. De los pares el mayor número ingresado.
# d. Suma de los positivos.
# e. Producto de los negativos.

def calcular_numeros():
    numeros = []
    numeros_pares = []
    acumulador_numeros_pares = 0
    acumulador_numeros_impares = 0
    menor_numero = None
    mayor_numero_par = None
    suma_positivos = 0
    producto_negativos = 1
    
    for i in range(5):
        numero = int(input("Ingrese un número:"))
        while numero == 0:
            numero = int(input("Ingrese un número:"))
        numeros.append(numero)
        
        if numeros[i] % 2 == 0:
            acumulador_numeros_pares += 1
            numeros_pares.append(numeros[i])
            if mayor_numero_par == None or mayor_numero_par < numeros_pares[-1]:
                mayor_numero_par = numeros_pares[-1]
        else:
            acumulador_numeros_impares += 1
        
        if menor_numero == None or menor_numero > numeros[i]:
            menor_numero = numeros[i]
        
        if numero >= 0:
            suma_positivos += numero
        else:
            producto_negativos *= numero
    
    print(f"""
        Cantidad de numeros pares: {acumulador_numeros_pares}
        cantidad de numeros impares: {acumulador_numeros_impares}
        Menor número ingresado: {menor_numero}
        Mayor número par: {mayor_numero_par}
        Suma de los positivos: {suma_positivos}
        Producto de los negativos: {producto_negativos}""")


# Ejercicio 4: Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
#distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO ser soltero.'

def edad_y_estado_civil():
    edad = int(input("Ingrese su edad: "))
    estado_civil = input("Ingrese su estado civil: ")
    if edad < 18 and estado_civil != "soltero":
        print("Es muy pequeño para NO ser soltero.")


# Ejercicio 5:
# Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
# por cada estadía como base, se pide el ingreso de una estación del
# año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
# Plata/Córdoba) para vacacionar para poder calcular el precio final:
# -en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
# descuento del 10% Mar del Plata tiene un descuento del 20%
# -en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
# un aumento del 10% Mar del Plata tiene un aumento del 20%
# -en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
# aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
# precio sin descuento.
# Validar el ingreso de datos

def sacar_tarifas_viajes():
    estadia = 15000
    precio_total = 0
    estaciones_validas = ["invierno", "verano", "primavera", "otoño"]
    destinos_validos = ["bariloche", "mar del plata", "cataratas", "cordoba"]
    
    estacion_del_año = input("Ingrese la estación del año: ").lower()
    while estacion_del_año not in estaciones_validas:
        estacion_del_año = input("Estación inválida. Ingrese nuevamente: ").lower()

    localidad = input("Ingrese la localidad: ").lower()
    while localidad not in destinos_validos:
        localidad = input("Localidad inválida. Ingrese nuevamente: ").lower()
    
    cantidad_de_estadias = int(input("Ingrese la cantidad de estadias: "))
    while cantidad_de_estadias < 1:
        cantidad_de_estadias = int(input("Ingrese la cantidad de estadias: "))
    
    if estacion_del_año == "invierno":
        match localidad:
            case "bariloche":
                precio_total = estadia + estadia * 0.20
            case "cataratas" | "cordoba":
                precio_total = estadia - estadia * 0.10
            case "mar del plata":
                precio_total = estadia - estadia * 0.20
    
    if estacion_del_año == "verano":
        match localidad:
            case "bariloche":
                precio_total = estadia - estadia * 0.20
            case "cataratas" | "cordoba":
                precio_total = estadia + estadia * 0.10
            case "mar del plata":
                precio_total = estadia + estadia * 0.20
    
    if estacion_del_año == "primavera" or estacion_del_año == "otoño":
        match localidad:
            case "bariloche" | "mar del plata" | "cataratas":
                precio_total = estadia + estadia * 0.10
            case "cordoba":
                precio_total = estadia
    
    precio_total = precio_total * cantidad_de_estadias
    print(f"El precio de su viaje a {localidad} es de ${precio_total}")


print(mostrar_aumento_sueldo())
print(pedir_edad())
print(calcular_numeros())
print(edad_y_estado_civil())
print(sacar_tarifas_viajes())
