import turtle as tr

tr.shape('turtle')
h = 1
step = 50
x = -10
y = -10
while h < 11:	
	for i in range(4):
		tr.forward(step)
		tr.left(90)
	tr.penup()
	tr.goto(x, y)
	tr.pendown()
	h += 1
	x -= 10
	y -= 10
	step += 20

input()