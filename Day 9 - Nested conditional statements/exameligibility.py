medical=input("Do you have medical cause? (Y/N)")
if medical=="Y":
    print("You are allowed")
else:
    attendance=int(input("Enter the attendence of student :"))
    if attendance>=75:
        print("You are allowed")
    else:
        ("You are not allowed") 