from Sensing.PCF8591 import PCF8591

class Sensor:

    def __init__(self, address, chn):
        self.adc = PCF8591(address)
        self.senseChn = chn

    def getReading(self):
        return self.adc.read(self.senseChn)
