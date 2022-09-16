def get_color(color):
    keep_looping = True
    color_str = 0
    no_of_try , tries_left = 1 , 4

    while keep_looping: 
        tries_left = 3 - no_of_try #tries_left keep track of the number of tries with respect to no_of_try in the exception handling
        if 0 <= tries_left < 4:
            try: #request an int input - if input != int, loop will be thrown into exception handling below
                color_str=int(input("Enter the value of the {} color for message (0 to 255):".format(color)))
                if color_str in range(0,256):
                    return color_str
                else: #call user out if input not within range
                    print("Input not in range between 0-255 [No of tries left:{}]".format(tries_left))
                    no_of_try +=1
            except:#exception handling if input != int
                no_of_try +=1
                print("False input - Integers only [No of tries left:{}]".format(tries_left))
                
        else:
            print("You have enter a invalid value after 3 tries!")
            return 0
