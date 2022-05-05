import RPi.GPIO as GPIO
import time

step = 19
dir = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(step, GPIO.OUT, initial=0)
GPIO.setup(dir, GPIO.OUT, initial=0)

steps = 200

for i in range(steps):
	GPIO.output(step,1)
	time.sleep(.01)
	GPIO.output(step,0)
	time.sleep(.01)
