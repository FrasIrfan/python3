x = ["My , name , is , Fras"]
print(type(x)) #prints the data type which is used
print (x) #prints the list
print (len(x))
#Here the length of the string will be 1 
#as the list is a single string element


#using split method to obtain the list of 4 elements
print("\nusing split method")
split_elements = x[0].split(", ")  # Splitting the string into separate elements
# split method on this string with ", " as the delimiter. 
# This means that the string will be split wherever the sequence ", " occurs
print(split_elements)  # Output: ['My', 'name', 'is', 'Fras']
print(len(split_elements))  # Output: 4, since there are four separate elements now



