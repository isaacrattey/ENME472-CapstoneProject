from Sensor import Sensor
import time

phChn = 0
address = 0x48

phSensor = Sensor(address, phChn)

while True:
    print("%4f" % phSensor.getReading())
    time.sleep(0.1)