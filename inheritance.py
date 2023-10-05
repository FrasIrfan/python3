# Employee class
class Employee:
    def __init__(self, employee_name, employee_id):
        # Initialize employee name and ID
        self.name = employee_name
        self.id = employee_id

    def show_details(self):
        # Display employee details
        print(f"The name of Employee {self.id} is {self.name}")

# Programmer class, which inherits from Employee
class Programmer(Employee):
    def showLanguage(self):
        # Display the default programming language for programmers
        print("The default language is Python")

# Create an instance of the Employee class
employee1 = Employee("Jawad", 1)
employee1.show_details()  

# Create an instance of the Programmer class
employee2 = Programmer("Chand", 2)
employee2.show_details()  
employee2.showLanguage()  
