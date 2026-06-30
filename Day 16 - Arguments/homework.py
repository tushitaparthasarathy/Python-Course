def shutdown():
    choice = input("Do you want to shut down? (Yes/No): ")

    if choice == "Yes":
        print("Shutting down")
    elif choice == "No":
        print("Abort shut down")
    else:
        print("Sorry.")
shutdown()