def cube(number):
    return number*number*number
def xyz(number):
    if number%3==0:
        return cube(number)
    else:
        return False
print(xyz(9))
print(xyz(4))