class Person:
    name = "Leo"
    occupation = "software developer"
    
    # Self means that object for which this method is called
    def info(self):
        print(f"{self.name} is a {self.occupation}")


# a is a object
a = Person()
# a.info() 
a.name = "Rocky"
a.occupation = "Feline partner"
a.info()

# b is another object
b = Person()
b.name = "Chand"
b.occupation = "Lawyer"
b.info()
