import moving.xyaxis
import moving.zaxis
import time

z = moving.zaxis.zaxis(step = 19, dir = 13)
xy = moving.xyaxis.xyaxis()
# move to tray position
# already done
# move z into position
z.move(150)
# move y down into tray
xy.move(0, 130)
#collect data for tray1