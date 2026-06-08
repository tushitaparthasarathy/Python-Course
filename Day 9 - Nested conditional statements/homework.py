age = int(input("Enter student's age: "))
if age >= 10:
    if age <= 20:
        print("Student can enroll in the class.")
    else:
        print("Student cannot enroll. Age is more than 20.")
else:
    print("Student cannot enroll. Age is less than 10.")