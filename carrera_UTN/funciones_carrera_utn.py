#from carrera_utn import *
from constantes_utn import *
import pygame as pg
import json


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

def pedir_nombre(pantalla, fuente):
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
        pantalla.fill(STEELBLUE)
        texto = fuente.render("Ingrese su nombre: " + nombre, True, NEGRO)
        pantalla.blit(texto, (100, 200))
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


def mostrar_mejores_puntajes(pantalla, fuente):
    archivo_puntajes = "puntajes.json"
    try:
        with open(archivo_puntajes, "r") as archivo:
            puntajes = json.load(archivo)
    except FileNotFoundError:
        puntajes = []
    pantalla.fill(STEELBLUE)
    posicion_y = 50
    for indice, puntaje in enumerate(puntajes):
        texto = fuente.render(f"{indice + 1} {puntaje['nombre'].capitalize()} - {puntaje['puntaje']}", True, NEGRO)
        pantalla.blit(texto, (100, posicion_y))
        posicion_y += 50
    pg.display.flip()
    pg.time.wait(4000)

