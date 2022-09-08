multipli = int(input("Enter a number between 1 to 9:")) 

while ( multipli < 1 or multipli > 9):
    print("Number must be between 1 to 9!")
    multipli = int(input("Enter a number between 1 to 9:")) 
else:
     for i in range(-1,11):
      result = i * multipli
      print(i,"x",multipli,"=",result)







