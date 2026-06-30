def shutdown(condition):
    condition=input("Do you want to shutdown")
    return condition
    if condition=="yes":
        print("Shutting down")
    elif condition=="no":
        print("Abort shutdown")
    else:
        print("sorry")
