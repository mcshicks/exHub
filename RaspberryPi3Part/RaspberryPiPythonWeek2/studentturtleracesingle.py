import turtle
from random import randint
from gpiozero import Button
from gpiozero import LED

# Original Turtle race setup
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

# Add Buttons and LEDs
# TODO Fill in the ?? to add the LED's
# And buttons to the program
red = LED(??)
red.off()
yellow = LED(??)
yellow.off()
button = Button(??)

print("Press the button to start the race")
button.wait_for_press()
for turn in range(100):
    ada.forward(randint(1,10))
    bob.forward(randint(1,10))
# See who won
if(bob.xcor() > ada.xcor()):
    print("Bob won")
    ## TODO Add a statment here to turn on the red led
    
elif(bob.xcor() < ada.xcor()):
    print("Ada won")
    # TODO Add a statmenet to turn on the yellow led
else:  # Tie!
    print("It's a tie!")
    # TODO turn on the leds to your choice for a tie
    # hint choices are led.on(), led.off() and led.blink()
    # where you replace led with red or yellow
    
print("Press button to end program")
button.wait_for_press()
