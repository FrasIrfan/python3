person = {
    'name': 'Fras',
    'age': 19,
    'hobbies': ['programming', 'playing football', 'gaming']
}

print(person)
print(type (person))
print(person.get('age'))

# getting all keys using the dict_keys function
allKeys = person.keys()
print(allKeys)
for x in allKeys:
    print(x)

# getting all values using the value function
allValues = person.values()
print(allValues)
for x in allValues:
    print(x)

# Accesing individual values using keys
print(person['name'])
print(person['age'])

# Adding a new value pair
person ['gender'] = 'Male'
print(person['gender'])

# Modifying a value
person ['age'] = 20
print(person['age'])

# Removing a key
del person ['hobbies']
# print(person['hobbies']) #will show error

# Checking if a key exists
if 'name' in person:
    print("Name KEY exists in person")

# Iterating over keys
for key in person:
    print(key, ':', person[key])
# the loop variable (key) takes on each key of the dictionary
#in each iteration.

# Iterating over values
for key, value in person.items():
    print(key, ':', value)
# using the items() method of the dictionary. 
# This method returns a sequence of key-value pairs as tuples.
# The loop then iterates over these tuples, and in each iteration,
# the variables key and value are assigned the values of the 
# current tuple's elements (key and value, respectively).