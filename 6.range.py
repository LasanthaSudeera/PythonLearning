# Range type

rng = range(6) # always starts from 0
print(type(rng))
print(rng)
print(len(rng)) # returns 6, as it has 0-5 elements

# Use a for loop to loop though the range
for i in rng:
    print(str(i) + " element")

# Create a new range with custom start
rng2 = range(2,5)
print(len(rng2)) # returns 3 as it starts with 2 and end with 4, as it excluded the max value we provide
for i in rng2:
    print(str(i) + " element")

# Run range in steps
rng3 = range(1,15, 3)
print(len(rng3)) # returns 5 total elements as it skips every 3rd value
for i in rng3:
    print(str(i) + " element")