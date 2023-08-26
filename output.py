# example no 1
def product(a, b):
        return(a*b)

print(product(product(2,4), product(3,5)))
# a. The first inner call (product(2, 4)) resulted in 8.
# b. The second inner call (product(3, 5)) resulted in 15.
# c. Therefore, the outer product call becomes product(8, 15), 
# which calculates the product of 8 and 15, resulting in 120.

# example no 2
def difference(a, b):
        return(a-b)

def sum(a, b):
        return(a+b)

print(difference(sum(2,2), sum(3,3)))

# Example 3
# Evaluate the Boolean output of this comparison


print((5 >= 2*4) and (5 <= 4*3))

# Example 4 
# Evaluate the value of the comparison in the if statement 


x = 3
if x+5 > x**2 or x % 4 != 0:
        print("This comparison is True")
        
        # Example 5 
# Evaluate the output of this if-elif-else statement


number = 6
if number * 2 < 14:
        print(number * 6 % 3)
elif number > 7:
        print(100 / number)
else:
        print(7 - number)
        

def get_remainder(x, y):
 
  if x == 0 or y == 0 or x ==y:
    remainder = 0
  else:
    remainder = (x % y) / y
  return remainder


print(get_remainder(10, 3))


def greater_value(x,y):
    if x > y:
        return x
    else:
        return y
    
print(greater_value(10,3*5))


