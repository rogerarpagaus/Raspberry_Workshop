import Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

trig = 17
echo = 27

spiSettings = SPI.SpiDev(0,0, max_speed_hz=4000000)
d = LCD.PCD8544(23, 24, spi=spiSettings)

d.begin(contrast=60)
d.clear()
d.display ()
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
draw = ImageDraw.Draw(image)
draw .rectangle((0,0,84,84), outline=255, fill=255)
font = ImageFont.load_default()
draw.text ((5,10), 'Messung Start', font=font)
d.image(image)
d.display()
gpio.setup(22,gpio.IN,pull_up_down=gpio.PUD_UP)
print('Messung started')

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)

# Schlaufe start
while True:
    draw .rectangle((0,0,84,84), outline=255, fill=255)
    #buttonPressed = gpio.input(22)
    #if buttonPressed == 1:
    gpio.output(trig,False)

    time.sleep(0.5)

    gpio.output(trig, True)
    time.sleep(0.00001)
    gpio.output(trig, False)

    while gpio.input (echo) == 0:
        start = time.time()

    while gpio.input (echo) == 1:
        stop = time.time()

    vergangeZeit = stop-start

    entfernung = round(vergangeZeit*343200/2, 2)
    Einheit = "mm"
    Text = "Distanz ist"
    Meldung = str(entfernung) + Einheit
    #print(Text)
    #print(Meldung)
    draw.text ((5,20), Text, font=font)
    draw.text ((5,30), Meldung, font=font)
    d.image(image)
    d.display()
