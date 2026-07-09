def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
try:
    print("*CALCULATOR*")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    option=int(input("Enter your option: "))
    num1=float(input("Enter number 1: "))
    num2=float(input("Enter number 2: "))
    if option==1:
        print("Answer = ", add(num1,num2))
    elif option==2:
        print("Answer = ", subtract(num1,num2))
    elif option==3:
        print("Answer = ", multiply(num1,num2))
    elif option==4:
        print("Answer = ", divide(num1,num2))
except ZeroDivisionError:
    print("Error")
except ValueError:
    print("Error")
