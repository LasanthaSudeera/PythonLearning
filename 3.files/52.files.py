"""
To open a file we use open() in python
There are 7 modes
    1. write (w) -> deletes all the content from begining to end and write the context
    2. read (r) -> open the file from begining to end
    3. append (a) -> add some context to already existing file with context to the end
    4. read & write (w+) Can both read and write
    5. read, write & append (r+)
    6. appending and reading (a+)
    7. exlusice mode (x), if a file does not exists a new file will be created, but in case if the file exists
        an error will be thrown

    For normal text files all above modes will work, but if you are working with binary files "b" should be appended for the modes
        example:
            wb rb r+b

    f = open("filename", "mode", "buffer")

    buffer has two possible values 4096 or 8092, this can be left empty

    after we are done, f.close() can be invoked
"""

# Write to a file
f = open("learning.txt", "w")
f.writelines([
    "Hello World\n",
    "This is awesome"
])
f.close()

# Write from input
f = open("learning.txt", "w")
text = input("Input some text to save: ")
f.write(text)
f.close()

# Read a file
f = open("learning.txt", "r")
print(f.read())
f.close()

# Simple notepad
f = open("learning.txt", "w")
print("Text your text. To save press enter and in a new line :s and press enter.\n")
s = ""
while s != ":s":
    s = input()
    f.write(s + "\n") # Everytime we press enter, it will create the spacing
f.close()

# Check if the file exists
import os, sys
if os.path.isfile("learning.txt"):
    print("File Exists")

if os.path.isfile("learnings.txt"):
    print("File Exists")
else:
    print("Doesn't exists")