# Lamdas are anonymous functions, lambdas will always return a function, which should be invoked to get a result back

# Simple lambda function to get the square 
f = lambda x: x *x
print(f(10))

a = lambda a,b: a*b
print(a(2,3))

# Lambda to check if the number is EVEN
even = lambda num: 'YES' if num%2 == 0 else 'NO'
print(even(2))

# Lambda with filter()
numList = [1,2,3,4,5,6,7,8,9,10]
filteredList = list(filter(lambda x: x%2 == 0, numList))
print(filteredList)

# Lambda with map()
multipliedList = list(map(lambda x: x*10, numList))
print(multipliedList)

# Lambda with reduce()
from functools import reduce
total = int(reduce(lambda x,y: x+y, numList))
print(total)