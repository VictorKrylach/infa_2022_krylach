
import turtle as tr

import numpy as np


def throw_material(speed_0, angle):
	x = 0
	y = 10
	#speed_y = speed_0 * np.sin(angle)
	dt = 0
	g = 3
	while y >= 0:
		dt += 1
		speed_x = speed_0 * (np.cos(angle))
		print(speed_x)
		x += speed_x * dt
		#y += speed_y * dt - ((g * dt**2) / 2)
		tr.goto(x,y)
	

throw_material(10, 60)

input()
	
#speed_0 *= 0.2
	#y = 0
	#dt = 0
	#while y >= 0:
		#dt += -0.1
	#	x += speed_x * dt
		#y += speed_y * dt - ((g * dt**2) / 2)
	#	tr.goto(x,y)