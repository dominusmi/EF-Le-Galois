import os  
from Servo import Servo
import time
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1)
import pigpio


pi = pigpio.pi();

servo = Servo(pi,4)

while True:
	
	servo.change_angle(180)
	time.sleep(1)
	servo.change_angle(0)
	time.sleep(1)
	servo.change_angle(90)
	time.sleep(1)
	servo.change_angle(45)
	time.sleep(1)
