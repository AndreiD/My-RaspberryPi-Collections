import RPi.GPIO as GPIO
from time import sleep
from random import randint

servoPIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

pwm = GPIO.PWM(servoPIN, 50)

pwm.start(0)  # Initialization


def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servoPIN, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoPIN, False)
    pwm.ChangeDutyCycle(0)


SetAngle(0)
print("Starting...")
try:
    while True:
        print(".")
        sleep(randint(10, 40))

        SetAngle(90)
        SetAngle(0)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("Bye")
