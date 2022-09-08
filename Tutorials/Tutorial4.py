def printUI():
    print("Wecome to the grading system! Please enter your option:")
    print("1: Input Record")
    print("2: Query a student")
    print("3: list grades in a group")
    print("4: get max in a group")
    print("5: list all group names")
def inputRecord(group_name, student_id, student_score):
        dataBase[(group_name,student_id)] = student_score
      
def query(dataBase,group_name, student_id):
    for key,value in dataBase.items()

    


#main program body
while True:
    dataBase = {}
    #UI and error handling
    printUI()
    option = input("option:")
    if (option.isdigit() == False):
        ("Invalid option.")
        continue

    #option 1 selector    
    option = int(option)
    if (option == 1):
        group_name = str(input("Please input the group name: "))
        student_id = str(input("Please input the student id:"))
        student_score = str(input("Please input the score:"))
        inputRecord(group_name, student_id, student_score)

    elif (option == 2):
        groupName = str(input("Please input the group name: "))
        studentID = str(input("Please input the student id: "))
        student_score = query(dataBase,group_name, student_id)

    



       

 
    







