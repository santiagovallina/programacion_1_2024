import pygame as pg
import json
from constantes_utn import *
from datos_utn import lista

# Inicializar variables
pregunta = ""
texto_pregunta_lineas = []
texto_respuesta_a = []
texto_respuesta_b = []
texto_respuesta_c = []
respuesta_a = ""
respuesta_b = ""
respuesta_c = ""
respuesta_correcta = ""
respuesta_elegida = ""
lista_preguntas = []
lista_respuesta_a = []
lista_respuesta_b = []
lista_respuesta_c = []
lista_respuesta_correcta = []
tiempo = 0
contador = 0
puntuacion = 0
tiempo_iniciado = False
fin_tiempo = False

for e_lista in lista:
    lista_preguntas.append(e_lista["pregunta"])
    lista_respuesta_a.append(e_lista["a"])
    lista_respuesta_b.append(e_lista["b"])
    lista_respuesta_c.append(e_lista["c"])
    lista_respuesta_correcta.append(e_lista["correcta"])

pg.init()

fuente = pg.font.SysFont("Arial", 30)
fuente_dos = pg.font.SysFont("Arial", 18)
fuente_tres = pg.font.SysFont("Arial", 10)

boton_comenzar = fuente.render("Comenzar", True, NEGRO)
boton_terminar = fuente.render("Terminar", True, NEGRO)

texto_pregunta = fuente_dos.render(pregunta, True, NEGRO)
texto_respuesta_a_ = fuente_dos.render(respuesta_a, True, COLOR_AMARILLO)
texto_respuesta_b_ = fuente_dos.render(respuesta_b, True, COLOR_AMARILLO)
texto_respuesta_c_ = fuente_dos.render(respuesta_c, True, COLOR_AMARILLO)
texto_score = fuente_dos.render("SCORE", True, COLOR_GRIS)
texto_puntuacion = fuente_dos.render("0", True, COLOR_GRIS)
texto_tiempo = fuente.render("Tiempo: ", True, NEGRO)
texto_tiempo_numero = fuente.render("0", True, NEGRO)
texto_score = fuente.render("Puntaje: ", True, NEGRO)
texto_puntuacion = fuente.render("0", True, NEGRO)

texto_avanza_uno = fuente_tres.render("Avanza 1", True, NEGRO)
texto_retrocede_uno = fuente_tres.render("Retrocede 1", True, NEGRO)
texto_salida = fuente_dos.render("SALIDA", True, NEGRO)
texto_llegada = fuente_dos.render("LLEGADA", True, NEGRO)

imagen_logo = pg.image.load("carrera_UTN/logo_carrera_utn.png")
imagen_logo = pg.transform.scale(imagen_logo, (220, 120))
rect_logo = pg.Rect(200, 400, 150, 40)

imagen_personaje = pg.image.load("carrera_UTN/messi_.png")
imagen_personaje = pg.transform.scale(imagen_personaje, (40, 70))
rect_personaje = pg.Rect(120, 240, 150, 40)

imagen_llegada = pg.image.load("carrera_UTN/llegada.png")
imagen_llegada = pg.transform.scale(imagen_llegada, (130, 40))
rect_llegada = pg.Rect(100, 200, 150, 40)

timer_segundos = pg.USEREVENT
pg.time.set_timer(timer_segundos, 1000)  # 1000 es un segundo
segundos = 5

screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pg.display.set_caption("Carrera UTN")


def render_text(texto, fuente, color, max_ancho):
    palabras = texto.split(' ')
    lineas = []
    linea_actual = palabras[0]

    for palabra in palabras[1:]:
        if fuente.size(linea_actual + ' ' + palabra)[0] <= max_ancho:
            linea_actual += ' ' + palabra
        else:
            lineas.append(linea_actual)
            linea_actual = palabra

    lineas.append(linea_actual)
    return [fuente.render(linea, True, color) for linea in lineas]


def pedir_nombre():
    nombre = ""
    while True:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                return None
            elif evento.type == pg.KEYDOWN:
                if evento.key == pg.K_RETURN:
                    return nombre
                elif evento.key == pg.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += evento.unicode

        screen.fill(STEELBLUE)
        texto = fuente.render("Ingrese su nombre: " + nombre, True, NEGRO)
        screen.blit(texto, (100, 200))
        pg.display.flip()


def guardar_puntaje(nombre, puntaje):
    archivo_puntajes = "puntajes.json"
    try:
        with open(archivo_puntajes, "r") as archivo:
            puntajes = json.load(archivo)
    except FileNotFoundError:
        puntajes = []

    puntajes.append({"nombre": nombre, "puntaje": puntaje})
    puntajes = sorted(puntajes, key=lambda x: x["puntaje"], reverse=True)[:10]

    with open(archivo_puntajes, "w") as archivo:
        json.dump(puntajes, archivo)


def mostrar_mejores_puntajes():
    archivo_puntajes = "puntajes.json"
    try:
        with open(archivo_puntajes, "r") as archivo:
            puntajes = json.load(archivo)
    except FileNotFoundError:
        puntajes = []

    screen.fill(STEELBLUE)
    y = 50
    for i, puntaje in enumerate(puntajes):
        texto = fuente_dos.render(f"{i + 1}. {puntaje['nombre']} - {puntaje['puntaje']}", True, NEGRO)
        screen.blit(texto, (100, y))
        y += 30

    pg.display.flip()
    pg.time.wait(5000)


flag_run = True
while flag_run:
    lista_eventos = pg.event.get()
    for evento in lista_eventos:
        if evento.type == pg.QUIT:
            flag_run = False
        if evento.type == pg.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)

            if 150 < posicion_click[0] < 310 and 520 < posicion_click[1] < 600:
                pregunta = lista_preguntas[contador]
                respuesta_a = lista_respuesta_a[contador]
                respuesta_b = lista_respuesta_b[contador]
                respuesta_c = lista_respuesta_c[contador]
                respuesta_correcta = lista_respuesta_correcta[contador]
                texto_pregunta_lineas = render_text(pregunta, fuente_dos, NEGRO, 350)
                texto_respuesta_a = render_text(respuesta_a, fuente_dos, COLOR_AMARILLO, 100)
                texto_respuesta_b = render_text(respuesta_b, fuente_dos, COLOR_AMARILLO, 100)
                texto_respuesta_c = render_text(respuesta_c, fuente_dos, COLOR_AMARILLO, 100)
                tiempo_iniciado = True
                segundos = 5

            if 450 < posicion_click[0] < 650 and 520 < posicion_click[1] < 600:
                nombre = pedir_nombre()
                if nombre:
                    guardar_puntaje(nombre, puntuacion)
                    mostrar_mejores_puntajes()
                flag_run = False

            if tiempo_iniciado:
                if 245 < posicion_click[0] < 320 and 150 < posicion_click[1] < 190:
                    respuesta_elegida = "a"
                elif 375 < posicion_click[0] < 455 and 150 < posicion_click[1] < 190:
                    respuesta_elegida = "b"
                elif 500 < posicion_click[0] < 570 and 150 < posicion_click[1] < 190:
                    respuesta_elegida = "c"
                else:
                    respuesta_elegida = None

                if respuesta_elegida == respuesta_correcta:
                    puntuacion += 10
                    if rect_personaje.x < 570 and rect_personaje.y < 375:  # mover de a dos casilleros
                        rect_personaje.move_ip(130, 0)
                    elif rect_personaje.x > 570 and rect_personaje.x < 630 and rect_personaje.y < 375:  # saltar a la fila de abajo
                        rect_personaje.x = 640
                        rect_personaje.y = 375
                    elif rect_personaje.x > 630 and rect_personaje.y < 375:  # saltar a la fila de abajo
                        rect_personaje.x = 570
                        rect_personaje.y = 375
                    elif rect_personaje.x > 70 and rect_personaje.x < 250 and rect_personaje.y == 375:  # mover de a dos casilleros
                        rect_personaje.move_ip(-130, 0)
                    elif rect_personaje.x == 70 and rect_personaje.y == 375:  # mover de a dos casilleros y saltar a la fila de abajo
                        rect_personaje.x = 70
                        rect_personaje.y = 510
                    elif rect_personaje.x < 570 and rect_personaje.y > 370:  # mover de a dos casilleros
                        rect_personaje.move_ip(130, 0)
                    elif rect_personaje.x > 570 and rect_personaje.y > 370:  # saltar a la fila de abajo
                        rect_personaje.x = 70
                        rect_personaje.y = 640

                else:
                    puntuacion -= 5
                    if rect_personaje.x < 570 and rect_personaje.y < 375:  # mover de a un casillero
                        rect_personaje.move_ip(130, 0)
                    elif rect_personaje.x > 570 and rect_personaje.x < 640 and rect_personaje.y < 375:  # saltar a la fila de abajo
                        rect_personaje.x = 640
                        rect_personaje.y = 375
                    elif rect_personaje.x > 630 and rect_personaje.y < 375:  # saltar a la fila de abajo
                        rect_personaje.x = 570
                        rect_personaje.y = 375
                    elif rect_personaje.x > 70 and rect_personaje.x < 250 and rect_personaje.y == 375:  # mover de a un casillero
                        rect_personaje.move_ip(-130, 0)
                    elif rect_personaje.x == 70 and rect_personaje.y == 375:  # mover de a un casillero y saltar a la fila de abajo
                        rect_personaje.x = 70
                        rect_personaje.y = 510
                    elif rect_personaje.x < 570 and rect_personaje.y > 370:  # mover de a un casillero
                        rect_personaje.move_ip(130, 0)
                    elif rect_personaje.x > 570 and rect_personaje.y > 370:  # saltar a la fila de abajo
                        rect_personaje.x = 70
                        rect_personaje.y = 640

            texto_puntuacion = fuente_dos.render(str(puntuacion), True, COLOR_GRIS)

    if tiempo_iniciado and evento.type == timer_segundos:
        segundos -= 1
        if segundos == 0:
            tiempo_iniciado = False
            pregunta = ""
            respuesta_a = ""
            respuesta_b = ""
            respuesta_c = ""
            respuesta_correcta = ""
            respuesta_elegida = ""
            texto_pregunta_lineas = []
            texto_respuesta_a = []
            texto_respuesta_b = []
            texto_respuesta_c = []
            contador += 1
            if contador >= len(lista_preguntas):
                contador = 0

    if rect_personaje.colliderect(rect_llegada):
        nombre = pedir_nombre()
        if nombre:
            guardar_puntaje(nombre, puntuacion)
            mostrar_mejores_puntajes()
        flag_run = False

    screen.fill(STEELBLUE)

    pg.draw.rect(screen, COLOR_GRIS, (150, 520, 160, 80))
    screen.blit(boton_comenzar, (160, 540))

    pg.draw.rect(screen, COLOR_GRIS, (450, 520, 200, 80))
    screen.blit(boton_terminar, (460, 540))

    pg.draw.line(screen, NEGRO, (60, 80), (710, 80), 10)
    pg.draw.line(screen, NEGRO, (60, 220), (710, 220), 10)
    pg.draw.line(screen, NEGRO, (60, 360), (710, 360), 10)
    pg.draw.line(screen, NEGRO, (60, 500), (710, 500), 10)
    pg.draw.line(screen, NEGRO, (60, 640), (710, 640), 10)

    screen.blit(texto_salida, (10, 65))
    screen.blit(texto_llegada, (10, 625))

    pg.draw.line(screen, NEGRO, (60, 80), (60, 640), 10)
    pg.draw.line(screen, NEGRO, (710, 80), (710, 640), 10)

    pg.draw.line(screen, COLOR_GRIS, (710, 150), (60, 150), 10)
    screen.blit(texto_avanza_uno, (5, 130))

    pg.draw.line(screen, COLOR_GRIS, (60, 300), (710, 300), 10)
    screen.blit(texto_retrocede_uno, (5, 280))

    pg.draw.line(screen, COLOR_GRIS, (710, 440), (60, 440), 10)
    screen.blit(texto_avanza_uno, (5, 420))

    pg.draw.line(screen, COLOR_GRIS, (60, 580), (710, 580), 10)
    screen.blit(texto_retrocede_uno, (5, 560))

    screen.blit(imagen_logo, rect_logo)

    screen.blit(texto_pregunta, (160, 100))

    screen.blit(texto_tiempo, (700, 10))
    texto_tiempo_numero = fuente.render(str(segundos), True, NEGRO)
    screen.blit(texto_tiempo_numero, (850, 10))

    screen.blit(texto_score, (700, 50))
    screen.blit(texto_puntuacion, (850, 50))

    screen.blit(imagen_personaje, rect_personaje)
    screen.blit(imagen_llegada, rect_llegada)

    if texto_pregunta_lineas:
        for i, linea in enumerate(texto_pregunta_lineas):
            screen.blit(linea, (160, 100 + i * 20))

    if texto_respuesta_a:
        for i, linea in enumerate(texto_respuesta_a):
            screen.blit(linea, (245, 150 + i * 20))

    if texto_respuesta_b:
        for i, linea in enumerate(texto_respuesta_b):
            screen.blit(linea, (375, 150 + i * 20))

    if texto_respuesta_c:
        for i, linea in enumerate(texto_respuesta_c):
            screen.blit(linea, (500, 150 + i * 20))

    pg.display.flip()

pg.quit()


