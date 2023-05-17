#Immutable

a=10
b=10
print(a is b) # Since we are declaring two variables with same value, the memory is shared and both are pointed to the same location
print(id(a))
print(id(b))

# If we change the varaible to a diffrent value, a new memory location is allocated
b=14
print(a is b)
print(id(a))
print(id(b))

# Same behaviour in string and all basic types