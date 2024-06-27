import pygame as pg
from constantes_utn import *
from datos_utn import lista

pregunta = ""
texto_pregunta_lines = ""
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
texto_respuesta_a = fuente_dos.render(str(respuesta_a), True, COLOR_AMARILLO)
texto_respuesta_b = fuente_dos.render(str(respuesta_b), True, COLOR_AMARILLO)
texto_respuesta_c = fuente_dos.render(str(respuesta_c), True, COLOR_AMARILLO)
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

def render_text(text, font, color, max_width):
    words = text.split(' ')
    lines = []
    current_line = words[0]
    
    for word in words[1:]:
        if font.size(current_line + ' ' + word)[0] <= max_width:
            current_line += ' ' + word
        else:
            lines.append(current_line)
            current_line = word
            
    lines.append(current_line)
    return [font.render(line, True, color) for line in lines]

flag_run = True
while flag_run:
    lista_eventos = pg.event.get()
    for evento in lista_eventos:
        if evento.type == pg.QUIT:
            flag_run = False
        if evento.type == pg.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            print(posicion_click)
            
            if 150 < posicion_click[0] < 310 and 520 < posicion_click[1] < 600:
                pregunta = lista_preguntas[contador]
                respuesta_a = lista_respuesta_a[contador]
                respuesta_b = lista_respuesta_b[contador]
                respuesta_c = lista_respuesta_c[contador]
                respuesta_correcta = lista_respuesta_correcta[contador]

                texto_pregunta_lines = render_text(pregunta, fuente_dos, NEGRO, 350)
                
                texto_respuesta_a = fuente_dos.render(str(respuesta_a), True, COLOR_AMARILLO)
                texto_respuesta_b = fuente_dos.render(str(respuesta_b), True, COLOR_AMARILLO)
                texto_respuesta_c = fuente_dos.render(str(respuesta_c), True, COLOR_AMARILLO)
                tiempo_iniciado = True
                segundos = 5

            if tiempo_iniciado:
                if 245 < posicion_click[0] < 320 and 170 < posicion_click[1] < 190:
                    respuesta_elegida = "a"
                elif 375 < posicion_click[0] < 455 and 170 < posicion_click[1] < 190:
                    respuesta_elegida = "b"
                elif 500 < posicion_click[0] < 570 and 170 < posicion_click[1] < 190:
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
                    contador += 1
                    pregunta = lista_preguntas[contador]
                    respuesta_a = lista_respuesta_a[contador]
                    respuesta_b = lista_respuesta_b[contador]
                    respuesta_c = lista_respuesta_c[contador]
                    respuesta_correcta = lista_respuesta_correcta[contador]
                    
                    texto_pregunta_lines = render_text(pregunta, fuente_dos, NEGRO, 350)
                    
                    texto_respuesta_a = fuente_dos.render(respuesta_a, True, COLOR_AMARILLO)
                    texto_respuesta_b = fuente_dos.render(respuesta_b, True, COLOR_AMARILLO)
                    texto_respuesta_c = fuente_dos.render(respuesta_c, True, COLOR_AMARILLO)
                    segundos = 5
                else:
                    fin_tiempo = True
        
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
                        
                        texto_pregunta_lines = render_text(pregunta, fuente_dos, NEGRO, 350)
                        
                        texto_respuesta_a = fuente_dos.render(respuesta_a, True, COLOR_AMARILLO)
                        texto_respuesta_b = fuente_dos.render(respuesta_b, True, COLOR_AMARILLO)
                        texto_respuesta_c = fuente_dos.render(respuesta_c, True, COLOR_AMARILLO)
                        segundos = 5
                    else:
                        fin_tiempo = True

    screen.fill(STEELBLUE)

    pg.draw.rect(screen, STEELBLUE3, (450, 520, 200, 80), border_radius=15)
    pg.draw.rect(screen, STEELBLUE3, (150, 520, 200, 80), border_radius=15)
    
    pg.draw.rect(screen, BLACK, (239, 9, 352, 202))
    pg.draw.rect(screen, GREEN, (240, 10, 350, 200))
    
    # Dibuja casillas aquí

    for i, line in enumerate(texto_pregunta_lines):
        screen.blit(line, (245, 30 + i * 30))
    
    screen.blit(texto_respuesta_a, (245, 170))
    screen.blit(texto_respuesta_b, (380, 170))
    screen.blit(texto_respuesta_c, (500, 170))
    
    screen.blit(texto_puntuacion, (740, 100))
    
    pg.display.flip()

pg.quit()

