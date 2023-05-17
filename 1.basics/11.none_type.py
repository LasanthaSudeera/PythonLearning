# None type similar to NULL in php

# This function does not return anything
def noneReturnFunction():
    a = 10

# Invoking the above function will return None as it returns noting
print(noneReturnFunction())

# Creating a function with optional Params
def optionalParamsFunction(name = None):
    return name

# Invoking about function without the params
print(optionalParamsFunction())
# Invoking the same function with params
print(optionalParamsFunction("Lasan"))

