import RPi.GPIO as GPIO


class Motor:

    # Class variables: speed, pin

    def __init__(self, pin):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)

        # Float between 0 and 100
        self.speed = 0

        # Creates the pin object
        self.p = GPIO.PWM(pin, 0.5)

        # Start the pin at 0 power
        self.p.start(0)


    # Speed must be in [0,100]
    def change_speed(self, speed):
        self.p.ChangeDutyCycle(speed)

    # Remove PWM, ready for cleanup
    def clean(self):
        self.p.stop()
