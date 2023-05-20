"""
 module re is used for regex

 Sequence characters
 -------------------
 -------------------

\d for digits
\D any non digit character
\s whitespace
\S non whitespace
\w for any alphanumerica character
\W non alphanumeric character
\b space around words
\A do a search only at the start of the string
\Z only matches the end of the string
"""

import re

# A regex to return text as a match
string = "This text is a sample simple text, textz"
result = re.search(r't\w\w\w', string) # Here the expression is start with 't' with any character replace the 3 www, so the match is text
print(result.group())

# Find all, starts with t with any character replace the 3 www, so the match is text
result = re.findall(r't\w\w\w', string)
print(result)

# match() only search at the begining of the string
result = re.match(r't\w\w\w', string)
print(result)

# split() will split the string based on a match
string2 = "This text 4 is a sample 4 simple text"
# split wherever there is a digit
result = re.split(r'\d+', string2)
print(result)

# replace a string with a new string with sub()
result = re.sub(r"t\w\w\w", 'string', string)
print(result)

# Quantifiers
"""
    Quantifiers can be used to match one for more characters
    + one or more repitions of the match example \d+ one or matching digits
    * zero or more of the expression
    ? zero or one of the expression
    {m} exatcly the 'm' number of occurences
    {m,n} minnimum number of occurences, n maximum number of occurences


"""

# One or more of the repitition 
result = re.findall(r't\w+', string)
print(result)

# Zero or more of the repitition 
result = re.findall(r't\w*', string)
print(result)

# Zero or one of the repitition 
result = re.findall(r't\w?', string)
print(result)

# Extact number of following character, in this example 1
result = re.findall(r't\w{2}', string)
print(result)

# min and max number of following character, in this example 1
result = re.findall(r't\w{1,3}', string)
print(result)

# Get the dates from a string
string3 = "Today is 20-05-2023, and tomorrow is 21-05-2023, and short had is 21-05-23"
result = re.findall(r'\d{1,2}-\d{1,2}-\d{2,3}', string3)
print(result)

# Special characters
"""
    \ escape character if you wanr to use the backward slash
    . anycharacter except a new line
    ^ match the regex at the begining of the string
    $ match the regec at the end of the string
    [...] match the range of values
    [^...] match anything but what's inside the square bracket
    (...) can give a regex to match
    (R | S) can define multiple regex, R and S are example regex placements

"""

# should occur at the behgining of the srting
result = re.search(r'^t\w\w\w', string)
print(result) # returns none as the expression cannot be matched at the begining


