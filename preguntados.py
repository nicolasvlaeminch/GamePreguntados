import pygame
from constantes import *
from datos import lista

pygame.init()
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Preguntados")
clock = pygame.time.Clock()
running = True
activar_pregunta = False
pasar_pregunta = False
reiniciar_pregunta = False
primera_entrada_pregunta = True
primera_entrada_reiniciar = True
primera_entrada_reiniciar_activada = False
mostrar_preguntas = True
score = 999
puntos_score = 10
vidas = 2
sub_listas = []

for pregunta in lista:
    sub_lista = [pregunta['pregunta'], pregunta['a'], pregunta['b'], pregunta['c'], pregunta['correcta']]
    sub_listas.append(sub_lista)

imagen = pygame.image.load("Preguntados/icono.png")
imagen = pygame.transform.scale(imagen,(225, 225))
fuente = pygame.font.SysFont("Arial", 24)
texto_pregunta = fuente.render("PREGUNTA", True, COLOR_AZUL)
texto_reiniciar = fuente.render("REINICIAR", True, COLOR_AZUL)
i = 0

while running:
    texto_score = fuente.render(f"SCORE: {score}", True, COLOR_AMARILLO)
    texto_pregunta_preguntados = fuente.render(str(sub_listas[i][0]), True, COLOR_AMARILLO)
    texto_respuesta_a = fuente.render(str(sub_listas[i][1]), True, COLOR_AMARILLO)
    texto_respuesta_b = fuente.render(str(sub_listas[i][2]), True, COLOR_AMARILLO)
    texto_respuesta_c = fuente.render(str(sub_listas[i][3]), True, COLOR_AMARILLO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            position_click = list(evento.pos)

            if (position_click[0] > 320 and position_click[0] < 480) and (position_click[1] > 15 and position_click[1] < 95):  
                if activar_pregunta == True:
                    pasar_pregunta = True
                activar_pregunta = True

            elif (position_click[0] > 320 and position_click[0] < 480) and (position_click[1] > 505 and position_click[1] < 585):  
                reiniciar_pregunta = True

            elif (position_click[0] > 10 and position_click[0] < 200) and (position_click[1] > 380 and position_click[1] < 420):
                if sub_listas[i][4] == "a":
                    score = score + 10
                    mostrar_preguntas = False
                else:
                    vidas = vidas - 1

            elif (position_click[0] > 250 and position_click[0] < 450) and (position_click[1] > 380 and position_click[1] < 420):
                if sub_listas[i][4] == "b":
                    score = score + 10
                    mostrar_preguntas = False
                else:
                    vidas = vidas - 1
                
            elif (position_click[0] > 500 and position_click[0] < 750) and (position_click[1] > 380 and position_click[1] < 420):
                if sub_listas[i][4] == "c":
                    score = score + 10
                    mostrar_preguntas = False
                else:
                    vidas = vidas - 1

    screen.fill(COLOR_AZUL)
    screen.blit(imagen, (10, 10))
    pygame.draw.rect(screen, COLOR_AMARILLO,(320, 15, 160, 80))
    pygame.draw.rect(screen, COLOR_AMARILLO,(320, 505, 160, 80))
    screen.blit(texto_pregunta, (335, 40, 160, 80))
    screen.blit(texto_reiniciar, (335, 530, 160, 80))
    screen.blit(texto_score, (335, 200, 160, 80))

    if activar_pregunta:
        if pasar_pregunta:
            if vidas == 1:
                vidas = 2
            mostrar_preguntas = True
            i = i + 1
            pasar_pregunta = False
            if primera_entrada_reiniciar_activada:
                primera_entrada_reiniciar_activada = False
            if i == len(lista):
                i = 0
        if primera_entrada_pregunta:
            i = 0
            score = 0
            primera_entrada_pregunta = False
        if reiniciar_pregunta:
            mostrar_preguntas = True
            if vidas < 2:
                vidas = 2
            i = i + 1
            score = 0
            reiniciar_pregunta = False
            if primera_entrada_reiniciar:
                i = 0
                primera_entrada_reiniciar = False
            if primera_entrada_reiniciar_activada == False:
                i = 0
                primera_entrada_reiniciar_activada = True
            if i == len(lista):
                i = 0

        screen.blit(texto_pregunta_preguntados, (20, 300, 160, 80))
        if mostrar_preguntas and (vidas > 0):
            screen.blit(texto_respuesta_a, (18, 390, 160, 80))
            screen.blit(texto_respuesta_b, (260, 390, 160, 80))
            screen.blit(texto_respuesta_c, (520, 390, 160, 80))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
