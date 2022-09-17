
def MergeSort (DataSet):
    SizeOfData = len(DataSet) 
    #print(DataSet)
    #Slices the list into 2 sub-list
    if SizeOfData < 2: #condition to stop the recursion,when data slices into single element
        return DataSet
    else:
        left_list = DataSet[:SizeOfData // 2] 
        right_list = DataSet[SizeOfData //2:]
        left_list = MergeSort(left_list) #recusion for left till single element
        right_list = MergeSort(right_list) #recursion for right
    return Merge(left_list,right_list) 

def Merge(left_list,right_list):
    #a secondary list for the sorted items
    resultlist = [] 
    #while left and right have elements
    while left_list and right_list: 
        #compare 1st element of both lists and append the smallest into resultlist
        if left_list[0] > right_list[0]:
            resultlist.append(right_list[0])
            right_list.pop(0)
        elif left_list[0] < right_list[0]:
            resultlist.append(left_list[0])
            left_list.pop(0)
    #if the corresponding list still contain elements, append everything to the result list
    if left_list:
        resultlist.extend(left_list)
    else:
        resultlist.extend(right_list)   
    return resultlist


List_of_items = [6,9,8,2,1,10]
sorted_list = MergeSort(List_of_items)
for items in sorted_list:
    print(items,end =',')
