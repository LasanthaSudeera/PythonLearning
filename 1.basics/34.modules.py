from math import *
import math

print(sqrt(2))
print(ceil(7.2))
print(floor(8.9))
print(fabs(-5.0)) # Returns the absolute values, removes plus or minus. iabs() is used for integer values

# To get all the methods available in the module, dir() can be used dir() or dir(module)

print(dir(math)) # Methods available in the math module
print(dir()) # All methods available in the current module with all imports including

# help() can be used to get a detailed info on the module
"""uncomment this to see the help()"""
# help(math) 

# Print a random number between 0 and 1 with random module
from random import *
print(random())

# Get a random number between a given range
print(randint(1,100))

# Get floating point random number between a given range
print(uniform(1,10))

# Get a random value from a list
lst = ['Apple', 'Orange', 'Mango', 'Banana']
print(choice(lst))
print("My favourite fruit is {}".format(choice(lst)))