from datetime import date
def dateOfBirth(name):
    birthday = raw_input('Enter'+ name + '(yyyy mm dd):').split(' ')
    try:
        years = date(int(birthday[0]),int(birthday[1]),int(birthday[2]))
        return years
    except Exception as e:
        print('{}, you have entered an Invalid date format').format(e)
        dateOfBirth(name)
def age():
    birth = dateOfBirth('Your date of birth')
    today = date.today()
    if ((today.month,today.day) < (birth.month,birth.day)):
        another_year = 1
    else:
        another_year = 0
    your_age = today.year - birth.year - another_year
    return("you have {} years now").format(your_age)
print(age())
