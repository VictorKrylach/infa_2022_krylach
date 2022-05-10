import turtle as tr
import numpy as np

tr.shape('turtle')

def move(x, y):
	tr.penup()
	tr.goto(x, y)
	tr.pendown()

#drow a face (main yelow circle)
def circle_1():
	tr.fillcolor('yellow')
	tr.begin_fill()
	for i in range(90):
		tr.forward(10)
		tr.right(4)
	tr.end_fill()

#drow eyes
def circle_2():
	tr.fillcolor('blue')
	tr.begin_fill()
	for i in range(90):
		tr.forward(1.7)
		tr.right(4)
	tr.end_fill()

#drow nose
def nose(mass):
	tr.width(mass)
	tr.right(90)
	tr.forward(50)

#drow mouse
def mouse():
	tr.color('red')
	for i in range(45):
		tr.forward(4)
		tr.right(4)
	

circle_1()
move(-65, -70)
circle_2()
move(75, -70)
circle_2()
move(5, -120)
nose(15)
move(65, -200)
mouse()


input()