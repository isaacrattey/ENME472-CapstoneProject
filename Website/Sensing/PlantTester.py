from Sensor import Sensor
from datetime import datetime

phChn = 0
tempChn = 1
address = 0x48

phSensor = Sensor(address, phChn)
tempSensor = Sensor(address, tempChn)

# while True:
#     ph = phSensor.getReading()
#     temp = tempSensor.getReading()
#     print(f"pH: {ph}\tTemp: {temp}")
#     time.sleep(0.1)

def TestPlant(plantNum):
    # Move to that plant
    # Gantry code...
    #     
    # 
    #     
    ph = phSensor.getReading()
    temp = tempSensor.getReading()
    return ph, temp