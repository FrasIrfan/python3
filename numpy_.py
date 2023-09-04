import numpy as np
my_array = np.array([0,10,20,30,40,50,60])
print(my_array)
print(type(my_array))
print(my_array[0])
print(my_array[1])
print(my_array.dtype)

# multidimensional array

multi_array = np.array([[0,10,20],[30,40,50]])
print(multi_array)
print(multi_array[1,2]) #1st row 2nd column
print(multi_array.shape) #2 rows 3 columns
print(multi_array < 20)
print(multi_array[multi_array < 20])