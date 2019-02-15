from turtle import *
from random import randint

ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()
bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160, 70)    
bob.pendown()


for turn in range(100):
	ada.forward(randint(1,5))
	bob.forward(randint(1,5))
