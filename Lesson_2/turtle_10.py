import turtle as tr

tr.shape('turtle')

def sercle_left():
	for i in range(90):
		tr.forward(4)
		tr.left(4)
def sercle_right():
	for i in range(90):
		tr.forward(4)
		tr.right(4)
sercle_left()
sercle_right()
tr.right(45)
sercle_left()
sercle_right()
tr.right(90)
sercle_left()
sercle_right()


input()