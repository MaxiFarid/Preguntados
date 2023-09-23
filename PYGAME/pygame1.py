# Desafío Preguntados
# Preguntados es una franquicia de entretenimiento de plataformas y una de las marcas más
# exitosas de la división de Gaming de Etermax.
# Preguntados es principalmente un juego de preguntas y respuestas de Cultura General tipo
# trivia. Digamos que este es el apartado en el que cabrían cuestiones de todo tipo. Si controlas
# datos históricos, orígenes de comidas, literatura y curiosidades de todo tipo, lograrás una buena
# puntuación.

# Recientemente Etermax ha decidido desarrollar el juego en Python, y para acceder a las
# entrevistas es necesario completar el siguiente desafío.

# La empresa compartió con todos los participantes cierta información confidencial de un grupo
# de preguntas y respuestas. Y semana a semana enviará una lista con los nuevos requerimientos.
# Quien supere todas las etapas accederá a una entrevista con el director para de la compañía.
# Set de datos 

# La información a ser analizada se encuentra en el archivo datos.py, por tratarse de una lista,
# bastará con incluir dicho archivo en el proyecto de la siguiente manera:

# from datos import lista

# Desafío:
# A. Analizar detenidamente el set de datos.
# B. Recorrer la lista guardando en sub-listas: la pregunta, cada opción y la respuesta
# correcta.
# C. Crear 2 botones (rectángulos) uno con la etiqueta “Pregunta”, otro con la etiqueta
# “Reiniciar”
# D. Imprimir el Score: 999 donde se va a ir acumulando el puntaje de las respuestas
# correctas. Cada respuesta correcta suma 10 puntos.
# E. Al hacer clic en el botón (rectángulo) “Pregunta” debe mostrar las preguntas
# comenzando por la primera y las tres opciones, cada clic en este botón pasa a la
# siguiente pregunta.
# F. Al hacer clic en una de las tres palabras que representa una de las tres opciones, si es
# correcta, debe sumar el score y dejar de mostrar las opciones.
# G. Solo tiene 2 opciones para acertar la respuesta correcta y sumar puntos, si agotó ambas
# opciones, deja de mostrar las opciones y no suma score
# H. Al hacer clic en el botón (rectángulo) “Reiniciar” debe mostrar las preguntas
# comenzando por la primera y las tres opciones, cada clic pasa a la siguiente

import pygame
from datos_pygame import lista
from constantes_pygame import *

pregunta = ""
opcion_a = ""
opcion_b = ""
opcion_c = ""
reiniciar = ""
posicion = 0
score = 0
opcion_seleccionada = ""
contador_errores = 0

posicion_imagen = [10,10]
lista_preguntas = []
lista_respuesta_a = []
lista_respuesta_b = []
lista_respuesta_c = []

color_rectangulo_opcion_a = COLOR_AMARILLO
color_rectangulo_opcion_b = COLOR_AMARILLO
color_rectangulo_opcion_c = COLOR_AMARILLO

bandera_mostrar_pregunta = None
bandera_mostrar_opciones = None
mostrar_score_final = None

for e_lista in lista:
    lista_preguntas.append(e_lista["pregunta"])
    lista_respuesta_a.append(e_lista["a"])
    lista_respuesta_b.append(e_lista["b"])
    lista_respuesta_c.append(e_lista["c"])

#Inicializar Pygame
pygame.init()

#Configuracion de pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA)) #Tamaño de la pantalla
pygame.display.set_caption("Preguntados") #Titulo

#Cargar Una Imagen
imagen = pygame.image.load("PYGAME/imagen_preguntados.png")
imagen = pygame.transform.scale(imagen,(250,250))

# Definir una fuente y un objeto de texto
fuente = pygame.font.SysFont("Arial", 30)  # Puedes ajustar el tamaño y el tipo de fuente según tus preferencias
texto_pregunta = fuente.render(str(pregunta), True, COLOR_GRIS)

texto_rectangulo_pregunta = fuente.render("Pregunta", True, COLOR_NEGRO)
texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_NEGRO)
texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_NEGRO)
texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_NEGRO)
texto_score = fuente.render(str(f"SCORE: {score}"), True, COLOR_GRIS)
texto_reiniciar = fuente.render(str(f"Reiniciar"), True, COLOR_NEGRO)

flag_correr = True
while flag_correr:

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
        
        #Muestro las coordenadas X, Y
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)

            # PREGUNTA
            if (posicion_click[0] > 300 and posicion_click[0] < 500) and (posicion_click[1] > 20 and posicion_click[1] < 120):
                color_rectangulo_opcion_a = COLOR_AMARILLO
                color_rectangulo_opcion_b = COLOR_AMARILLO
                color_rectangulo_opcion_c = COLOR_AMARILLO

                if posicion > 0:
                    posicion += 1

                bandera_mostrar_opciones = True
                bandera_mostrar_pregunta = True

            # REINICIAR
            if (posicion_click[0] > 300 and posicion_click[0] < 500) and (posicion_click[1] > 480 and posicion_click[1] < 580):
                color_rectangulo_opcion_a = COLOR_AMARILLO
                color_rectangulo_opcion_b = COLOR_AMARILLO
                color_rectangulo_opcion_c = COLOR_AMARILLO
                contador_errores = 0
                posicion = 0
                score = 0

            # OPCIONES
            if (posicion_click[0] > 35 and posicion_click[0] < 255) and (posicion_click[1] > 390 and posicion_click[1] < 450):
                if 'a' == lista[posicion]["correcta"]:
                    color_rectangulo_opcion_a = COLOR_AMARILLO
                    color_rectangulo_opcion_b = COLOR_AMARILLO
                    color_rectangulo_opcion_c = COLOR_AMARILLO    
                    posicion += 1

                    if contador_errores < 2:  # Solo sumamos puntos si el contador de errores es menor a 2
                        score += 10
                    contador_errores = 0
                else:
                    color_rectangulo_opcion_a = COLOR_ROJO
                    contador_errores += 1

            elif (posicion_click[0] > 290 and posicion_click[0] < 510) and (posicion_click[1] > 390 and posicion_click[1] < 450):
                if 'b' == lista[posicion]["correcta"]:
                    color_rectangulo_opcion_a = COLOR_AMARILLO
                    color_rectangulo_opcion_b = COLOR_AMARILLO
                    color_rectangulo_opcion_c = COLOR_AMARILLO    
                    posicion += 1
    
                    if contador_errores < 2:  # Solo sumamos puntos si el contador de errores es menor a 2
                        score += 10
                    contador_errores = 0
                else:
                    color_rectangulo_opcion_b = COLOR_ROJO
                    contador_errores += 1

            elif (posicion_click[0] > 545 and posicion_click[0] < 765) and (posicion_click[1] > 390 and posicion_click[1] < 450):
                if 'c' == lista[posicion]["correcta"]:
                    color_rectangulo_opcion_a = COLOR_AMARILLO
                    color_rectangulo_opcion_b = COLOR_AMARILLO
                    color_rectangulo_opcion_c = COLOR_AMARILLO
                    posicion += 1

                    if contador_errores < 2:  # Solo sumamos puntos si el contador de errores es menor a 2
                        score += 10
                    contador_errores = 0
                else:
                    color_rectangulo_opcion_c = COLOR_ROJO
                    contador_errores += 1

    pantalla.fill(COLOR_AZUL)

    pygame.draw.rect(pantalla, COLOR_AMARILLO, (300, 20, 200, 100),)
    pantalla.blit(imagen,(posicion_imagen),) #Fundimos la imagen en la superficie pantalla
    pantalla.blit(texto_pregunta,(30,285))
    pantalla.blit(texto_rectangulo_pregunta,(350,50))

    pygame.draw.rect(pantalla, color_rectangulo_opcion_a, (35,390,220,60)) # Rectangulo Respuesta A
    pantalla.blit(texto_opcion_a,(45,400))

    pygame.draw.rect(pantalla, color_rectangulo_opcion_b, (290,390,220,60)) # Rectangulo Respuesta B
    pantalla.blit(texto_opcion_b,(300,400))

    pygame.draw.rect(pantalla, color_rectangulo_opcion_c, (545,390,220,60)) # Rectangulo Respuesta C 
    pantalla.blit(texto_opcion_c,(555,400))

    pygame.draw.rect(pantalla, COLOR_AMARILLO, (300,480,200,100)) # Rectangulo Reiniciar
    pantalla.blit(texto_reiniciar,(350,510))

    pantalla.blit(texto_score,(300,155)) # Texto score

    pygame.display.flip()

    if (bandera_mostrar_opciones == True) and (bandera_mostrar_pregunta == True):
        pregunta_actual = lista_preguntas[posicion]
        opciones_actual_a = lista_respuesta_a[posicion]
        opciones_actual_b = lista_respuesta_b[posicion]
        opciones_actual_c = lista_respuesta_c[posicion]

        texto_pregunta = fuente.render(str(pregunta_actual), True, COLOR_GRIS)
        texto_opcion_a = fuente.render(str(opciones_actual_a), True, COLOR_NEGRO)
        texto_opcion_b = fuente.render(str(opciones_actual_b), True, COLOR_NEGRO)
        texto_opcion_c = fuente.render(str(opciones_actual_c), True, COLOR_NEGRO)

        texto_score = fuente.render(str(f"SCORE: {score}"), True, COLOR_GRIS)

    if mostrar_score_final == True:
        pantalla.blit(texto_score, (300, 155))

pygame.quit() 