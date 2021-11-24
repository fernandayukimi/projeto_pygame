''''#import pygame
#from pygame.locals import * 
#from sys import exit

#pygame.init()

#largura = 640
#altura = 480 

#tela = pygame.display.set_mode((largura, altura)

# JOGO DO DINOSSAURO VERSÃO ROBERTO CARLOS EDICÃO NATAL:

import pygame 

pygame.init()

window = pygame.display.set_mode((680, 480))
pygame.display.set_capition('RC!')

game = True 

'''

import pygame
from pygame.locals import *
from sys import exit
pygame.init()

largura = 600
altura = 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('jogo')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

                