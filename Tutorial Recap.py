#Tutorial 1 Discussion 3
def fizzBuzz ():
    for i in range(1,21):
            if 0 ==  (i % 3) and 0 == (i % 5): #check both multiples of 3 and 5
                print('FizzBuzz')
            elif 0 == (i % 3): #check multiple of 3 
                print('Fizz')
            elif 0 == (i % 5): #check multiple of 5
                print('Buzz')
        
            else:
                print(i)



#Tutorial 1 Discussion 5
def students_percentage():
    number_of_boys = int(input("Enter the number of boys: "))
    number_of_girls =int(input("Enter the number of girls: "))

    def percentage(boys,girls): #function to computate percentages
        total = boys + girls
        boyspercentage = round(boys/total * 100)
        girlspercentage = round(girls/total * 100)
        print("Boys:{}%".format(boyspercentage))
        print("Girls:{}%".format(girlspercentage))
        
    percentage(number_of_boys,number_of_girls) #calls the function : def percentage()
    


#Tutorial 2 Discussion 4 (Looping)
def pattern_printing():
    user_width = int(input("Please enter pattern width: "))

    for width_top in range(0,user_width+1):
        print(width_top * '*')

    for width_bottom in range(user_width+1,0,-1):
        print(width_bottom * '*')



#random behavioural test
def test_dictionary():
    tuple_test = {
        "name" : 'marcus',
        'age' : '22',
        'year' : '2000'
        }
    tuple_test.update({'horoscope' : 'virgo'})
    tuple_test['color'] = 'black'

    x = tuple_test['name']
    y = tuple_test.get('name')


    print(x,y)
    print(tuple_test)



def dataSets():
    #LIST - Square braces
    #TUPLE - Round braces
    #SET - 
    #DICT - Curly braces

    list1 = ['computer','hello',67,88]
    list1[1] = 'PC'
    x = list1.pop(2)
    print(list1,x)

    tuple1 = ('computer','hello',67,88)
    #tuple1[0] = 'PC' - Tuple is immutable
    print(tuple1)

    set1 = {'computer','hello',67,88}
    print(set1)

    dict1 = {
        1: "monday",
        2: "Tueday",
        3: "Wednesday"
    }
    print(dict1)
    dict1.get(1)

def list_test():
    list1 = ['computer','hello',67,88]
    new_list = []

    length = len(list1)

    for i in range(length+1,0,-1):
        x = list1.pop(i)
        print(x)
        
    
    print("{} {}".format(list1,new_list,))



t1 = (1, 2, 3, 3)
t2 = (1, 2, 3, 4)
if t1 < t2:
    print('hi')
else:
    print('bye')