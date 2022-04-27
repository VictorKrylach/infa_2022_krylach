import pygame
from pygame.drow import *

pygame.init()

screen = pygame.display.set_mode((300, 200))

pygame.display.update()

clock = pygame.time.Clock()

while true:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
