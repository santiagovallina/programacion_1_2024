import pygame as pg
from constantes import *

pg.init() #iniciamos el juego


#crear la pantalla
screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

#titulo de la ventana
pg.display.set_caption("Clase de pygame")

#imagen_messi
poscion_imagen = [250, 250]
imagen_messi = pg.image.load("pygame\messi.jpg")
imagen_messi = pg.transform.scale(imagen_messi, (100, 100))
#                left  top   ancho   alto
rect_messi = pg.Rect(30, 100, 101, 101)

# otra imagen
imagen_rana = pg.image.load("pygame\descarga.jpg")
imagen_rana = pg.transform.scale(imagen_rana, (50, 50))
# tomar el rect() de la img de la rana
rect_rana = pg.Rect(30, 100, 101, 101)
rect_rana.x = 301
rect_rana.y = 301

#texto
fuente = pg.font.SysFont("Arial", 30)
texto = fuente.render("messirve", True, COLOR_GRIS)

#defino la musica
# pg.mixer.init()
# sonido_fondo = pg.mixer.Sound("pygame\sonido_messi.mp3")
# volumen = 0.09
# sonido_fondo.set_volume(volumen)
# sonido_fondo.play()

# timer de 1 segundo
timer_segundos = pg.USEREVENT
pg.time.set_timer(timer_segundos, 1000) # 1000 es un segundo
segundos = "10"
fin_tiempo = False

#timer de 2 segundos
timer_2_segundos = pg.USEREVENT+1
pg.time.set_timer(timer_2_segundos, 2000) #2000 es 2 segundos


#caja de texto para ingreso del usuario
ingreso = ""
ingreso_rect = pg.Rect(200, 400, 150, 40)




running = True 
while running:
    lista_eventos = pg.event.get()
    for event in lista_eventos:
        #si el evento es salir, cierra la ventana
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            lista_posicion = list(event.pos)
            #modifico el left
            rect_messi[0] = lista_posicion[0]
            rect_messi[1] = lista_posicion[1]
        
        """if event.type == pg.MOUSEBUTTONDOWN:
            poscion_imagen_messi = list(event.pos)"""
        
        if event.type == pg.USEREVENT:
            if event.type == timer_segundos:
                if fin_tiempo == False:
                    segundos = int(segundos) - 1
                    if int(segundos) == 0:
                        fin_tiempo = True
                        segundos = "Tiempo"
        
        """if event.type == pg.USEREVENT+1:
            if event.type == timer_2_segundos:
                print("pasaron 2 segundos")
        
        if event.type == pg.KEYDOWN:
            if event.type == pg.K_BACKSPACE:
                ingreso = ingreso[0:1]
            else:
                ingreso += event.unicode
                print(ingreso)"""
        
        
        """if event.type == pg.MOUSEBUTTONDOWN:
            print(event.pos) #muestra la coordenada en la que se hizo click
            posicion_circulo = list(event.pos) #voy cambiando la poscion del circulo con el mouse"""
    
        """if event.type == pg.KEYDOWN: #evento de presionar una tecla
            #mover el circulo
            if event.key == pg.K_RIGHT:
                posicion_circulo[0] = posicion_circulo[0]+10
            if event.key == pg.K_LEFT:
                posicion_circulo[0] = posicion_circulo[0]-10
            if event.key == pg.K_UP:
                posicion_circulo[1] = posicion_circulo[1]-10
            if event.key == pg.K_DOWN:
                posicion_circulo[1] = posicion_circulo[1]+10"""
    
    #fuera del for
    lista_teclas = pg.key.get_pressed()
    if True in lista_teclas:
        if lista_teclas[pg.K_RIGHT]:
            posicion_circulo[0] = posicion_circulo[0] + 0.5
        elif lista_teclas[pg.K_LEFT]:
            posicion_circulo[0] = posicion_circulo[0] - 0.5
        elif lista_teclas[pg.K_UP]:
            posicion_circulo[1] = posicion_circulo[1] - 0.5
        elif lista_teclas[pg.K_DOWN]:
            posicion_circulo[1] = posicion_circulo[1] + 0.5
    
    
    # agregamos todo lo que hicimos
    screen.fill((COLOR_CELESTE)) #pintamos el fondo de la pantalla
    
    pg.draw.rect(screen, COLOR_ROJO, rect_rana)
    screen.blit(imagen_rana, (rect_rana.x+5, rect_rana.y+5))
    
    pg.draw.rect(screen, COLOR_ROJO, rect_messi)
    screen.blit(imagen_messi, rect_messi)
    
    """screen.blit(imagen_messi, (poscion_imagen)) #agrego la imagen_messi
    screen.blit(texto, (300, 400))""" # agrego el texto
    
    """segundos_texto = fuente.render(str(segundos), True, COLOR_ROJO)
    screen.blit(segundos_texto, (300, 300))"""
    
    
    
    flag_viva = True
    if rect_messi.colliderect(rect_rana):
        flag_viva = False
        
    
    # dibujamos un circulo
    #pg.draw.circle(screen, COLOR_BLANCO, posicion_circulo, 60)
    
    #dibujamos un rectangulo
    #los primeros dos numeros son las coordenadas, los otros dos largo y ancho
    #pg.draw.rect(screen, COLOR_BLANCO, (10, 30, 200, 100))


    #creo el rectangulo para el ingreso del usuario
    """pg.draw.rect(screen, COLOR_BLANCO, ingreso_rect, 3)
    texto_superficie = fuente.render(ingreso, True, COLOR_VERDE)
    # screen.blit(texto_superficie, ingreso_rect)
    screen.blit(texto_superficie, (ingreso_rect.x+5, ingreso_rect.y+1.5))"""
    
    
    # con el flip actualizamos la pantalla, es decir, muestra todo lo que agregamos
    pg.display.flip()
#sonido_fondo.stop() #stop al sonido
pg.quit() # finalizamos el juego