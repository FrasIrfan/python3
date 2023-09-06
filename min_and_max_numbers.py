max = -9999999  
min = 9999999   

for i in range(1, 6):
    n = int(input(f"Enter {i}st number: "))
    
    if n > max:
        max = n
    if n < min:
        min = n

print("Max number is", max)
print("Min number is", min)
