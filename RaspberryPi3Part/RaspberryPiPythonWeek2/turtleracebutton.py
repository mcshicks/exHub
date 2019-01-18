import turtle
from random import randint
from gpiozero import Button
from gpiozero import LED

red = LED(18)
red.off()
yellow = LED(24)
yellow.off()
button = Button(25)
ada = turtle.Turtle()
ada.color('yellow')
ada.shape('turtle')
ada.penup()
ada.goto(-160, 100)
ada.pendown()
bob = turtle.Turtle()
bob.color('red')
bob.shape('turtle')
bob.penup()
bob.goto(-160, 70)
bob.pendown()

while(True):
    try:
        button.wait_for_press()
        red.off()
        yellow.off()
        ada.goto(-160, 100)
        bob.goto(-160, 70)
        bob.clear()
        ada.clear()
        for turn in range(100):
            ada.forward(randint(1,10))
            bob.forward(randint(1,10))
        if(bob.xcor() > ada.xcor()):
            print("Bob won")
            red.on()
        elif(bob.xcor() < ada.xcor()):
            print("Ada won")
            yellow.on()
        else:
            red.blink()
            yellow.blink()
    except KeyboardInterrupt:
        exit()



