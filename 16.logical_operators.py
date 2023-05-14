# When using logical operators, we use them against boolean values

x = 20
y = 30

print(x == 20 and y ==30 ) # returns True as the condition is true
print(x == 25 and y ==30 ) # returns False as the condition is false
print(x == 25 or y ==30 ) # returns True as y ==30 is True
print(not(x == 25 or y ==30 )) # returns False as y ==30 is True and the opposite is False
