from Motor import Motor
import time

motor = Motor(7)

motor.change_speed(50)

time.sleep(1)

motor.change_speed(0)
motor.clean()
