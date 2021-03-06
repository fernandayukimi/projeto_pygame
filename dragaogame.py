#importações
import pygame
import random
from pygame.locals import *


#surgimento aleatorio das maçãs e colisão com a maçã
def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)
def collision(c1, c2):
    return (c1 [0]== c2[0] and (c1[1] == c2[1]))



UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#skin do personagem: que no caso é um dragão
pygame.init()
altura = 500
largura = 500
screen = pygame.display.set_mode((altura, largura))
pygame.display.set_caption('dragao')


dragao = [(200, 200), (210, 200), (220, 200)]
dragao_skin = pygame.Surface((10, 10))
dragao_skin.fill((34,139,34))

#maçã
apple_pos = on_grid_random()
apple = pygame.Surface ((10,10))
apple.fill((255,0,0))


my_direction = LEFT


Clock = pygame.time.Clock()


font = pygame .font.Font('freesansbold.ttf', 18)
score = 0

game_over = False
while not game_over:
    Clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT 
    if collision (dragao[0], apple_pos):
        apple_pos = on_grid_random()
        dragao.append((0,0))
        score = score + 1
    if dragao[0][0] == largura or dragao[0][1] == largura or dragao [0][0]< 0 or dragao [0][1] < 0:
        game_over = True
        break

    for i in range(1, len(dragao) -1):
        if dragao[0][0] == dragao[i][0] and dragao[0][1]==dragao[i][1]:
            game_over = True
            break
    if game_over:
        break


    for i in range (len(dragao) -1, 0, -1):
        dragao[i] = (dragao[i - 1][0], dragao[i-1][1]) 

    if my_direction == UP:
        dragao[0] = (dragao[0][0], dragao[0][1]-10)
    if my_direction == DOWN:
        dragao[0] = (dragao[0][0], dragao[0][1]+10)  
    if my_direction == RIGHT:
        dragao[0] = (dragao[0][0]+10, dragao[0][1])  
    if my_direction == LEFT:
        dragao[0] = (dragao[0][0]-10, dragao[0][1])    

    screen.fill((255,255,255))
    screen.blit(apple, apple_pos)

    score_font = font.render('Score: %s' % (score), True, (255,0,0))
    score_rect = score_font.get_rect()
    score_rect.topleft = (altura - 120,10)
    screen.blit(score_font,score_rect)

    for pos in dragao:
        screen.blit(dragao_skin,pos)
    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 65)
    game_over_screen = game_over_font.render('Game Over', True, (255,0,0))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (altura / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()