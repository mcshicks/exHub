import turtle
from random import randint
from mpu6050 import mpu6050
from gpiozero import Button
from gpiozero import LED

# Create the LED and Button Objects
red = LED(18)
red.off()
yellow = LED(24)
yellow.off()
button = Button(25)

# Create the acceleromoter object
sensor = mpu6050(0x68)
accel_data = sensor.get_accel_data()
gyro_data = sensor.get_gyro_data()
heading = 0  # 
speed = 0
XMAX = 160

ada = turtle.Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160, 00)
ada.pendown()
bob = turtle.Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160, 70)
bob.pendown()
runRace = False
maximum = 0


def startRace():
    global runRace
    global speed
    runRace = True
    speed = 0
    ada.goto(-160, 00)
    bob.goto(-160, 70)
    ada.clear()
    bob.clear()
    bob.seth(randint(1, 360))  # start out in Random direction
    red.off()
    yellow.off()


# Use the button to start/restart the race
button.when_pressed = startRace


def updateGyro():
        global heading
        global speed
        accel_data = sensor.get_accel_data()
        gyro_data = sensor.get_gyro_data()
        heading = heading + accel_data['y']
        speed = speed - accel_data['x']/10.0
        speed = max(0, speed)
        speed = min(speed, 10)
        # Call update gyro every 50 ms
        turtle.getscreen().ontimer(updateGyro, 50)


def race():
        global heading
        global speed
        global runRace
        if(runRace):
            bob.seth(heading)  # Update Bob's heading
            bob.forward(randint(1, 5) + speed)  # Bob can go faster
            ada.forward(randint(1, 5))
            xbob = bob.xcor()
            xada = ada.xcor()
            maximum = max(xbob, xada)
            if(maximum > XMAX):  # Do we have a winner?
                if(bob.xcor() > ada.xcor()):
                    print("Bob won")
                    red.blink()
                elif(bob.xcor() < ada.xcor()):
                    print("Ada won")
                    yellow.blink()
                else:  # Tie!
                    print("It's a tie!")
                    red.blink()
                    yellow.blink()
                runRace = False
        # Call update the race every 100 ms
        turtle.getscreen().ontimer(race, 100)


updateGyro()
race()
turtle.mainloop()
