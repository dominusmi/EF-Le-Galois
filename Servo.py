import RPi.GPIO as GPIO

class Servo:
	def __init__(self, pi, pin_number):

		self.pi = pi
		self.pin_number = pin_number
                self.pi.set_servo_pulsewidth( self.pin_number, 0 )

	def change_angle(self,angle):
		dc = 9.60*angle+760
		print dc
		self.pi.set_servo_pulsewidth(self.pin_number,dc)

		
	def stop(self):
		self.pi.set_servo_pulsewidth(self.pin_number,dc)
    		self.pi.stop()

		
