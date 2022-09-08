
while(True):


 input_prime = int(input("Enter a number:"))
 for n in range(2,int(input_prime/2)+1):  #not possible for any number larger than input_prime/k to divide evenly into k
        if input_prime%n == 0: 
           isprime = False
        break
 else:
        isprime = True
 print("The number is a prime number:",isprime)


