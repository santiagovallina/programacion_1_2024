#### AYUDA PARA HACER EL CARRERA DE MENTE

import pygame as pg
# from data1 import lista_bizarrap
from constantes import *

ANCHO_VENTANA = 500 
ALTO_VENTANA = 500 

lista_bzrp = []
titulo = ""
lista_titulos = []
contador = 0

for e_lista in lista_bzrp:
    lista_titulos.append(e_lista["title"])


pg.init()
#cargamos una imagen 
imagen = pg.imagen.load("utn.jpg")
imagen = pg.transform.scale(imagen, (80, 80))

#crear una fuente
fuente = pg.font.SysFont("Arial", 30)
texto_titulo = fuente.render(str(titulo), True, COLOR_GRIS)

#crear la pantalla
screen = pg.display.set_mode(ANCHO_VENTANA, ALTO_VENTANA)
pg.display.set_caption("pg bzrp")

flag_correr = True
while flag_correr:
    lista_eventos = pg.event.get()
    for evento in lista_eventos:
        if evento.type == pg.QUIT:
            flag_correr = False
        
        if evento.type == pg.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            print(posicion_click) #busco la posicion para saber en que coordenadas esta la figura
            if posicion_click[0] > 300 and posicion_click[0] < 500 and posicion_click[1] > 20 and posicion_click[1] < 120: #son las coordenadas del rectangulo
                titulo = lista_titulos[contador]
                texto_titulo = fuente.render(str(titulo), True, COLOR_VERDE)
                if contador >= len(lista_titulos):
                    contador = 0
                else:
                    contador = contador + 1
    
    
    screen.fill(COLOR_AMARILLO)
    pg.draw.rect(screen, COLOR_BLANCO, (300, 20, 200, 100))
    screen.blit(texto_titulo, (150, 1700))
    screen.blit(imagen, 30, 100)
    pg.display.flip()
    
pg.quit()