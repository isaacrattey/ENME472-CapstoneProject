# TEMP_PIN = 1
# PH_PIN = 0
# CHANNEL = 0x48

# import RPi.GPIO as gpio
# import time
from PCF8591 import PCF8591

class PHSensor:

    def __init__(self, address, chn):
        self.adc = PCF8591(address)
        self.phChn = chn

    def getPh(self):
        return self.adc.read(self.phChn)

# print("Hello")

# # Set up the gpio
# gpio.setmode(gpio.BCM)

# # Inputs
# gpio.setup(TEMP_PIN, gpio.IN)
# gpio.setup(PH_PIN, gpio.IN)

# # Outputs
# gpio.setup(18, gpio.OUT)


# Read the current value
