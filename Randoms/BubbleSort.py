import random
def bubblesort(alist):
    highest = 0
    count = 0
    for index_number in range(len(alist) - 1):
        swapped = False
        for i in range(len(alist) - index_number - 1):
            if alist[i] > alist[i+1]:
                highest = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = highest
                count += 1
                swapped = True
    print("Pass: {} {}".format(index_number + 1,alist))
    print(count)
                
def random_populate(Datasize):
    Generatedlist =[]
    for i in range (0,Datasize):
        randomNumber = random.randint(0,i)
        Generatedlist.append(randomNumber)
    return Generatedlist
        


alist = random_populate(1000)
bubblesort(alist)   
