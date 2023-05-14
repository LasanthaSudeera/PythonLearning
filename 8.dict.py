# Dictionary
"""
A dict is used to have key value pairs
    key: value
"""

dict1 = {
    'name': "John",
    'age': 29
}

print(type(dict1))
print(dict1)

# Get all the items
print(dict1.items())

# Items are loopable
for i in dict1.items():
    print(i)

# Get all the keys
print(dict1.keys())

# Keys are loopable
for i in dict1.keys():
    print(i)

# Get the single value using a key
print('Name is ' + dict1['name'])

# Delete an element using the key
del dict1['age']
print(dict1)