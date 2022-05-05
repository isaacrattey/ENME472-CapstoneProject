import RPi.GPIO as gpio
import time
import moving.xyaxis as xyaxis
import moving.zaxis as zaxis

gpio.setmode(gpio.BCM)
# Set up solenoid pins
solenoid1Pin = 5
solenoid2Pin = 6
gpio.setup(solenoid1Pin, gpio.OUT)
gpio.setup(solenoid2Pin, gpio.OUT)
z = zaxis.zaxis(step = 19, dir = 13)
xy = xyaxis.xyaxis()