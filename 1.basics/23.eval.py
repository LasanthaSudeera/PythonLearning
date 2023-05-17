# Using eval we will get a list from the user
lst = eval(input("Enter a list of elements: "))
# lst2 =[]
# for i in lst:
#     if i not in lst2:
#         lst2.append(i)                          # <- This logic can be replaced by set() as Set avoid duplicates
#     else:
#         continue
lst2 = set(lst)
print("Your unique list is: ",lst2)