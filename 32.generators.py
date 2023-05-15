# Custom generator similar to range
def customgen(x,y):
    while x<=y:
        yield x
        x+=1

# For loop using the customgen Generator
for i in customgen(1,10):
    print(i)

"""
In this custom generator the last value is also looped unlike range()
"""
