class MyClass:
    def __init__(self, initial_value):
        self._value = initial_value
    
    def show_value(self):
        print(f"Value is {self._value}")

#Getter
    @property
    def ten_value(self):
        return 10* self._value 
    
    @ten_value.setter
    def ten_value(self,new_value):
        self._value = new_value/10

obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show_value()
