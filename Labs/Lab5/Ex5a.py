from sense_hat import SenseHat
from text_color import get_color
sense = SenseHat()
sense.set_rotation(0)
sense.clear()

#--- function get_color() ---------------------------


     
#main body program
r_int = get_color("red")
g_int = get_color("green")
b_int = get_color("blue")
print(r_int,g_int,b_int)
msg_color = (r_int, g_int, b_int)
sense.show_message("I got it!", text_colour=msg_color)
