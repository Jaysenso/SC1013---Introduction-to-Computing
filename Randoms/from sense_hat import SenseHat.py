from sense_hat import SenseHat
import time
import random
sense = SenseHat()

while True:
  random_colors = []
  for i in range(3):
    random_colors.append(random.randint(0,255))
    print(random_colors)
    
  colors = tuple(random_colors) 
  red = (255,255,0)
  print(red) 
  
  sense.set_pixel(0,0,colors)
  sense.set_pixel(0,7,colors)
  sense.set_pixel(7,0,colors)
  sense.set_pixel(7,7,red)
  time.sleep(1)
  