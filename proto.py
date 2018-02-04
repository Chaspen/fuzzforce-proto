import pygame
from pygame.locals import *
import sys

posX = 800
posY = 600

pygame.init()
protoDispInit = pygame.display.set_mode((posX, posY))
pygame.display.set_caption('FuzzForce Production Protoype')
clock = pygame.time.Clock()

#exit msg
def proto_quit():
    pygame.quit()
    sys.exit



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            proto_quit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                proto_quit()
            elif event.key == K_w:
                moveY = -1
            elif event.key == K_s:
                moveY = 1
            elif event.key == K_a:
                moveX = -1
            elif event.key == K_d:
                moveX = 1

    posX += moveX
    posY += moveY

    black = (0, 0, 0)
    white = (255, 255, 255)
    playerColorBlue = (0, 0, 255)
    enemyColorRed = (255, 0, 0)


    dispPlayer = pygame.image.load("square.png")
    dispPlayer = pygame.transform.scale(dispPlayer, (50,50))

    protoDispInit.fill(white)
    protoDispInit.blit(dispPlayer, (0,0))

    pygame.display.update()
    clock.tick(120)
pygame.quit()
quit()
