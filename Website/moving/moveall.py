import moving.xyaxis
import moving.zaxis
import time

z = moving.zaxis.zaxis(step = 19, dir = 13)
xy = moving.xyaxis.xyaxis()

xy.move(0,0)
z.move(150)
xy.move(0,70)
time.sleep(3)


xy.move(0,0)
z.move(0)
time.sleep(3)

z.move(0)
xy.move(300,380)
z.move(150)
time.sleep(3)



xy.move(300,440)
time.sleep(3)



xy.move(300,380)
z.move(0)
xy.move(0,0)
time.sleep(3)


