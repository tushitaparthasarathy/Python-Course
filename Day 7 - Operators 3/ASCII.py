print("ASCII Value Checker")
print("="*40)
char=input("Enter a single charcter: ")
if type(char) is str and len(char)==1:
    ascii_val=ord(char)
    print("Character :", char)
    print("ASCII Value:" , ascii_val)
    print("Character type: " , end="")
    if ascii_val>=65 and ascii_val<=90:
       print("Type: Uppercase")
    elif ascii_val>=97 and ascii_val<=122:
       print("Type: Lowercase")
    elif ascii_val>=48 and ascii_val<=57:
       print("Type: Digit")
    elif ascii_val ==32:
       print("Type: Space")
    else:
        print("Special Character")
else:
    print("Error: Please enter exactly ONE character")




 