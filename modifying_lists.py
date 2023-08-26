fruits = ["Apple , mango , banana , orange"]
print(fruits)
#adding another element to the list
fruits.append("Guava")
print(fruits)
#adding a element on a different position
fruits.insert(0,"Pineapple") 
#index starts from 0, so index of Pineapple is one less than that of
print(fruits)
#assigning something else to the position
fruits[0] ="Updated value" #assigning value at particular index
print(fruits)

fruits[1] ="Updated value" #assigning value at particular index
print(fruits)

fruits[2] ="Updated value" #assigning value at particular index
print(fruits)
