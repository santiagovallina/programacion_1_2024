# Santiago Vallina

# Ejercicio 1: Crear una función lambda que incremente un 10% en el sueldo recibido.
incrementar_sueldo = (lambda num: num * 0.10 + num)(100)

# Ejercicio 2: Crear una función lambda que informe si una persona es mayor (mayor a
#17 años) o menor.
mayor_menor_edad = (lambda num: "Mayor de edad" if num > 17 else "Menor de edad")(17)

# Ejercicio 3: Crear una función lambda que indique si el número recibido es par o
# impar.
numero = int(input("Ingrese un número: "))
par_o_impar = (lambda numero: "Numero par" if numero % 2 == 0 else "Numero impar")(numero)

# Ejercicio 4: Crear una función lambda que indique si el número recibido es positivo o
# negativo.
positivo_o_negativo =(lambda numero: "numero negativo" if numero < 0 else "numero positivo" )(numero) 
print(positivo_o_negativo)


# Ejercicio 5: Crear una función lambda que realice un 10% de descuento en el
# importe recibido.
descuento = (lambda numero: numero * 0.90)(numero)

# Ejercicio 6: Crear una función lambda devuelva el doble del número recibido.
devolver_doble = (lambda numero: numero * 2)(numero)

# Ejercicio 7: Crear una función lambda que devuelva el texto “femenino” si recibe el
# valor “f” y sino “masculino”.
# # genero = input("Ingrese genero F o M: ").lower()
# while genero != "f" and genero != "m":
#     genero = input("Ingrese genero F o M: ").lower()
# mostrar_genero = (lambda genero: "Femenino" if genero == "f" else "Masculino")(genero)