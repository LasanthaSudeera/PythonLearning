# Map list Usecase

# Example
students = {
    'john': ['Python', 'Java'],
    'jane' : ['MetaTrader 5 Basics', 'c#']
}

for studentKey in students.keys():
    print("The courses " + studentKey.title() + " enrolled are: ")
    for course in students[studentKey]:
        print("* " + course)

# Exercise
countries = ["LK", "AUS", "USA"]
countries.remove("AUS")
countries.insert(1, "UK")
print(countries)