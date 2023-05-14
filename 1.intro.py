# Single Line Comment
firstName = str(input("Please enter your first name: "))
lastName = str(input("Please enter your last name: "))
age = int(input("Please enter you age: "))
ssn = str(input("Please enter your social security number: "))
height = float(input("Please enter your height (CM): "))
weight = float(input("Please enter your weight (Kg): "))

""" Multi line comment
can be used as DOC Blocks
"""
print(
    "First Name: " + firstName,
    "Last Name: " + lastName,
    "Age: " + str(age),
    "Social Security Number: " + str(ssn),
    "Height: " + str(height) + "cm",
    "Weight: " + str(weight) + "kg",
)