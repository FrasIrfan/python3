# Stack: First come last serve

# empty stack
stack = []

while True :
    i = input("Enter 1 to push \nEnter 2 to pop \nEnter 0 to exit \nEnter number: ")

    if i == "0":
        break
    
    elif i == "1":
        name = input("Enter item to push: ")
        stack.append(name)
        print (stack)
        
    elif i == "2":
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Popped item is", stack.pop())
            print (stack)

    else: 
        print("Invalid input")