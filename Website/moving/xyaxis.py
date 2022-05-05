import odrive
import time
import numpy as np
from odrive.utils import *
from odrive.enums import *

class xyaxis():

  def __init__(self):
      self.pitch = 2 #mm/rot
      self.pulley_diameter = 12.5 #mm
      self.drv = odrive.find_any() #detect a driver
      while self.drv.axis0.current_state != AXIS_STATE_IDLE and self.drv.axis0.current_state != AXIS_STATE_CLOSED_LOOP_CONTROL:
        time.sleep(0.1)

      if self.drv.axis0.is_homed == False:
        self.drv.axis0.requested_state = AXIS_STATE_HOMING

      if self.drv.axis1.is_homed == False:
        self.drv.axis1.requested_state = AXIS_STATE_HOMING

      #just incase anything weird happend since the last boot, clear any errors
      self.drv.clear_errors()

      #start closed loop control
      self.drv.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
      self.drv.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL


  def move(self, posx, posy, speedx = 50, speedy = 50): #pos in mm, #speed in rot/s

    self.drv.axis1.controller.config.vel_limit = speedx
    self.drv.axis0.controller.config.vel_limit = speedy
    self.curr_pos = [posx, posy] #current position for internal refrence

    setpointy = -1*posy/(self.pitch) #calculating the val in turns/s that needs to be given to the driver
    setpointx = -1*posx/(np.pi*self.pulley_diameter)
    self.drv.axis1.controller.input_pos = setpointx
    self.drv.axis0.controller.input_pos = setpointy
    while abs(self.drv.axis1.encoder.pos_estimate - setpointx) >0.05 or abs(self.drv.axis0.encoder.pos_estimate - setpointy) >0.05:
        print(self.drv.axis0.encoder.error)
        if self.drv.axis0.encoder.error != 0 or self.drv.axis0.encoder.error != 0 or self.drv.error != 0:
            print(str(dump_errors(self.drv)))
            self.drv.clear_errors()
            self.drv.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
            self.drv.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
            self.drv.axis1.controller.input_pos = setpointx
            self.drv.axis0.controller.input_pos = setpointy
        time.sleep(0.05)
        print(self.drv.axis1.encoder.pos_estimate - setpointx)
