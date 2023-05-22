from numpy import *

a1 = arange(1, 10)
# Shallow copy
a2 = a1.view()

print('a1', a1)
print('a2', a2)

a2[3] = 40

print("After modification")
print('a1', a1)
print('a2', a2)

# hard copy
a3 = a1.copy()

print('a1', a1)
print('a2', a3)

a3[3] = 40

print("After modification")
print('a1', a1)
print('a3', a3)

# slicing
print(a3[2:5])

# slicing with steps (2 steps)
print(a3[0:9:2])