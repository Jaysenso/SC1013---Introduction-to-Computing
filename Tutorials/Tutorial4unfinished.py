


from itertools import count
from multiprocessing.sharedctypes import Value


def printUI():
    print("\nWecome to the grading system! Please enter your option:")
    print("1: Input Record")
    print("2: Query a student")
    print("3: list grades in a group")
    print("4: get max in a group")
    print("5: list all group names")

def inputRecord(dataBase,group_name, student_id, student_score):
    dataBase[group_name,student_id] = student_score
        
def query(dataBase,group_name,student_id):
    try:
        student_score = 0
        student_score = dataBase[group_name,student_id]
        return student_score
    except KeyError:
        return -1

def listGrades(dataBase): 
    list_Grades = list(dataBase.items())
    return list_Grades


#main program body1
dataBase = {}    
student_id, student_score = 0,0
count = 1


while True:
    #UI and error handling
    printUI()
    option = input("option:")
    if (option.isdigit() == False):
        ("Invalid option.")
        continue
 
    #option 1 selector    
    option = int(option)
    if (option == 1):
        group_name = input("Please input the group name: ")
        try:
            student_id = int(input("Please input the student id no. {}:".format(count)))
            student_score = int(input("Please input the score:"))
            inputRecord(dataBase,group_name, student_id, student_score)
            print(dataBase.items())
            count+=1
        except ValueError:
            print()
           
    elif (option == 2):
        group_name = input("Please input the group name: ")
        student_id= int(input("Please input the student id: "))

        student_score = query(dataBase,student_id)
        if (student_score == -1):
           print("Invalid key,please re-enter")
        else:
            print("{:<15}{:<15}".format("Student ID", "Score"))
            print ("{:<15}{:<15}".format(student_id,student_score))
            
    elif (option == 3):
        group_name = input("Please input the group name: ")
        print("{:<15}{:<15}".format("Student ID", "Score"))
        for key,value in dataBase.items():
            print ("{:<15}{:<15}".format((key),value))

        
        


    

    



       

 
    







