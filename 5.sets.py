# Set
"""
Does not allow duplicates
a set is defined as below
 s = { 12, 3, "TXT" }

 Cannot perform indexing, repitition or slicing
"""

set1 = {12, 3, "TXT"}
print(type(set1))
print(set1)

# If the set has duplicates, it will omit it
set2 = {12, 3, "TXT", 12, "TXT"}
print(set2) # returns {3, 12, 'TXT'} as the duplicates are omitted

# Perform an update operation or add new elements to set, can have any number of elements in the square brackets
set1.update(["Updated Element"])
print(set1) # return {3, 12, 'Updated Variable', 'TXT'} with the new 'Updated Element'

# Remove an element
set1.remove("TXT")
print(set1) # returns {3, 12, 'Updated Element'} as TXT is removed

set2.remove("TXT")
print(set2) # returns {3, 12} as TXT is removed

# Frozen Set, once you convert to a forzen set, you cannot do update or remove operations
fset = frozenset(set1)
print(type(fset))
print(fset)