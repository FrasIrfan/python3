n = int(input("Please Enter a number: "))
i = 2
is_prime = True

while i < n:
    if n % i == 0:
        is_prime = False
    i += 1

if is_prime:
    print("Number is Prime")
else:
    print("Number is not prime")