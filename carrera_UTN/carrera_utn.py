import pygame as pg
from constantes_utn import *
from datos_utn import lista
import json

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
nombre = ""

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

boton_comenzar = fuente.render(str("Comenzar"), True, NEGRO)
boton_terminar = fuente.render(str("Terminar"), True, NEGRO)


texto_pregunta = fuente_dos.render(str(pregunta), True, NEGRO)
texto_respuesta_a_ = fuente_dos.render(str(respuesta_a), True, COLOR_AMARILLO)
texto_respuesta_b_ = fuente_dos.render(str(respuesta_b), True, COLOR_AMARILLO)
texto_respuesta_c_ = fuente_dos.render(str(respuesta_c), True, COLOR_AMARILLO)
texto_score = fuente_dos.render(str("SCORE"), True, COLOR_GRIS)
texto_puntuacion = fuente_dos.render(str("0"), True, COLOR_GRIS)
texto_tiempo = fuente.render(str("Tiempo: "), True, NEGRO)
texto_tiempo_numero = fuente.render(str("0"), True, NEGRO)
texto_score = fuente.render(str("Puntaje: "), True, NEGRO)
texto_puntuacion = fuente.render(str("0"), True, NEGRO)

texto_avanza_uno = fuente_tres.render(str("Avanza 1"), True, NEGRO)
texto_retrocede_uno = fuente_tres.render(str("Retrocede 1"), True, NEGRO)
texto_salida = fuente_dos.render(str("SALIDA"), True, NEGRO)
texto_llegada = fuente_dos.render(str("LLEGADA"), True, NEGRO)

imagen_logo = pg.image.load("carrera_UTN\logo_carrera_utn.png")
imagen_logo = pg.transform.scale(imagen_logo, (220, 120))
rect_logo = pg.Rect(200, 400, 150, 40)

imagen_personaje = pg.image.load("carrera_UTN\messi_.png")
imagen_personaje = pg.transform.scale(imagen_personaje, (40, 70))
rect_personaje = pg.Rect(120, 240, 150, 40)

imagen_llegada = pg.image.load("carrera_UTN\llegada.png")
imagen_llegada = pg.transform.scale(imagen_llegada, (130, 40))
rect_llegada = pg.Rect(100, 200, 150, 40)

timer_segundos = pg.USEREVENT
pg.time.set_timer(timer_segundos, 1000) # 1000 es un segundo
segundos = "5"
fin_tiempo = False

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


#
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
        texto = fuente.render(f"{i + 1} {puntaje['nombre'].capitalize()} - {puntaje['puntaje']}", True, NEGRO)
        screen.blit(texto, (100, y))
        y += 30
    pg.display.flip()
    pg.time.wait(5000)
#


mostrando_puntajes = False 
flag_run = True
while flag_run:
    lista_eventos = pg.event.get()
    for evento in lista_eventos:
        if evento.type == pg.QUIT:
            flag_run = False
        if evento.type == pg.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            print(posicion_click)

            if posicion_click[0] > 150 and posicion_click[0] < 310 and posicion_click[1] > 520 and posicion_click[1] < 600:
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
            
            if posicion_click[0] > 450 and posicion_click[0] < 650 and posicion_click[1] > 520 and posicion_click[1] < 600:
                nombre = pedir_nombre()
                if nombre:
                    guardar_puntaje(nombre, puntuacion)
                    mostrar_mejores_puntajes()
                pregunta = ""
                respuesta_a = ""
                respuesta_b = ""
                respuesta_c = ""
                texto_pregunta_lineas = []
                texto_respuesta_a = []
                texto_respuesta_b = []
                texto_respuesta_c = []
                puntuacion = 0
                contador = 0
                segundos = 5
                rect_personaje = pg.Rect(120, 240, 150, 40)
                tiempo_iniciado = False
            
            if tiempo_iniciado:  
                if posicion_click[0] > 245 and posicion_click[0] < 320 and posicion_click[1] > 150 and posicion_click[1] < 190:
                    respuesta_elegida = "a"
                elif posicion_click[0] > 375 and posicion_click[0] < 455 and posicion_click[1] > 150 and posicion_click[1] < 190:
                    respuesta_elegida = "b"
                elif posicion_click[0] > 500 and posicion_click[0] < 570 and posicion_click[1] > 150 and posicion_click[1] < 190:
                    respuesta_elegida = "c"
                else:
                    respuesta_elegida = None
                
                if respuesta_elegida == respuesta_correcta:
                    puntuacion += 10
                    if rect_personaje.x < 570 and rect_personaje.y < 375: #mover de a dos casilleros 
                        rect_personaje.move_ip(130, 0)
                    elif rect_personaje.x > 570 and rect_personaje.x < 630 and rect_personaje.y < 375: #saltar a la fila de abajo
                        rect_personaje.x = 640
                        rect_personaje.y = 375
                    elif rect_personaje.x > 630 and rect_personaje.y < 375:  #saltar a la fila de abajo
                        rect_personaje.x = 570
                        rect_personaje.y = 375
                    elif rect_personaje.x > 70 and rect_personaje.y > 370: #avanzar en fila de abajo
                        rect_personaje.move_ip(-130, 0)
                    elif rect_personaje.x < 300 and rect_personaje.y > 375:  #va a la llegada en cualquiera de los ultimos dos casilleros
                        rect_personaje.x = 70
                        rect_personaje.y = 375
                
                elif respuesta_elegida is not respuesta_correcta and respuesta_elegida is not None:
                    if rect_personaje.x == 120 and rect_personaje.y == 240:
                        rect_personaje.x = 120
                        rect_personaje.y = 240
                    elif rect_personaje.x < 700 and rect_personaje.y < 375:
                        rect_personaje.move_ip(-65, 0)
                    elif rect_personaje.x > 630 and rect_personaje.y > 350:
                        rect_personaje.x = 635
                        rect_personaje.y = 250
                    elif rect_personaje.x > 70 and rect_personaje.y > 370:
                        rect_personaje.move_ip(65, 0)
                
                texto_puntuacion = fuente.render(str(puntuacion), True, NEGRO)
                
                if contador < len(lista_preguntas):
                    pregunta = lista_preguntas[contador]
                    respuesta_a = lista_respuesta_a[contador]
                    respuesta_b = lista_respuesta_b[contador]
                    respuesta_c = lista_respuesta_c[contador]
                    respuesta_correcta = lista_respuesta_correcta[contador]
                    texto_pregunta_lineas = render_text(pregunta, fuente_dos, NEGRO, 350)
                    texto_respuesta_a = render_text(respuesta_a, fuente_dos, COLOR_AMARILLO, 100)
                    texto_respuesta_b = render_text(respuesta_b, fuente_dos, COLOR_AMARILLO, 100)
                    texto_respuesta_c = render_text(respuesta_c, fuente_dos, COLOR_AMARILLO, 100)
                    segundos = 5  # Reiniciar el temporizador para la siguiente pregunta
                else:
                    fin_tiempo = True
                contador += 1
        
        if evento.type == timer_segundos and tiempo_iniciado:
            if not fin_tiempo:
                segundos -= 1
                if segundos == 0:
                    contador += 1
                    if contador < len(lista_preguntas):
                        pregunta = lista_preguntas[contador]
                        respuesta_a = lista_respuesta_a[contador]
                        respuesta_b = lista_respuesta_b[contador]
                        respuesta_c = lista_respuesta_c[contador]
                        respuesta_correcta = lista_respuesta_correcta[contador]
                        texto_pregunta_lineas = render_text(pregunta, fuente_dos, NEGRO, 350)
                        texto_respuesta_a = render_text(respuesta_a, fuente_dos, COLOR_AMARILLO, 100)
                        texto_respuesta_b = render_text(respuesta_b, fuente_dos, COLOR_AMARILLO, 100)
                        texto_respuesta_c = render_text(respuesta_c, fuente_dos, COLOR_AMARILLO, 100)
                        segundos = 5  # Reiniciar temporizador
                    else:
                        fin_tiempo = True
        
    
    if rect_personaje.colliderect(rect_llegada):
        nombre = pedir_nombre()
        if nombre:
            guardar_puntaje(nombre, puntuacion)
            mostrar_mejores_puntajes()
        
    if rect_personaje.x > 505 and rect_personaje.x < 560 and rect_personaje.y < 340:
        rect_personaje.move_ip(65, 0)
    elif rect_personaje.x > 375 and rect_personaje.x < 435 and rect_personaje.y > 340:
        rect_personaje.move_ip(65, 0)
    
    
    screen.fill(STEELBLUE)
    
    pg.draw.rect(screen, STEELBLUE3, (450, 520, 200, 80), border_radius=15)
    pg.draw.rect(screen, STEELBLUE3, (150, 520, 200, 80), border_radius=15)
    
    pg.draw.rect(screen, BLACK, (239, 9, 352, 202))
    pg.draw.rect(screen, GREEN, (240, 10, 350, 200))
    
    pg.draw.rect(screen, CORAL1, (180, 280, 60, 60), border_radius=15)
    pg.draw.rect(screen, GRAY63, (245, 280, 60, 60), border_radius=15)
    pg.draw.rect(screen, YELLOW3, (310, 280, 60, 60), border_radius=15)
    pg.draw.rect(screen, SKYBLUE3, (375, 280, 60, 60), border_radius=15)
    pg.draw.rect(screen, RED2, (440, 280, 60, 60),  border_radius=15)
    pg.draw.rect(screen, VIOLETRED1, (505, 280, 60, 60), border_radius=15)
    pg.draw.rect(screen, PINK, (570, 280, 60, 60), border_radius=15)
    pg.draw.rect(screen, GREEN, (635, 280, 60, 60), border_radius=15)
    
    pg.draw.rect(screen, CORAL1, (180, 400, 60, 60), border_radius=15)
    pg.draw.rect(screen, GRAY63, (245, 400, 60, 60), border_radius=15)
    pg.draw.rect(screen, YELLOW3, (310, 400, 60, 60), border_radius=15)
    pg.draw.rect(screen, SKYBLUE3, (375, 400, 60, 60), border_radius=15)
    pg.draw.rect(screen, RED2, (440, 400, 60, 60), border_radius=15)
    pg.draw.rect(screen, VIOLETRED1, (505, 400, 60, 60), border_radius=15)
    pg.draw.rect(screen, PINK, (570, 400, 60, 60), border_radius=15)
    pg.draw.rect(screen, GREEN, (635, 400, 60, 60), border_radius=15)
    
    screen.blit(imagen_logo, (10, 10))
    screen.blit(imagen_llegada, (40, 410))
    screen.blit(imagen_personaje, (rect_personaje.x, rect_personaje.y))
    
    screen.blit(boton_comenzar, (185, 540,22,22))
    screen.blit(boton_terminar, (485, 540,22,22))
    
    screen.blit(texto_tiempo, (610, 35))
    screen.blit(texto_score, (610, 100))
    screen.blit(texto_puntuacion, (740, 100))
    
    for i, linea in enumerate(texto_pregunta_lineas):
        screen.blit(linea, (245, 30 + i * 30))
    for i, linea in enumerate(texto_respuesta_a):
        screen.blit(linea, (245, 150 + i * 30))
    for i, linea in enumerate(texto_respuesta_b):
        screen.blit(linea, (375, 150 + i * 30))
    for i, linea in enumerate(texto_respuesta_c):
        screen.blit(linea, (500, 150 + i * 30))
    
    screen.blit(texto_llegada, (70, 450))
    screen.blit(texto_salida, (100, 320))
    screen.blit(texto_avanza_uno, (509, 303))
    screen.blit(texto_retrocede_uno, (376, 425))
    
    segundos_texto = fuente.render(str(segundos), True, NEGRO)
    screen.blit(segundos_texto, (740, 35))
    
    pg.display.flip()
pg.quit()