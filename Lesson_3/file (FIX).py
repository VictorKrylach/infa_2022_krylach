import turtle as tr

import numpy as np


inp = open('post_index.txt', 'r')

f = ()
s = inp.readline()
s = inp.rstrip()
stamp_0 = f + ((s),)
stamp_1 = f + ((s),)
stamp_4 = f + ((s),)
stamp_7 = f + ((s),)

print (stamp_0)
print (stamp_1)

input()
inp.close()


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