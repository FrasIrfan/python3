for x in range(10):  
    print (x)
    
product = 1
# Initialize product to be one.
for n in range(1,10):
    product = product * n
    print(product)

for left in range (7):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()



for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop") 