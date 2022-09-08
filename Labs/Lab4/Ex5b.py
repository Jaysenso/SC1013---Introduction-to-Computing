from sense_hat import SenseHat
from time import sleep
import random

def wrap(value,minValue,maxValue):
    if value < minValue:
        return maxValue
    elif (value > maxValue):
        return minValue
    return value

#main body program
sense = SenseHat()
backgroundcolor = 0
CurrentColorIndex = 0
CurrentAngle = 0

yellow = (255, 255, 0)
red = (255, 0, 0)
pink = (255,105, 180)
nothing = (0, 0, 0)

#heartshape logo
P = pink
O = nothing
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

while True:
    ColorSwap = (yellow,red)
    AngleSwap = [0,90,180,270]

    CurrentColorIndex = wrap(CurrentColorIndex+1,0,len(ColorSwap) - 1 )
    for indexes in imageList:
        logo[indexes] = ColorSwap[CurrentColorIndex]

    rotation = AngleSwap[random.randint(0,3)]

    #print logo and rotate 90*
    sense.set_pixels(logo)
    sense.set_rotation(rotation)
    sleep(1)