class IOString:
    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("Enter a string: ")

    def print_string(self):
        print("Result is:", self.str1.upper())

str = IOString()
str.get_string()
str.print_string()