jugadores = [
    {"nombre" : "Ana", "edad" : 43, "puntos" : [10, 12, 14]},
    {"nombre" : "Juan", "edad" : 32, "puntos" : [12, 10, 11]},
    {"nombre" : "Pedro", "edad" : 28, "puntos" : [9, 15, 11]},
    {"nombre" : "Sol", "edad" : 31, "puntos" : [11, 8, 15]},
]

# Acumular puntos de cada jugador.
acumulador = 0
for e_jugador in jugadores:
    for i in range(0, len(e_jugador["puntos"])):
        acumulador += e_jugador["puntos"][i]
    print(e_jugador["nombre"], f"Total de puntos: {acumulador}")
    acumulador = 0


# Ver puntos de un jugador en particular.
print(jugadores[1]["puntos"]) #De Juan, que está en el índice 1, muestra los puntos.

# Ver un dato de un jugador en particular.
print(jugadores[1]["nombre"])

# Ver todos los nombres.
for e_jugador in jugadores:
    print(e_jugador["nombre"])


# Buscar el menor de edad y mostrar su nombre.
min = jugadores[0]["edad"]
nombre = jugadores[0]["nombre"]
for e_jugador in jugadores:
    if e_jugador["edad"] < min:
        min = e_jugador["edad"]
        nombre = e_jugador["nombre"]
print(f"El menor es {nombre} y tiene {min} años.")


# Ordenar de manera descendente por nombre.
for i in range(len(jugadores)-1):
    for j in range(i+1, len(jugadores)):
        if jugadores[i]["nombre"] < jugadores[j]["nombre"]:
            aux_jugadores = jugadores[i]
            jugadores[i] = jugadores[j]
            jugadores[j] = aux_jugadores
print("ordenado")
for e_jugador in jugadores:
    print(e_jugador)

# Determinar nombre del/los jugadores con menos de 10 puntos en algun juego
