import turtle as tr

tr.shape('turtle')

def sercle(step):
	for i in range(90):
		tr.forward(step)
		tr.left(4)
	for i in range(90):
		tr.forward(step)
		tr.right(4)
tr.right(90)
sercle(3)
sercle(4)
sercle(5)
sercle(6)
sercle(7)
sercle(8)
sercle(9)
sercle(10)

input()