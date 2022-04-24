from Sensor import Sensor
import time

phChn = 0
tempChn = 1
address = 0x48

phSensor = Sensor(address, phChn)
tempSensor = Sensor(address, tempChn)

while True:
    ph = phSensor.getReading()
    temp = tempSensor.getReading()
    print(f"pH: {ph}\tTemp: {temp}")
    time.sleep(0.1)