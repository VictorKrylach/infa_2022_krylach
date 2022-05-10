import turtle as tr
import numpy as np

tr.shape('turtle')

step = 1

for i in range(200):
	tr.forward(step / (2*np.pi))
	tr.left(50 / np.pi)
	step += 1

input()
