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