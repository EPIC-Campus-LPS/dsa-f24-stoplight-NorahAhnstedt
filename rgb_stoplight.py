import RPi.GPIO as GPIO 
#imports the "time" module which allows the program to pause for a number of seconds
import time 
#specifying that the mode of the pins in BCM (broadcom) specifys the way that the pins are numbered, now w>
GPIO.setmode(GPIO.BCM)
#defining the list led_pins with the list including GPIO 17, GPIO 26, GPIO 18
led_pins = [26, 20, 20]
for pin in led_pins:
	GPIO.setup(pin, GPIO.OUT)
for pin in led_pins:
	if pin == 26:
		GPIO.output(26, GPIO.HIGH)
		time.sleep(5)
		GPIO.output(26, GPIO.OUT)
	if pin == 20: 
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(20, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(26, GPIO.OUT)
		GPIO.output(20, GPIO.OUT)
		GPIO.output(20, GPIO.HIGH)
		time.sleep(4)
		GPIO.output(20, GPIO.OUT)
		break
#returns all the the GPIO pins to their previous state before the code was run 
GPIO.cleanup()





