# function to calculate the average of the two numbers
def simpleAvgCal(numOne, numTwo):
    return (numOne + numTwo) / 2

# Invoking the function
print(simpleAvgCal(10, 20))

# Invoking as named params, the order of the params does not matter
print(simpleAvgCal(numTwo=10, numOne=20))

# Retuning multiple values
def returnMultipleValues():
    a = 50
    b = 20
    c = a + b
    return a,b,c

print(returnMultipleValues())

# Sample global variable
x = "This is a global variable X"

# Sample function with a local variable
def testFucntion():
    y = "This is a local variable Y"
    print(x)
    print(y)

# Sample function that overwrites the global variable locally
def overWritingGlobalVariables():
    x = "Overwriiten X"
    print(x)

# Here even if the global variable is overwritten, with globals() we can refer the orignal value
def getOriginalGlobalEvenAfterOverride():
    x = "Overwriiten X"
    print(globals()['x'])



testFucntion()
overWritingGlobalVariables()
getOriginalGlobalEvenAfterOverride()
print(x)

# A function can be assigned to a variable and invoked
z = testFucntion # the testFunction() is not assigned to the z variable
z()

# Fuction inside a function
def helloWorld():
    hello = "Hello"
    def world():
        return " World"
    return hello + world()

print(helloWorld())

# Invoke another function, by acceping a function as a param
def invokeOtherFunc(func):
    return func

print(invokeOtherFunc(helloWorld()))

# Returning functions
def returnFunction():
    def returnFunction():
        return "Retuned function"
    return returnFunction

returnedFunction = returnFunction()
print(returnedFunction())

# Recursion
def factorial(number):
    if number == 0:
        return 1
    else:
        return number*factorial(number-1)
    
print(factorial(3))
print(factorial(5))

# Default arguments
def defaultArgs(name="Default name"):
    return name

print(defaultArgs())

# Optional arguments
# *args using *args as a param, this helps to pass inifinte optional params
def argsFunction(required, *args):
    print(required)
    print(args)

argsFunction("ok")
argsFunction("ok", 1,2,3,4)

# **kwargs using **kwargs as a param, this helps to pass infinite optional keyword params
def kwargsFunction(**kwargs):
    print(kwargs)

kwargsFunction(name="Test", age=23)

"""
    Important note *args and **kwargs can be anything, but the astrixs matter
    example *somevariable is equal to *args
            **somevariable is equal to **kwargs
"""

# Passing optioanl args to another function
def optionalArgsFunction(*args, **kwargs):
    optionalArgsFunctionTwo(*args, **kwargs)

def optionalArgsFunctionTwo(*args, **kwargs):
    print(args)
    print(kwargs)

optionalArgsFunctionTwo(12,34,56,name="Test")