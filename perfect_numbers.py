sum = 0
i=0

n = int(input("Enter a number: "))

for i in range(1, n):
    if n % i == 0:
        sum = sum+i

if n==sum:
    print("PERFECT NUMBER")

else:
    print("NOT A PERFECT NUMBER")
