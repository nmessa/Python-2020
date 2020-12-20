import RPi.GPIO as GPIO
GPIO.setwarnings(False)   #Disable warnings for any not reset pins
GPIO.setmode(GPIO.BCM)    #Allow ARM processor to access GPIO
GPIO.setup(18, GPIO.OUT)  #set pin 18 to output
GPIO.output(18, True)	#Turn LED on
