import RPi.GPIO as GPIO
import time
import numpy as np
#step = 19, dir = 13

class zaxis():

  def __init__(self, step, dir):
    self.step, self.dir = step, dir
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.step, GPIO.OUT, initial=0)
    GPIO.setup(self.dir, GPIO.OUT, initial=0)
    self.cur_dist = 0

  def home(self, val = 0):
    self.cur_dist = val

  def move(self, dist, speed = 5): #speed in mm/sec

    #calculate steps from angle in radians
    steps = 200*abs(dist - self.cur_dist)/(np.pi*16)
    #the pitch diameter is 16mm

    #if the angle is positive, go one way, negitive go the other
    if dist - self.cur_dist < 0:
      GPIO.output(self.dir,0)
    else:
      GPIO.output(self.dir,1)


    #on and off on the step input for every step
    for i in range(int(steps)):
      GPIO.output(self.step,1)
      time.sleep((16*np.pi)/(speed*200))
      GPIO.output(self.step,0)
      time.sleep((16*np.pi)/(speed*200))
    #reset current angle. steps is only is given by the desired angle minus the current angle
    self.cur_dist = dist
