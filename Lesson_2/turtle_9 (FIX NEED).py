import turtle as tr
import numpy as np

tr.shape('turtle')

tr.left(150)
def drow_figure(angle, step, x):
	for i in range(angle):
			tr.forward(step)
			tr.left(360 / angle)
	tr.penup()
	tr.goto(x, 0)
	tr.pendown()

drow_figure(3, 60, 10)
drow_figure(4, 80, 20)
drow_figure(5, 100, 30)

input()