import turtle as tr
import numpy as np

def drow_star_n_angles(n, step):
		tr.left(180)
		for i in range(n):
			tr.left(180 - (180 / n))
			tr.forward(step)

drow_star_n_angles(17, 200)

input()
