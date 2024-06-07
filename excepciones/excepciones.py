
try:
    dividendo = 4
    divisor = "2"
    resultado = dividendo/divisor
    print(resultado)

except ZeroDivisionError:
    print("No se puede dividir por cero")
except NameError:
    print("La variable no existe")
except TypeError:
    print("Error de tipo")
else:   #opcional
    print("Calculos fue exitoso ")
finally:
    print("por bien o por mal, terminó el código.")