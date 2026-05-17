print("Enter Marks Obtained in 5 Subjects:")

markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne + markTwo + markThree + markFour + markFive
avg = int(tot / 5)

validRange = range(0, 101)

if avg not in validRange:
    print("Invalid Input!")

elif avg in range(91, 101):
    print("Your Grade is A1")

elif avg in range(81, 91):
    print("Your Grade is A2")

elif avg in range(71, 81):
    print("Your Grade is B1")

elif avg in range(61, 71):
    print("Your Grade is B2")
    print("Your Grade is E2")