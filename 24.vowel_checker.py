vowels = {
    "a",
    "e",
    "i",
    "o",
    "u"
}
word = input("Enter a word to check the number of vowels: ")
results = {}
for c in word:
    if c in vowels:
        results[c] = results.get(c, 0) + 1
for k,v in results.items():
    print(k, "is present ", v, "times")