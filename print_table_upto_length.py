n = int(input("Enter a number to print the table for: "))

length = int(input("Enter length to print table upto: "))

for i in range(1,length+1):
    print(f"{n} x {i} = {n * i}")


