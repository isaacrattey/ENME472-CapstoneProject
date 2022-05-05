import odrive
import time
from odrive.utils import *
from odrive.enums import *
odrv0 = odrive.find_any()
while odrv0.axis0.current_state != AXIS_STATE_IDLE and odrv0.axis0.current_state != AXIS_STATE_CLOSED_LOOP_CONTROL:
	time.sleep(0.1)
	print(str(odrv0.axis0.current_state))
odrv0.clear_errors()
odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
odrv0.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL


while(True):
	odrv0.clear_errors()
	odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
	odrv0.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
	#odrv0.axis0.controller.input_pos = -30
	odrv0.axis1.controller.input_pos = -9
	time.sleep(3)
	print(str(dump_errors(odrv0)))
	#odrv0.axis0.controller.input_pos = 0
	odrv0.axis1.controller.input_pos = 0
	time.sleep(3)
