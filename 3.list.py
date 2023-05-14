# List type
lst = [1,2,3, "John Doe"]
print(type(lst))
print(lst)

# Get an element from the list
print(lst[3]) # return 'John Doe' as it's index is 3

# Get everthing from starting X to end index X
print(lst[2:4]) # returns [3, 'John Doe'] as it starts from 2 and the last index is ignored

# Repitition
print(lst*3) # Returns the same list 3 times as a single list

# Get the lenght of a list
print(len(lst)) # returns 4 as the list has only 4 elements

# Adding a new element to the list
lst.append("Jane Doe")
print(lst) # returns [1, 2, 3, 'John Doe', 'Jane Doe'] as not 'Jane Doe' new element is added

# Remove and element
lst.remove(3)
print(lst) # returns [1, 2, 'John Doe', 'Jane Doe'] as now '3' is removed first occurence

# Remove using the index
del(lst[0]) # del() is an inbuilt function not a list function
print(lst) # returns [2, 'John Doe', 'Jane Doe'] as '1' is removed, as it was in the 0 index

# Remove all elements from the list
lst.clear()
print(lst) # returns [] as all the elements are removed

lst = [1,2,3]

# Get the max element ONLY INT lists are supported
print(max(lst)) # max() is a built in function, returns 3 as it's the max

# Get the min element ONLY INT lists are supported
print(min(lst)) # min() is a bilt in function, returns 1 as it's the min

# Insert a new element in a particluar index
lst.insert(2, 10)
print(lst) # [1, 2, 10, 3] as 10 was inserted in the 2nd index

# Sort the list
lst.sort()
print(lst) # Sorted asc order [1, 2, 3, 10]

# Sort DSEC order
lst.sort(reverse=True)
print(lst) # Sorted desc order [10, 3, 2, 1]