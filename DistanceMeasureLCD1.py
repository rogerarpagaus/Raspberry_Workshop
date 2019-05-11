import Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

trig = 3
echo = 4

spiSettings = SPI.SpiDev(0,0, max_speed_hz=4000000)
d = LCD.PCD8544(23, 24, spi=spiSettings)

d.begin(contrast=60)
d.clear()
d.display ()
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
d.image(image)
d.display()

print('Messung started')
draw.text ((5,10), 'Messung started', font=font)

gpio.setup(trig, GPIO.OUT)
gpio.setup(echo, gpio.IN)

gpio.output(trig,False)

time.sleep(0.5)

gpio.output(trig, True)
time.sleep(o.00001)
gpio.output(trig, False)

while gpio.input (echo) == 0:
    start = time.time()

while gpio.input (echo) == 1:
    stop = time.time()

vergangeZeit = stop - start

entfernung = round(vergangeZeit*34000/2, 2)

print(entfernung)
draw.text ((5,10), entfernung, font=font)
d.image(image)
d.display()