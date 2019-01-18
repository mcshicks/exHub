import turtle
from random import randint
from mpu6050 import mpu6050
from time import sleep

sensor = mpu6050(0x68)


ada = turtle.Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()
bob = turtle.Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160, 70)    
bob.pendown()

def updateGyro():
        accel_data = sensor.get_accel_data()
        gyro_data = sensor.get_gyro_data()
        turtle.getscreen().ontimer(updateGyro, 50)

def race():
        ada.seth(gyro_data['z'])
        ada.forward(randint(1, 5))
        bob.forward(randint(1, 5))
        turtle.getscreen().ontimer(race, 100)

updateGyro()
race()
turtle.mainloop()
      
        
