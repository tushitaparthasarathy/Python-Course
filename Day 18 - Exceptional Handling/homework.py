try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Invalid age.")
    elif age % 2 == 0:
        print("The entered age is Even.")
    else:
        print("The entered age is Odd.")

except ValueError:
    print("ValueError: Please enter a valid integer age only.")