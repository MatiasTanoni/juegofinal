import pygame as py

class Nivel:
    def __init__(self, pantalla, personaje_principal, lista_plataformas, imagen_fondo) :
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo

    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == py.KEYDOWN:
                if evento.key == py.K_TAB:
                    #cambiar_modo()
                    pass
    

    def leer_inputs(self):
        teclas = py.key.get_pressed()

        if teclas[py.K_RIGHT]:
            self.jugador.que_hace = "Derecha"
        elif teclas [py.K_LEFT]:
            self.jugador.que_hace = "Izquierda"
        else:
            self.jugador.que_hace = "Quieto"