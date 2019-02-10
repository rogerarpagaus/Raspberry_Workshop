#!/usr/bin/python3
# RGB LED for Raspberry Pi B+ in build in case
import RPi.GPIO as gpio
import time
import random

gpio.setmode(gpio.BCM)
ledPin = [13,19,26]
gpio.setup(ledPin[0], gpio.OUT)
gpio.setup(ledPin[1], gpio.OUT)
gpio.setup(ledPin[2], gpio.OUT)
while True:
  gpio.output(ledPin[0], gpio.HIGH)
  time.sleep(1)
  gpio.output(ledPin[0], gpio.LOW)
  gpio.output(ledPin[1], gpio.HIGH)
  time.sleep(1)
  gpio.output(ledPin[1], gpio.LOW)
  gpio.output(ledPin[2], gpio.HIGH)
  time.sleep(1)
  gpio.output(ledPin[2], gpio.LOW)
  gpio.output(ledPin[0], gpio.HIGH)
  gpio.output(ledPin[1], gpio.HIGH)
  time.sleep(1)
  gpio.output(ledPin[0], gpio.LOW)
  gpio.output(ledPin[1], gpio.LOW)
  gpio.output(ledPin[0], gpio.HIGH)
  gpio.output(ledPin[2], gpio.HIGH)
  time.sleep(1)
  gpio.output(ledPin[0], gpio.LOW)
  gpio.output(ledPin[2], gpio.LOW)
  gpio.output(ledPin[1], gpio.HIGH)
  gpio.output(ledPin[2], gpio.HIGH)
  time.sleep(1)
  gpio.output(ledPin[1], gpio.LOW)
  gpio.output(ledPin[2], gpio.LOW)
