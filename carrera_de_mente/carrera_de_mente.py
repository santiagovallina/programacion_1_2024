from constantes import *
import pygame as pg
from datos import lista

lista_datos = []
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
contador = 0
puntuacion = 0
repetir = 1
intentos = 0

for e_lista in lista:
    lista_preguntas.append(e_lista["pregunta"])
    lista_temas.append(e_lista["tema"])
    lista_respuesta_a.append(e_lista["a"])
    lista_respuesta_b.append(e_lista["b"])
    lista_respuesta_c.append(e_lista["c"])
    lista_respuesta_correcta.append(e_lista["correcta"])


pg.init()

imagen_logo = pg.image.load("carrera_de_mente\imagen_logo.jpg")
imagen_logo = pg.transform.scale(imagen_logo, (200, 170))
rect_logo = pg.Rect(200, 400, 150, 40)

fuente = pg.font.SysFont("Arial", 30)
fuente_dos = pg.font.SysFont("Arial", 18)

boton_pregunta = fuente.render(str("PREGUNTA"), True, COLOR_GRIS)
boton_reiniciar = fuente.render(str("REINICIAR"), True, COLOR_GRIS)

texto_pregunta = fuente_dos.render(str(pregunta), True, COLOR_GRIS)
texto_tema = fuente_dos.render(str(tema), True, COLOR_AMARILLO)
texto_respuesta_a = fuente_dos.render(str(respuesta_a), True, COLOR_AMARILLO)
texto_respuesta_b = fuente_dos.render(str(respuesta_b), True, COLOR_AMARILLO)
texto_respuesta_c = fuente_dos.render(str(respuesta_c), True, COLOR_AMARILLO)
texto_score = fuente_dos.render(str("SCORE"), True, COLOR_GRIS)
texto_puntuacion = fuente_dos.render(str("0"), True, COLOR_GRIS)

screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

pg.display.set_caption("Carrera de mente")



flag_run = True
while flag_run:
    lista_eventos = pg.event.get()
    for evento in lista_eventos:
        if evento.type == pg.QUIT:
            flag_run = False
        if evento.type == pg.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            print(posicion_click) 
            
            if posicion_click[0] > 300 and posicion_click[0] < 510 and posicion_click[1] > 30 and posicion_click[1] < 110: 
                pregunta = lista_preguntas[contador]
                tema = lista_temas[contador]
                respuesta_a = lista_respuesta_a[contador]
                respuesta_b = lista_respuesta_b[contador]
                respuesta_c = lista_respuesta_c[contador]
                respuesta_correcta = lista_respuesta_correcta[contador]
                texto_pregunta = fuente_dos.render(str(pregunta), True, COLOR_GRIS)
                texto_tema = fuente.render(str(tema), True, COLOR_AMARILLO)
                texto_respuesta_a = fuente_dos.render(str(respuesta_a), True, COLOR_AMARILLO)
                texto_respuesta_b = fuente_dos.render(str(respuesta_b), True, COLOR_AMARILLO)
                texto_respuesta_c = fuente_dos.render(str(respuesta_c), True, COLOR_AMARILLO)
                if contador >= len(lista_preguntas) - 1:
                    contador = 0
                else:
                    contador += 1
            
            if posicion_click[0] > 310 and posicion_click[0] < 510 and posicion_click[1] > 380 and posicion_click[1] < 470:
                contador = 0
                pregunta = lista_preguntas[contador]
                tema = lista_temas[contador]
                respuesta_a = lista_respuesta_a[contador]
                respuesta_b = lista_respuesta_b[contador]
                respuesta_c = lista_respuesta_c[contador]
                respuesta_correcta = lista_respuesta_correcta[contador]
                puntuacion = 0
                texto_pregunta = fuente_dos.render(str(pregunta), True, COLOR_GRIS)
                texto_tema = fuente.render(str(tema), True, COLOR_AMARILLO)
                texto_respuesta_a = fuente_dos.render(str(respuesta_a), True, COLOR_AMARILLO)
                texto_respuesta_b = fuente_dos.render(str(respuesta_b), True, COLOR_AMARILLO)
                texto_respuesta_c = fuente_dos.render(str(respuesta_c), True, COLOR_AMARILLO)
            
            if posicion_click[0] > 10 and posicion_click[0] < 130 and posicion_click[1] > 290 and posicion_click[1] < 315:
                respuesta_elegida = "a"
            elif posicion_click[0] > 205 and posicion_click[0] < 325 and posicion_click[1] > 290 and posicion_click[1] < 315:
                respuesta_elegida = "b"
            elif posicion_click[0] > 395 and posicion_click[0] < 515 and posicion_click[1] > 290 and posicion_click[1] < 315:
                respuesta_elegida = "c"
            else:
                respuesta_elegida = None
            
            if respuesta_elegida == respuesta_correcta:
                puntuacion += 10
            
            
            print(respuesta_correcta)
            print(contador)
            texto_puntuacion = fuente_dos.render(str(puntuacion), True, COLOR_GRIS)



    screen.fill(COLOR_CELESTE)
    
    pg.draw.rect(screen, COLOR_AMARILLO, (310, 30, 200, 80))
    pg.draw.rect(screen, COLOR_AMARILLO, (310, 380, 200, 80))
    
    pg.draw.rect(screen, COLOR_CELESTE, (10, 290, 120, 25))
    pg.draw.rect(screen, COLOR_CELESTE, (205, 290, 120, 25))
    pg.draw.rect(screen, COLOR_CELESTE, (395, 290, 120, 25))

    screen.blit(texto_score, (370, 150))
    screen.blit(texto_puntuacion, (370, 170))
    screen.blit(boton_pregunta, (335, 45,22,22))
    screen.blit(boton_reiniciar, (335, 395,22,22))
    screen.blit(imagen_logo, (10, 10))
    screen.blit(texto_pregunta, (10, 225))
    screen.blit(texto_tema, (15, 190))
    screen.blit(texto_respuesta_a, (10, 290))
    screen.blit(texto_respuesta_b, (210, 290))
    screen.blit(texto_respuesta_c, (400, 290))
    
    pg.display.flip()


pg.quit()