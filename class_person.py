class Person:
    name = "Leo"
    occupation = "software developer"
    networth = 10
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
# print(a.name, "is a", a.occupation)
# a.name = "Rocky"
# a.occupation = "feline full time bro"
# print(a.name, "is a", a.occupation)


a.info()
a.name = "Rocky"
a.occupation = "Feline partner"
a.info()