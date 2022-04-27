import pygame
from pygame.draw import *

pygame.init()

FPS = 30
YELLOW = (249, 215, 28)
RED = (138, 3, 3)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((400, 400))

circle(screen, YELLOW, (200, 200), 125)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

pygame.quit()
