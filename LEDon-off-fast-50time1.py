#Let the LED go on/off 50 times, each status should stay for 30ms.
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)
for i in range (1,50):
	gpio.output(18, gpio.HIGH)
	print(i,' On')	
	time.sleep(0.03)
	gpio.output(18, gpio.LOW)
	print(i,' Off')
	time.sleep(0.03)
gpio.output(18, gpio.LOW)
gpio.cleanup()
Print('End')
