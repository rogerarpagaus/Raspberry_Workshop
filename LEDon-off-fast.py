import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)
gpio.output(18, gpio.HIGH)
time.sleep(0.1)
gpio.output(18, gpio.LOW)
time.sleep(0.1)
gpio.output(18, gpio.HIGH)
time.sleep (0.1)
gpio.output(18, gpio.LOW)
gpio.cleanup()