class Cat:
    def __init__(self, name):  # Constructor to initialize 'name'
        self.name = name

    def meow(self):
        print(f"{self.name} says Meow!")

my_cat = Cat("Rocky")  # Creating a Cat object and passing the name "Rocky"
print(my_cat.name)     # Accessing the 'name' attribute
my_cat.meow()          # Calling the 'meow' method
