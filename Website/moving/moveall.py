import xyaxis
import zaxis
import time

z = zaxis.zaxis(step = 19, dir = 13)
xy = xyaxis.xyaxis()

#z.move(100)
#xy.move(90,0)
xy.move(90,90)
time.sleep(3)

#z.move(0)
#xy.move(90,0)
xy.move(0,0)
time.sleep(3)
