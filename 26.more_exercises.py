# Join uses the given string as a delimter to join with the defined list
s = "-".join([
    'a',
    'b',
    'c'
])
print(s)

# Reverse a string using join
name = input("Enter a word to reverse: ")
print("".join(reversed(name)))

# Reverse a sentence
sentence = "All the power is within you"
temp = sentence.split()
result = []

i = len(temp) - 1
while i >= 0:
    result.append(temp[i])
    i -= 1
print(sentence)
print(" ".join(result))

# Reverse the characters of the word
newSentence = "Python is an awesome language"
temp2 = newSentence.split()
result2 = []

for i in range(len(temp2)):
    tempString = str(temp2[i])[::-1]
    result2.append(tempString)

print(newSentence)
print(" ".join(result2))

# Remove duplicate characters of a given string method one
duplicateString = "aaaaaaaaaaaavvvvvvvvvvvvvvvrtyuiooooooooooopppppp"
duplicateStringList = []
for i in duplicateString:
    duplicateStringList.append(i)
print(set(duplicateStringList))

# Remove duplicate characters of a given string method two
duplicateStringList2 = []
for i in duplicateStringList:
    if i not in duplicateStringList2:
        duplicateStringList2.append(i)
print(duplicateStringList2)

# Count the number of unique characters in a string
result3 = {}
for i in duplicateString:
    result3[i] = result3.get(i, 0) + 1
for key, value in result3.items():
    print("{} is repeated {} times.". format(key, value))
print("Unique letters are:")
for k in result3.keys():
    print("-> {}".format(k))

# Print a right angled trainangle
numberOfLines = int(input("Number of lines for the traingles: "))
for i in range(numberOfLines +1):
    print(" *"*i)
print('\n')

#Print a pyramid pattern for the given number of lines
for wi in range(1, numberOfLines+1):
    print(" "*(numberOfLines -wi), end="")
    print("* "*wi)

# Print all the occurences index for the word 'idea'
string = "Take up one idea and make that idea your life. Think and dream of that idea \
and leave every other idea alone"
subString = "idea"
found = False
pos = -1
length = len(string)
while True:
    pos = string.find(subString, pos+1, length)
    if pos == -1:
        break
    print("Found substring at position ", pos)
    found = True
if found == False:
    print("Substring not found!")