class India:
    def capital(self):
        print("Capital: New Delhi")
    def language(self):
        print("Language: Hindi")
    def type(self):
        print("Type: Democratic Country")
class USA:
    def capital(self):
        print("Capital: Washington")
    def language(self):
        print("Language: English")
    def type(self):
        print("Type: Developed Country")
obj_ind=India()
obj_usa=USA()
for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()