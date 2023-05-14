# Simple string
s = "This is a simple statement"

# Multi like String
sm = """ This is a multiline
string"""

# Get the length of a container
print(len(sm))

# Get an element of a container *2nd Char of s
print(s[1])

# String slicing *Get only 'This' from s
print(s[0:4]) # Does not include the element in the ending index

# To get the entire string, the ending index can be undefined
print(s[0:]) # This returns the entire string stored in the s container

# If the starting index is not provided, it starts from the very begining
print(s[:4]) # Returns 'this' as it still starts from 0

# Using minus numbers important to know -1 always represent the last element
print(s[-17:-10]) # Returns 'simple' as it start from -17 to -10, last slice element is not included as always

# Using steps, default is one, if the step is set to 2 it will select 1,3,5 etc
print(s[0:4:2]) # Only returns 'Ti' as it skips every 2nd element
print(s[::2]) # returns 'Ti sasml ttmn' as it skips every 2nd element

# Reversing the string
print(s[::-1])

#Palindrome checker using the reserve string
car = "Race Car"
car = car.replace(" ", "").lower() # remove space and convert to lower case return is 'racecar'
print(car) # Print the lowecase without space
print(car[::-1]) # Print the lowecase without space reversed string
if car == car[::-1]:
    print(car +' is a palindrome')
else:
    print(car +' is not a palindrome')

notCleanString = "              Has many unneccessary spaces before and after        "
print(notCleanString)
print('Before strip ' + str(len(notCleanString)))
cleanString = notCleanString.strip() # Removes the unncessary spaces from start and end
print('After strip ' + str(len(cleanString)))

# Remove only leading white spaces
print(notCleanString.lstrip())
# Remove only ending white spaces
print(notCleanString.rstrip())

# Get the index of a matching string using find
print(s.find("ple")) # returns 13 as the 'ple' match starts at 13th place

# Find can be given a place to start and end
print(s.find("ple", 0, 5)) # retutns -1 as it does not exists in 0 to 5 index
print(s.find("ple", 10, len(s))) # returns 13 as it exists in 13h ndex, but only looks in 10 to 26 index

# Find the count of occurences
print(s.count("is")) # returns 2 as 'is' is fount in 'This' and 'is'

# Replace old values with new value
print(s.replace('a', 'A')) # returns 'This is A simple stAtement' 'a' is replced by 'A'
print(s.replace('simple', 'correct')) # returns 'This is a correct statement' 'simple' is replced by 'correct'

# All lowercase
print(s.lower())

# All uppercase
print(s.upper())

# Title case
print(s.title()) # Every word starting letter is upper

# String formating
replacer = "Okay"
print(f"This is a string {replacer}")