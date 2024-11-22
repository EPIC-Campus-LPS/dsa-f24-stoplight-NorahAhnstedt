import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
red_pin = 20
green_pin = 26
button_pin = 13


GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

state = 0

def set_led_state(state):
    if state == 0:
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.LOW)
    elif state == 1:
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.HIGH)
    elif state == 2:
        GPIO.output(red_pin, GPIO.HIGH)
        GPIO.output(green_pin, GPIO.HIGH)
    elif state == 3:
        GPIO.output(red_pin, GPIO.HIGH)
        GPIO.output(green_pin, GPIO.LOW)
    if state == 4:
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.LOW)
try:
    while True:
        button_state = GPIO.input(button_pin)
        if button_state == GPIO.LOW:
            state = (state + 1)
            set_led_state(state)
            while GPIO.input(button_pin) == GPIO.IN:
                time.sleep(0.1) 
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
