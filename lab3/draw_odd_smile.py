import pygame
from pygame.draw import *

pygame.init()

FPS = 30
YELLOW = (249, 215, 28)
RED = (138, 3, 3)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((400, 400))

rect(screen, (240, 240, 240), (0, 0, 400, 400))
circle(screen, YELLOW, (200, 200), 125)
circle(screen, RED, (255, 179), 20)
circle(screen, RED, (146, 179), 25)
circle(screen, BLACK, (255, 179), 9)
circle(screen, BLACK, (146, 179), 10)

polygon(screen, BLACK, [[175, 171], [183, 159],
						[82, 86], [75, 96]])
polygon(screen, BLACK, [[223, 173], [217, 164],
						[319, 110], [325, 119]])
rect(screen, BLACK, (155, 270, 100, 23))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

pygame.quit()
