print("\n")
print("Multiples of 7 uisng the list comprehension")
multiples = [x*7 for x in range(1,11)]
print(multiples)
#lists comprehensions let us create new lists based on sequences or ranges

print("\n")
print("Calculating lengths of elements")
languages = ['c++','python','Java','Ruby']
length = [ len(language) for language in languages ] 
print (length)


print ("\n")
print("All the numbers between 0 and 100 that are divisible by 3")
z= [x for x in range(0,101) if x % 3 == 0]
print(z)