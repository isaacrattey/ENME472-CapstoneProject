import moving.xyaxis
import moving.zaxis
import time

z = moving.zaxis.zaxis(step = 19, dir = 13)
xy = moving.xyaxis.xyaxis()


xy.move(300, 380)
z.move(150)
xy.move(300, 440)