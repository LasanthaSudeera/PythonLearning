# Tuple
"""
A tuple is similar to a list but immutable, it maintains insertion order, allows duplicated, if the
tuple has a single element is should be ended with a ,
example t1 = (1,2,3)
brackets are optional but recommended for clarity
tuple with a single element
t2 = 1, <= ended with a comma

* A tuple can be used as a key to a dictionary
"""

tpl1 = (1,2,3,10,5,6,7,10, "John Doe", "Jane Doe")
print(type(tpl1))
print(tpl1)

# Repitition in tuple is similar to list
print(tpl1*3)

# Get the number of times the element has occured
print(tpl1.count(10)) # returns 2 as it's repeated 2 times

# Get the index of an element
print(tpl1.index('John Doe')) # returns 8 as 'John Doe' is in the 8th index

# Slicing works similar to lists
print(tpl1[2:5])

# Converting a list to a tuple
lst = [1,3,5, 'TXT']
print(type(lst)) 
print(lst) # retuns the list
tpl2 = tuple(lst);
print(tpl2) # returns the list converted to a tuple
print(type(tpl2))