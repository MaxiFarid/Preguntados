lista=\
[
    {'pregunta': '¿Cuál es la moneda de México?', 'a': 'Peso', 'b': 'Dolar', 'c':'Euro' ,'correcta': 'a'}, 
    {'pregunta': '¿De qué colores es la bandera de Japón?', 'a': 'Azul y Amarilla','b': 'Blanca y roja', 'c':'Celeste y Blanca' ,'correcta': 'b'}, 
    {'pregunta': '¿Cuántos elementos forman la Tabla Periódica?', 'a': '118', 'b': '123', 'c':'125' ,'correcta': 'a'},
    {'pregunta': '¿Quién pintó la Mona Lisa?', 'a': 'Dali', 'b': 'Miguel Angel', 'c':'Leonardo da Vinci' ,'correcta': 'c'},
    {'pregunta': '¿Qué elemento de la tabla periódica tiene como símbolo He?', 'a': 'Hielo', 'b': 'Helio', 'c':'Litio' ,'correcta': 'b'},
    {'pregunta': '¿Qué planeta es el que se encuentra más cerca del Sol?', 'a': 'Mercurio', 'b': 'Marte', 'c':'Jupiter' ,'correcta': 'a'},
    {'pregunta': '¿A cuántos kilómetros equivale una milla?', 'a': '3.6 km.', 'b': '2.6 km.', 'c':'1.6 km.' ,'correcta': 'c'},
    {'pregunta': '¿De dónde es originario el mojito?', 'a': 'Cuba', 'b': 'Puerto Rico', 'c':'El Salvador' ,'correcta': 'a'},
    {'pregunta': '¿Cuántos lados tiene un heptadecágono?', 'a': 'Dieciseis', 'b': 'Diecisete', 'c':'Quince' ,'correcta': 'b'},
    {'pregunta': '¿De dónde sale el aceite de oliva?', 'a': 'aceitunas', 'b': 'girasol', 'c':'maiz' ,'correcta': 'a'},
    {'pregunta': '¿Dónde nació la pizza?', 'a': 'Roma', 'b': 'Venecia', 'c':'Napoles' ,'correcta': 'c'},
    {'pregunta': '¿Cuál es la capital de Kenia?', 'a': 'Luanda', 'b': 'Nairobi', 'c':'El Cairo' ,'correcta': 'b'},
    {'pregunta': '¿Cuántos colores tiene el cubo Rubik?', 'a': '6', 'b': '9', 'c':'4' ,'correcta': 'a'},
    {'pregunta': '¿A qué país pertenece la Isla de Pascua?', 'a': 'Argentina', 'b': 'Chile', 'c':'Brasil' ,'correcta': 'b'},
    {'pregunta': '¿Cuál es el país más grande del mundo?', 'a': 'China', 'b': 'Canada', 'c':'Rusia' ,'correcta': 'c'},
    {'pregunta': '¿Cuál es el lugar más frío de la tierra?', 'a': 'Rusia', 'b': 'Antartida', 'c':'Groenlandia' ,'correcta': 'b'},
    {'pregunta': '¿Cuál es el río más largo del planeta?', 'a': 'Amazonas', 'b': 'Nilo', 'c':'Misisipi' ,'correcta': 'a'}
]     

    # if posicion == len(lista):
    #     texto_score_final = fuente.render(f"SCORE FINAL: {score}", True, COLOR_GRIS)
    #     pantalla.blit(texto_score_final, (300, 155))

    #     pygame.draw.rect(pantalla, COLOR_AMARILLO, (300, 20, 200, 100))
    #     pantalla.blit(imagen, posicion_imagen)

    #     pantalla.blit(texto_pregunta, (30, 285))
    #     pantalla.blit(texto_rectangulo_pregunta, (350, 50))

    #     pygame.draw.rect(pantalla, color_rectangulo_opcion_a, (35, 390, 220, 60))
    #     pantalla.blit(texto_opcion_a, (45, 400))

    #     pygame.draw.rect(pantalla, color_rectangulo_opcion_b, (290, 390, 220, 60))
    #     pantalla.blit(texto_opcion_b, (300, 400))

    #     pygame.draw.rect(pantalla, color_rectangulo_opcion_c, (545, 390, 220, 60))
    #     pantalla.blit(texto_opcion_c, (555, 400))

    #     pygame.draw.rect(pantalla, COLOR_AMARILLO, (300, 480, 200, 100))
    #     pantalla.blit(texto_reiniciar, (350, 510))

    #     pantalla.blit(texto_score, (300, 155))

    #     pygame.display.flip()

    #     if mostrar_score_final == True:
    #         pantalla.blit(texto_score, (300, 155))