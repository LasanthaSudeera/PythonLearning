lst = []
"""for x in range(1,11):
    lst.append(x**3)                    <= Same logic can be used to generate a list with list comprehension
print(lst)
"""

lst = [x**3 for x in range(1,11)]
print(lst)

# Example create a list with all the even nunbers between 1 and 20
evenLst = [x for x in range(1,21) if x%2 == 0]
print(evenLst)

# Example multiple 2 lists
a = [1,2,3,4,5]
b = [6,7,8,9,10]

result = [a[x] * b[x] for x in range(len(a))]
print(result)

# Example get the duplicated values
d = [1,2,3,4]
e = [2,4,6,8]

duplicated = [ i for i in d if i in e]
print(duplicated)