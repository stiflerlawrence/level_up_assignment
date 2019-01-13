#define a method with aList as the  parameter
def grade(aList):
    #pos meaning position
    #the for loops through the length of list to find all elements in the list
    for pos in range(len(aList)):
        if aList[pos] < 49:
            print("{} is F").format(aList[pos])
        elif aList[pos] > 49 and aList[pos] < 60:
            print("{} is E").format(aList[pos])
        elif aList[pos] > 59 and aList[pos] < 70:
            print("{} is D").format(aList[pos])
        elif aList[pos] > 69 and aList[pos] < 80:
            print("{} is C").format(aList[pos])
        elif aList[pos] > 79 and aList[pos] < 90:
            print("{} is B").format(aList[pos])
        elif aList > 89 and aList[pos] < 101:
            print("{} is A").format(aList[pos])
        else:
            print("is out of range")
    return aList
#here we define our list
bList = [4,56,93,67,34,76]

#we call the list with the argument as the defined list above
grade(bList)
