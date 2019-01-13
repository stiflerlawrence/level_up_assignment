#import the datetime first
from datetime import date
def dateOfBirth(name):
    #initializing the user to enter data
    #try to check if the data entered is correct with a split to allow spaces
    birthday = raw_input('Enter'+ name + '(yyyy mm dd):').split(' ')
    try:
        years = date(int(birthday[0]),int(birthday[1]),int(birthday[2]))
        return years
    except Exception as e:
        #throw an error when the entered data is wrong
        print('{}, you have entered an Invalid date format').format(e)
        #dateOfBirth(name)
def age():
    #Prompt the user to enter data
    birth = dateOfBirth('Your date of birth')
    today = date.today()
    #if the month of birth is less than today's month in that very year we add on 1 year
    #on someone's age
    if ((today.month,today.day) < (birth.month,birth.day)):
        another_year = 1
    else:
        another_year = 0
    your_age = today.year - birth.year - another_year
    return("you have {} years now").format(your_age)
print(age())
