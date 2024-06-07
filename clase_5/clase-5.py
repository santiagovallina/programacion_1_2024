def potencia(base: int, exponente: int) -> int:
    '''
    Recibe un número para la base y otro para el exponente.
    Calcula la potencia.
    Retorna el resultado.
    '''
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


def encontrar_numeros_primos(numero: int) -> bool:
    '''
    Recibe un número. Calcula si el número es primo o no.
    Retorna el resultado.
    '''
    pass


def pedir_numero() -> bool:
    '''
    Recibe un número. Determina si es par o no.
    Retorna un booleano.
    '''
    numero_ingresado = int(input("Ingrese un numero: "))
    numero_primo = True if numero_ingresado % 2 == 0 else False
    return numero_primo


#LAMBDA
sumar = lambda x, y: x + y
#print(sumar(2, 7))

#print((lambda num: "Es par" if num % 2 == 0 else "Es impar")(7))





#BURBUJEO
lista_de_numeros = [2, 1, 5, 34, 6, 7, 5, 99]
aux = 0

for i in range(len(lista_de_numeros)- 1):
    for k in range(i + 1, len(lista_de_numeros)):
        if lista_de_numeros[i] > lista_de_numeros[k]:
            #SWAP
            aux = lista_de_numeros[i]
            lista_de_numeros[i] = lista_de_numeros[k]
            lista_de_numeros[k] = aux
print(lista_de_numeros)