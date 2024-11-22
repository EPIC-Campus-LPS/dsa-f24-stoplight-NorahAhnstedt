#imports python library "RPi.GPIO" which is used to control GPIO pins on rasperry PI and then reassigns it a shorter name, now when we type in GPIO we aew using the module RPi.GPIO
import RPi.GPIO as GPIO 
#imports the "time" module which allows the program to pause for a number of seconds
import time 
#specifying that the mode of the pins in BCM (broadcom) specifys the way that the pins are numbered, now when we say pin 17 it refers to the number based on the Broadcom chip 
GPIO.setmode(GPIO.BCM)

#defining the list led_pins with the list including GPIO 17, GPIO 26, GPIO 18
led_pins = [17, 26, 18]

#for every value (17,26,18) in the list pins do the following line of code 
for pin in led_pins:
	#specifies the pin as an output. Pin is saying the it will 1st be 17 then 26 then 18. GPIO.OUT means that the pins is RECIVING signals and then controling external devices. 
	#since this line follows a for loop each pin will be assigned as an output at some point
	GPIO.setup(pin, GPIO.OUT)

#this for loops does the same thing as the one before
for pin in led_pins:
	#however now it says the output pin should be turned on high (this turns on the light)
	GPIO.output(pin, GPIO.HIGH)
	#these if statements speficy how long the code should pause for each variable which is how we make yellow turn on an off a lot quicker then the others
	#it also says to turn offf the light after the code has been paused for x amount of time 
	if pin == 17:
		time.sleep(5)
		GPIO.output(pin, GPIO.OUT)
	elif pin == 26:
		time.sleep(1) 
		GPIO.output(pin, GPIO.OUT)
	elif pin == 18:
		time.sleep(4)
		GPIO.output(pin, GPIO.OUT)
#returns all the the GPIO pins to their previous state before the code was run 
GPIO.cleanup()
