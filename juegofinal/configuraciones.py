import pygame as py

def reescalar_imagenes(diccionario_animaciones, ancho, alto):
    for clave in diccionario_animaciones:
        lista = diccionario_animaciones[clave]
        for i in range(len(lista)):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = py.transform.scale(img, (ancho,alto))

def rotar_imagen(imagenes:list):
    lista_imagenes = []
    for i in range(len(imagenes)):
        imagen_rotada = py.transform.flip(imagenes[i],True,False)
        lista_imagenes.append(imagen_rotada)
    
    return lista_imagenes


personaje_quieto = [py.image.load(r"imagenes\quieto.png")]

personaje_derecha = [py.image.load(r"imagenes\caminaderecha.png"),
                    py.image.load(r"imagenes\caminaderecha2.png"),
                    py.image.load(r"imagenes\caminaderecha3.png"),
                    py.image.load(r"imagenes\caminaderecho4.png"),
                    py.image.load(r"imagenes\caminaderecha5.png")]

personaje_izquierda = rotar_imagen(personaje_derecha)
