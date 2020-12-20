import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)   #Disable warnings for any not reset pins
GPIO.setmode(GPIO.BCM)    #Allow ARM processor to access GPIO
GPIO.setup(18, GPIO.OUT)  #set pin 18 to output

#Make LED blink
while True:
    GPIO.output(18, True)
    time.sleep(1)
    GPIO.output(18, False)
    time.sleep(.1)
