import turtle as tr

tr.shape('turtle')

def sercle(step1, step2):
	for i in range(45):
		tr.forward(step1)
		tr.right(4)
	for i in range(45):
		tr.forward(step2)
		tr.right(4)

tr.left(90)
sercle(4, 1)
sercle(4, 1)
sercle(4, 1)
sercle(4, 1)
sercle(4, 1)
sercle(4, 1)

input()