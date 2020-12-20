import RPi.GPIO as GPIO
import time
import random

left_name = raw_input('Enter left player name: ')
right_name = raw_input('Enter right player name: ')
names = [left_name, right_name]

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

led = 4
right_button = 15
left_button = 14

GPIO.setup(led, GPIO.OUT)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)

GPIO.output(led, 0)
time.sleep(random.uniform(5, 10))
GPIO.output(led, 1)

while True:
    if GPIO.input(left_button) == False:
        print names[0],"won"
        break
    if GPIO.input(right_button) == False:
        print names[1], "won"
        break

GPIO.cleanup()
    
