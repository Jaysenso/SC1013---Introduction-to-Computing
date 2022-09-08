from sense_hat import SenseHat
from time import sleep
import random

def wrap(value,minValue,maxValue):
    if value < minValue:
        return maxValue
    elif (value > maxValue):
        return minValue
    #return value

#main body program
sense = SenseHat()
backgroundcolor = 0
CurrentColorIndex = 0
CurrentAngle = 0

while True:
    #heartshape logo
    P = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    print(P)
    O = (0, 0, 0)
    logo = [
        O, O, O, O, O, O, O, O,
        O, P, P, O, P, P, O, O,
        P, P, P, P, P, P, P, O,
        P, P, P, P, P, P, P, O,
        O, P, P, P, P, P, O, O,
        O, O, P, P, P, O, O, O,
        O, O, O, P, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]   

    #to filter out the image[P] from the background[O]
    backgroundcolor = O
    imageList = [i for i in range(0,len(logo)) if (logo[i] != backgroundcolor)]

    AngleSwap = [0,90,180,270]
    rotation = AngleSwap[random.randint(0,3)]
    print(rotation)

    #print logo and rotate 90*
    sense.set_pixels(logo)
    sense.set_rotation(rotation)
    
    sleep(1)