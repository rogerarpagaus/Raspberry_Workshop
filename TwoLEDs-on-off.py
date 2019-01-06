# Code for switching two LEDs on/off based on a selection, one on Pin 18 and one on Pin 23.

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)
gpio.setup(23, gpio.OUT)

color = input ("which color should be on, yellow or green")
if color == "yellow":
  gpio.output(23, gpio.HIGH)
  time.sleep(2)
  gpio.output(23, gpio.LOW)

if color == "green":
  gpio.output(18, gpio.HIGH)
  time.sleep(2)
  gpio.output(18, gpio.LOW)

gpio.cleanup()
