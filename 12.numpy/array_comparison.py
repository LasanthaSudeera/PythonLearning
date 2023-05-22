from numpy import *

a1 = array([1, 2, 3, 4, 500])
a2 = array([10, 20, 30, 40, 50])

# compare array
print(a1 > a2)
print(a1 < a2)

# check atleast one element is greater
print(any(a1 > a2))

# compare all elements
print(all(a1 > a2))

# check if multiple conditions are passed
print(logical_and(a2 > 5, a2 < 100))

# apply where to get only the condition matching elements
print(where(a1 < 100, a1, 0))