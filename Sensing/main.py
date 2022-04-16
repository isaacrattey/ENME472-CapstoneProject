from PHSensor import PHSensor
import time

phChn = 0
address = 0x48

phSensor = PHSensor(address, phChn)

while True:
    print("%4d" % phSensor.getPh())
    time.sleep(0.1)