import pygame
from pygame.draw import *

pygame.init()

FPS = 30
GROUND_COLOR = (40, 32, 26)
SKY_COLOR = (3, 13, 14)
MOON_COLOR = (208, 228, 227)
CLOUD_COLOR_ONE = (100, 100, 100)
CLOUD_COLOR_TWO = (42, 42, 42)

UFO_COLOR_ONE = (129, 129, 129)
UFO_COLOR_TWO = (196, 196, 196)
UFO_LIGHTS_COLOR = (233, 233, 233)

BLACK = (0, 0, 0)
RED = (232, 59, 59)
GREEN = (35, 121, 20)
ALIEN_COLOR = (158, 184, 154)

screen = pygame.display.set_mode((794, 1123))
#draw sky back-ground
rect(screen, SKY_COLOR, (0, 0, 794, 584))
#draw a ground
rect(screen, GROUND_COLOR, (0, 583, 794, 539))
#draw moon
circle(screen, MOON_COLOR, (541, 250), 100)
#draw clouds
ellipse(screen, CLOUD_COLOR_ONE, (560, 0, 800, 110))
ellipse(screen, CLOUD_COLOR_ONE, (-450, 30, 1010, 220))
ellipse(screen, CLOUD_COLOR_ONE, (410, 180, 597, 105))
ellipse(screen, CLOUD_COLOR_TWO, (135, 100, 854, 130))
ellipse(screen, CLOUD_COLOR_ONE, (-260, 270, 810, 115))
ellipse(screen, CLOUD_COLOR_TWO, (-535, 240, 910, 115))
ellipse(screen, CLOUD_COLOR_ONE, (290, 310, 750, 115))
ellipse(screen, CLOUD_COLOR_TWO, (200, 390, 710, 100))
#draw UFO
#surface_light = polygon(screen, UFO_LIGHTS_COLOR, ((215, 420), (10, 760), (360, 763)), pygame.SRCALPHA)
polygon(screen, (233, 233, 233, 0.1), ((215, 420), (10, 760), (360, 763)))

ellipse(screen, UFO_COLOR_ONE, (5, 400, 400, 120))
ellipse(screen, UFO_COLOR_TWO, (50, 390, 310, 90))
#draw alien
circle(screen, ALIEN_COLOR, (555, 900), 10)


circle(screen, ALIEN_COLOR, (645, 920), 10)



#circle(screen, RED, (255, 179), 20)
#circle(screen, RED, (146, 179), 25)
#circle(screen, BLACK, (255, 179), 9)
#circle(screen, BLACK, (146, 179), 10)

#polygon(screen, BLACK, [[175, 171], [183, 159],
						#[82, 86], [75, 96]])
#polygon(screen, BLACK, [[223, 173], [217, 164],
						#[319, 110], [325, 119]])
#rect(screen, BLACK, (155, 270, 100, 23))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

pygame.quit()