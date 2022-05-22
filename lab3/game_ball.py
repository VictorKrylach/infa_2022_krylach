import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

x = y = r = None
score = 0

def new_ball():
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def click(event):
    print(x, y, r)
    #if event.type == pygame.MOUSEBUTTONDOWN:
       #print(event.pos[0], event.pos[1])
        #if (((event.pos[0])**2 + (event.pos[1])**2)**1/2) < r:
            #i = 100
            #print(i)
#(((event.pos[0])**2 + (event.pos[1])**2)**1/2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            click(event)
            if int(((x - event.pos[0])**2 + (y - event.pos[1])**2)**0.5) < r:
                score += 100
                print('Your score: ', score)
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()