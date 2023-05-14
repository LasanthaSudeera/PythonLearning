# Bytes and ByteArray
"""
No slicing or repetition is allowed in bytes or bytearray
"""

lst = [12,25,40, 234] # max 255 as lmited by bytes
b = bytes(lst)
print(b)
print(type(b))

# To modify an index, bytes can be coverted to a bytes array
ba = bytearray(b)
print(ba)
print(type(ba))

# Modify the index of bytes array
ba[0] = 14