from configuraciones import *
import pygame as py


class Personaje:
    def __init__(self, animaciones, tamaño, pos_x, pos_y, velocidad) -> None:

        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, *tamaño) 
        self.rectangulo_principal = self.animaciones["Derecha"][0].get_rect() 
        self.rectangulo_principal.x = pos_x
        self.rectangulo_principal.y = pos_y
        self.velocidad = velocidad

        self.que_hace = "Quieto"
        self.animacion_actual = self.animaciones["Quieto"]
        self.contador_pasos = 0

        self.desplazamiento_y = 0
        self.potencia_salto = -15
        self.limite_velocidad_salto = 15
        self.gravedad = 1
        #self.esta_saltando = False