SOLENOID1_PIN = 3
SOLENOID2_PIN = 3

import RPi.GPIO as gpio
import time

print("Hello")

# Set up the gpio
gpio.setmode(gpio.BCM)

# Inputs

# Outputs
gpio.setup(SOLENOID1_PIN, gpio.OUT)
gpio.setup(SOLENOID2_PIN, gpio.OUT)


# Read the current value
