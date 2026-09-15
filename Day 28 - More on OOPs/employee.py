class Employee:

    def __init__(self):
        print("Employee has entered.")

    def __del__(self):
        print("Employee has left.")


def Create_obj():
    print("Making object..")
    obj=Employee()
    print("Function end..")
    return obj

print("Calling Create_obj() Functions..")
obj=Create_obj()
print("Program end..")