from numpy import *

# creating an array from numpy

# optionaly you can specify the datatype of the array
numbs = array([1, 2, 3, 4, 5])
numbs = array([1, 2, 3, 4, 5], int)  # Optional

chrs = array(['a', 'b', 'c', 'd', 'e'])
chrs = array(['a', 'b', 'c', 'd', 'e'], str)  # optional
print(numbs)
print(chrs)

# line space, can be used to divide a range of number that is evenly spaced.
print(linspace(0, 100))

#logpsace returns numbers spaced evenly on a log scale.
print(logspace(1,100))

#array range, similar to range but generates an array
print(arange(1,20))

# generate a array full of ones
print(ones(10))

# generate a array full of zeros
print(zeros(10))