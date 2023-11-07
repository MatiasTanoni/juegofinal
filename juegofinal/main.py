import pygame as py
from pygame.locals import *
from configuraciones import *

W = 1200 #ANCHO
H = 600   #ALTO
FPS = 18

py.init()
RELOJ = py.time.Clock()
PANTALLA = py.display.set_mode((W,H))
py.display.set_caption("Juego Matias Tanoni")

#BackGround
fondo = py.image.load(r"imagenes\background.png").convert()
fondo = py.transform.scale(fondo,(W,H))

contador_pasos = 0

#Acciones
acciones = {}
acciones["Quieto"] = personaje_quieto
acciones["Derecha"] = personaje_derecha
acciones["Izquierda"] = personaje_izquierda

reescalar_imagenes(acciones,110,130)

personaje={
    "contador_pasos":0
}

def mover_animacion(rectangulo, velocidad, pantalla):
    x_nueva = rectangulo.x + velocidad
    if x_nueva < pantalla.get_width() - rectangulo_personaje.width and x_nueva > 0: #PARA QUE NO SE VAYA DE LA PANTALLA
        rectangulo.x += velocidad

def animar_personaje(pantalla, lista_imagenes,rectangulo_personaje,contador_pasos):
    largo_lista = len(lista_imagenes)

    if personaje["contador_pasos"] >= largo_lista: #REINICIO LA EL CONTADOR CON EL MAXIMO DE IMAGENES QUE TENGO
        personaje["contador_pasos"] = 0            #EN LA LISTA PARA QUE LA SECUENCIA DE IMAGENES SE REINICIE

    pantalla.blit(lista_imagenes[personaje["contador_pasos"]], rectangulo_personaje)
    personaje["contador_pasos"] += 1

def actualizar_pantalla(pantalla,fondo,que_hace:str,acciones,rectangulo_personaje,personaje):
    pantalla.blit(fondo,(0,0))
    match que_hace:
        case "Quieto":
            animar_personaje(pantalla, acciones["Quieto"], rectangulo_personaje,personaje)
        case "Derecha":
            animar_personaje(pantalla, acciones["Derecha"], rectangulo_personaje,personaje)
            mover_animacion(rectangulo_personaje,15,pantalla)
        case "Izquierda":
            animar_personaje(pantalla, acciones["Izquierda"], rectangulo_personaje,personaje)
            mover_animacion(rectangulo_personaje,15,pantalla)



#Personaje
x_inicial = 200
y_inicial = 400
rectangulo_personaje = personaje_quieto[0].get_rect()
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial

que_hace = "Quieto"


flag = True
while flag:
    RELOJ.tick(FPS)
    PANTALLA.blit(fondo,(0,0))
    for event in py.event.get():
        if event.type == QUIT:
            flag = False
    teclas = py.key.get_pressed()

    if teclas[py.K_RIGHT]:
        que_hace = "Derecha"
    elif teclas [py.K_LEFT]:
        que_hace = "Izquierda"
    else:
        que_hace = "Quieto"

    actualizar_pantalla(PANTALLA, fondo, que_hace, acciones, rectangulo_personaje,personaje["contador_pasos"])

    py.display.update()

py.quit()