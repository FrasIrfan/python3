class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Leo",19)
person2 = Person("Rocky",2)

print(person1.name)
print(person1.age)
print(f"My name is {person1.name} and I'm {person1.age} years old.")

# print(person2.name)
# print(person2.age)