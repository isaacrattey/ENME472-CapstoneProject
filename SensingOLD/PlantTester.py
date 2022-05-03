from Sensor import Sensor
from datetime import datetime
import time

phChn = 0
tempChn = 2
moistureChn = 1
address = 0x48

phSensor = Sensor(address, phChn)
tempSensor = Sensor(address, tempChn)
moistureSensor = Sensor(address, moistureChn)

# while True:
#     ph = phSensor.getReading()
#     temp = tempSensor.getReading()
#     print(f"pH: {ph}\tTemp: {temp}")
#     time.sleep(0.1)

def measure():
    ph = 0.0
    # temp = 0
    moisture = 0.0
    for i in range(5):
        ph += phSensor.getReading()
        # temp = tempSensor.getReading()
        temp = -1.0
        moisture += moistureSensor.getReading()
        time.sleep(.5)
    ph /= 5.0
    moisture /= 5.0
    print(ph, temp, moisture)
    return ph, temp, moisture