# Ejercicio 6:
# Utilizar For
# Dada la siguiente lista:
# [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
# mostrar el mayor.

def mostrar_mayor_numero():
    lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
    mayor_numero = None
    for numero in lista_numeros:
        if mayor_numero == None or mayor_numero < numero:
            mayor_numero = numero
    return mayor_numero

# Ejercicio 7:
# Dada la siguiente lista:
# [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
# mostrar solo los números pares.

def mostrar_numeros_pares():
    lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
    lista_pares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)
    return lista_pares


# Ejercicio 8:
# Dada la siguiente lista:
# [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
# mostrar el número repetido

def mostrar_numero_repetido():
    lista_numeros = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
    numeros_vistos = []
    for numero in lista_numeros:
        if numero in numeros_vistos:
            return numero
        else:
            numeros_vistos.append(numero)


# Ejercicio 9:
# Dadas las siguientes listas:
# edades = [25,36,18,23,45]
# nombre = ["Juan","Ana","Sol","Mario","Sonia"]
# y considerando que la posición en la lista corresponde a la misma persona,
# mostar el nombre de la persona más joven

def mostrar_persona_mas_joven():
    edades = [25, 36, 18, 23, 45]
    nombre = ["Juan", "Ana", "Sol", "Mario", "Sonia"]
    menor_numero = None
    persona_mas_joven = ""
    for i in range(len(edades)):
        if menor_numero == None or menor_numero > edades[i]:
            menor_numero = edades[i]
            persona_mas_joven = nombre[i]
    mensaje = print(f"La persona más joven es {persona_mas_joven}")
    return mensaje


# Ejercicio 10:
# Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
# respectivas listas. Validar el ingreso de datos según su criterio.
# Datos:
# nombre, sexo (f/m), nota (validar).
# Una vez cargados los datos:
# Mostrar el nombre del hombre con nota más baja
# Mostrar el promedio de notas de las mujeres
# Ejemplo:
# nombres = ["Juan","Pedro","Sol","Paco","Ana"]
# sexo = ["m","m","f","m","f"]
# nota = [6,8,10,8,5]

def mostrar_datos_alumnos():
    nombres = []
    sexos = []
    notas = []
    nota_mas_baja = None
    hombre_nota_mas_baja = ""
    acumulador_notas = 0
    contador_mujeres = 0
    promedio_mujeres = 0
    
    
    for i in range(5):
        nombre = input("Ingrese su nombre: ").lower()
        while nombre is None:
            nombre = input("Incorrecto, ingrese nuevamente: ").lower()
        nombres.append(nombre)
        
        sexo = input("Ingrese su sexo f o m: ").lower()
        while sexo != "f" and sexo != "m":
            sexo = input("Incorrecto, ingrese nuevamente: ").lower()
        sexos.append(sexo)
        
        nota = int(input("Ingrese su nota: "))
        while nota > 10 or nota < 0:
            nota = int(input("Ingrese nuevamente: "))
        notas.append(nota)
    
    for i in range(len(nombres)):
        if sexos[i] == "m": 
            if nota_mas_baja is None or nota_mas_baja > notas[i]:
                nota_mas_baja = notas[i]
                hombre_nota_mas_baja = nombres[i]
        elif sexos[i] == "f":
            acumulador_notas += notas[i]
            contador_mujeres += 1
    promedio_mujeres = acumulador_notas // contador_mujeres
    mensaje = print(f"""el hombre con nota más baja es {hombre_nota_mas_baja}
    y su nota es {nota_mas_baja}
    el promedio de nota de mujeres es {promedio_mujeres}""")
    return mensaje
