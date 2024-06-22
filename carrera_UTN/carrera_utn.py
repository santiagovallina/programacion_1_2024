import pygame as pg
from constantes_utn import *
from datos_utn import lista

pregunta = ""
tema = ""
respuesta_a = ""
respuesta_b = ""
respuesta_c = ""
respuesta_correcta = ""
respuesta_elegida = ""
lista_preguntas = []
lista_temas = []
lista_respuesta_a = []
lista_respuesta_b = []
lista_respuesta_c = []
lista_respuesta_correcta = []
timepo = 0
contador = 0
puntuacion = 0

for e_lista in lista:
    lista_preguntas.append(e_lista["pregunta"])
    lista_temas.append(e_lista["tema"])
    lista_respuesta_a.append(e_lista["a"])
    lista_respuesta_b.append(e_lista["b"])
    lista_respuesta_c.append(e_lista["c"])
    lista_respuesta_correcta.append(e_lista["correcta"])


pg.init()

fuente = pg.font.SysFont("Arial", 30)
fuente_dos = pg.font.SysFont("Arial", 18)

boton_comenzar = fuente.render(str("Comenzar"), True, NEGRO)
boton_terminar = fuente.render(str("Terminar"), True, NEGRO)

imagen_logo = pg.image.load("carrera_UTN\logo_carrera_utn.png")
imagen_logo = pg.transform.scale(imagen_logo, (220, 120))
rect_logo = pg.Rect(200, 400, 150, 40)

imagen_personaje = pg.image.load("carrera_UTN\messi_.png")
imagen_personaje = pg.transform.scale(imagen_personaje, (40, 70))
rect_personaje = pg.Rect(100, 200, 150, 40)

imagen_llegada = pg.image.load("carrera_UTN\llegada.png")
imagen_llegada = pg.transform.scale(imagen_llegada, (130, 40))
rect_llegada = pg.Rect(100, 200, 150, 40)

texto_tiempo = fuente.render(str("Tiempo: "), True, NEGRO)
texto_tiempo_numero = fuente.render(str("0"), True, NEGRO)

texto_score = fuente.render(str("Puntaje: "), True, NEGRO)
texto_puntuacion = fuente.render(str("0"), True, NEGRO)

screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pg.display.set_caption("Carrera UTN")


flag_run = True
while flag_run:
    lista_eventos = pg.event.get()
    for evento in lista_eventos:
        if evento.type == pg.QUIT:
            flag_run = False
        if evento.type == pg.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            print(posicion_click) 





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
    screen.blit(imagen_personaje, (100, 250))
    screen.blit(imagen_llegada, (40, 410))
    
    screen.blit(boton_comenzar, (185, 540,22,22))
    screen.blit(boton_terminar, (485, 540,22,22))
    
    screen.blit(texto_tiempo, (610, 35))
    screen.blit(texto_tiempo_numero, (740, 35))
    screen.blit(texto_score, (610, 100))
    screen.blit(texto_puntuacion, (740, 100))
    
    
    pg.display.flip()

















pg.quit()