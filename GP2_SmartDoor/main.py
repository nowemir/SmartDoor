import motion
import RPi.GPIO as GPIO
import temperature
import faceMaseDetact as FMD
from time import sleep

def OpenDoor():
    GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
     
def CloseDoor():
    GPIO.setup(20,GPIO.OUT,initial =GPIO.HIGH) 
def GreenLED():
    
    GPIO.setup(5,GPIO.OUT,initial=GPIO.HIGH)
    sleep(1)
    GPIO.setup(5,GPIO.OUT,initial =GPIO.LOW) 

def RedLED():
    
    GPIO.setup(6,GPIO.OUT,initial=GPIO.HIGH)
    sleep(1)
    GPIO.setup(6,GPIO.OUT,initial =GPIO.LOW) 

def WhiteLED():
 
    GPIO.setup(13,GPIO.OUT,initial=GPIO.HIGH)
    sleep(1)
    GPIO.setup(13,GPIO.OUT,initial =GPIO.LOW) 

def YellowLED():
    
    GPIO.setup(19,GPIO.OUT,initial=GPIO.HIGH)
    sleep(1)
    GPIO.setup(19,GPIO.OUT,initial =GPIO.LOW) 

def BlueLED():
    
    GPIO.setup(26,GPIO.OUT,initial=GPIO.HIGH)
    sleep(1)
    GPIO.setup(26,GPIO.OUT,initial =GPIO.LOW) 

try: 
    BlueLED()
    while True:
        
        move = motion.move()
 
        if move == 1:

            temp = temperature.temp()
            if float(temp) <= 35:

                WhiteLED()
                print('your temperature is ', temp)

                while True:
                    FMD_result = int(FMD.faceMaskDetacted())
                    if FMD_result == -1:
                        YellowLED()

                        print('let me try again')
                    if FMD_result == 0:

                        OpenDoor()
                        GreenLED()
   
                        print('chaked done succsessful. Dore is Open')
                        sleep(3)
                        CloseDoor()
                        break
                    if FMD_result == 1:

                        print('Sorry, you donnot allow to Enter without facemask')
                        RedLED()
                        break
            else:
                print('Sorry, your Temperature is High')
finally:
    GPIO.cleanup()


