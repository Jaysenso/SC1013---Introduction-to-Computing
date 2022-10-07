from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

while True:
    sense.clear()
    for positions in range(4):
        xIndex = random.randint(0,7)
        yIndex = random.randint(0,7)
        randomcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        print(randomcolor)
        sense.set_pixel(xIndex,yIndex,tuple(randomcolor))
    sleep(1)
        

    