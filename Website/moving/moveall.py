import xyaxis
import zaxis
import time

z = zaxis.zaxis(step = 19, dir = 13)
xy = xyaxis.xyaxis()

while True:
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


