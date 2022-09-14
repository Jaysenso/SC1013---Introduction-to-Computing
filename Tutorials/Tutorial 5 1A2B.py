from random import randint

def bulls_and_cows():
    count = 1
    #generate random 4 digits as my solution/target answer
    random_number = [randint(1,9) for i in range(4)]
    if len(random_number) == 4:
        target_number = random_number
        print("**TESTING** - target no. : {}".format(target_number))

    #main body
    while True:
        num_digits = input('Please input 4 digits :')
        if num_digits.isdigit() == True and len(num_digits) == 4:
            #populate user's input in list[user_guess] eg. num_digits = 1111 => user_guess = [1,1,1,1]
            user_guess = [int(num) for num in num_digits]
            
        else:
            print("4 Digits Integer only")
            continue
        
          
        
        if user_guess == target_number:
            print("You win!!")
            break   

        else:
            #initialize cow,bull = 0 in while loop 
            cow = 0
            bull = 0
            
            for x in range(0,4):
                #First check whether any of the numbers aligned with solution
                if user_guess[x] == target_number[x]:
                    bull += 1
                #Second check whether any numbers are present in solution
                elif user_guess[x] in target_number:
                    cow += 1

        #Count to keep track of attempt (no. of loops)            
        count +=1
        
        print("{} A (Bulls) {} B (Cows)".format(bull,cow))

    print("Attempts:{}".format(count))


     
bulls_and_cows()  
     


    



   
   
