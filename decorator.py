def greet(func):
    def wrapper():
        print("Hey there, Fras!")
        func()
        print("Thank you for running this code")
    return wrapper

@greet
def hello():
    print("Hello world")

hello()
