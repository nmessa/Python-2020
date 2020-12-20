#SOS code generator

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    #S
    for i in range(3):
        GPIO.output(18, True)
        time.sleep(.1)
        GPIO.output(18, False)
        time.sleep(.1)
    time.sleep(0.5)

    #O
    for i in range(3):
        GPIO.output(18, True)
        time.sleep(1)
        GPIO.output(18, False)
        time.sleep(.1)
    time.sleep(0.5)

    #S
    for i in range(3):
        GPIO.output(18, True)
        time.sleep(.1)
        GPIO.output(18, False)
        time.sleep(.1)
    time.sleep(1.5)
