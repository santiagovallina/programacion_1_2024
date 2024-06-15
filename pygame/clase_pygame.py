import pygame as pg

pg.init() #inicializo pg
screen = pg.display.set_mode([500, 500])
pg.display.set_caption("clase pygame") #cambiar nombre de la ventana
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((255, 255, 255)) #se pinta el fondo de la pantalla
    #se dibuja un circulo azul en el centro
    pg.draw.circle(screen,(0, 0, 255), (250, 250), 75)
    pg.display.flip()
pg.quit() #finalizo pg


