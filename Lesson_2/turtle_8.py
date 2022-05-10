import turtle as tr
tr.shape('turtle')

step = 10

for i in range(24):
	tr.forward(step)
	tr.left(90)
	step += 4

input()