
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.IN)
counter = 1
def move():
    while True:
        if GPIO.input(18) == 0:
            return 1
