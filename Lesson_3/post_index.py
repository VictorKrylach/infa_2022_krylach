import turtle as tr

import numpy as np

stamp_0 = [(50, 90), (100, 90), (50, 90), (100, 90)]

stamp_1 = [(5000**0.5, 135), (100, 180)]

stamp_4 = [(50, 270), (50, 90), (50, 180), (100, 0)]

stamp_7 = [(50, 135), (5000**0.5, 315), (50, 0)]



def character_0():
	for step, angle in stamp_0:
		tr.forward(step)
		tr.right(angle)
	tr.penup()
	tr.forward(100)
	tr.pendown()

def character_1():
	tr.penup()
	tr.right(90)
	tr.forward(50)
	tr.left(135)
	tr.pendown()
	for step, angle in stamp_1:
		tr.forward(step)
		tr.right(angle)
	tr.penup()
	tr.forward(100)
	tr.right(90)
	tr.forward(50)
	tr.pendown()

def character_4():
	tr.right(90)
	for step, angle in stamp_4:
		tr.forward(step)
		tr.right(angle)
	tr.penup()
	tr.right(90)
	tr.forward(50)
	tr.pendown()

def character_7():
	for step, angle in stamp_7:
		tr.forward(step)
		tr.right(angle)
	tr.penup()
	tr.left(90)
	tr.forward(100)
	tr.right(270)
	tr.forward(100)
	tr.right(90)
	tr.pendown()


character_1()
character_4()
character_1()
character_7()
character_0()
character_0()

input()