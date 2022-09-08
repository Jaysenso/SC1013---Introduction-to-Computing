import random
random_number = random.randint(0,100)
print(random_number)
guess_number = int(input("Guess the number:"))


while (guess_number != random_number): 
 if random_number > guess_number:
     print("Input is higher")

 elif random_number < guess_number:
     print("Number is lower") 

 else:
     print("The number is:",random_number)

 guess_number = int(input("Guess the number:"))




