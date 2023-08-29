def check_prime_number(n):
        i = 2
        is_prime = True

        while i < n:
            if n % i == 0:
                is_prime = False
                break
            i += 1
            return is_prime
            
n = int(input("Please Enter a number: "))

prime = check_prime_number(n)
if prime:
    print("Number is Prime")
else:
    print("Number is not prime")