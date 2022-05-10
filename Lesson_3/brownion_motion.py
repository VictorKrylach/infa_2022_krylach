import turtle as tr

from random import *

def motion():
	degree = randint(0, 360)
	step_1 = randint(15, 50)
	step_2 = randint(15, 50)
	tr.left(degree)
	tr.forward(step_1)
	tr.left(degree)
	tr.forward(step_2)

i = 0
while i < 50:
	motion()
	i += 1