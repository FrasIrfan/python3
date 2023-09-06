n = int(input("Enter a number to print the table for: "))

input = int(input("Enter 1 to print table upto 10 \nEnter 2 to print table upto 20  : "))

if input == 1:
    for i in range(1,11):
        print(f"{n} x {i} = {n * i}")
elif input == 2:
    for i in range(1,21):
        print(f"{n} x {i} = {n * i}")
else:
    print("Incorrect input")



