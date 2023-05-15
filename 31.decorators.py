# A decorator function is a function that returns a function, and the same time add a special meaning to the output.

# Decorator function, returns a function
def decor(func):
    def innerFunc():
        result = func()
        return result*2
    return innerFunc

def decoratingFunction():
    return 5

result =decor(decoratingFunction)
print(result())

# Automatically adding a decorator to a function using @
@decor
def autoDecoraterFunc():
    return 10

print(autoDecoraterFunc())

# Exercise Hello name, How are you decorator
def stringDecor(func):
    def innerFunc(n):
        string = func(n)
        string += ", How are you?"
        return string
    return innerFunc

@stringDecor
def helloNameFunction(name):
    return "Hello {}".format(str(name).title())

print(helloNameFunction("lasan"))

# Decorator chaining
def half(func):
    def inner():
        result = func() /2
        return result
    return inner

def intoTen(func):
    def inner():
        result = func() * 10
        return result
    return inner

@half # 10 becomes 5
@half # 5 becomes 2.5
@intoTen # 2.5 x 10  is 25.0
def num():
    return 10

print(num())