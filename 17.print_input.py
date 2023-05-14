# Using a custom seperator, default is blank
print(10, 20) # Without seperator
print(10,20, sep="--") # returns 10--20 as the new custom seperator is --
print(10,20, sep="\n") # returns in two new lines, as now the seperator is a newline character

# Using place holders
"""
    %i for integer type data
    %s for string type data
    %f for floating point data
"""
name = "Lasantha"
age = 29
marks = 89.90
print("Your name is %s and your age is %i and your marks are %f" %(name, age, marks))

# Restricting the float to just 2 decimal places
print("Your name is %s and your age is %i and your marks are %.2f" %(name, age, marks))
"""
                                                                ^ is used to define the decimal places here limited to 2
"""

# Using brazes to format the string
print("Your name is {} and your age is {} and your marks are {}".format(name,age,marks))

# Using index
print("Your name is {0} and your marks are {2} and your age is {1}".format(name,age,marks))

# Getting multiple inputs, and saving to the list, the result of the for loop is stored in x and type casted to int
lst = [ int(x) for x in input("Enter 3 numbers seperated by space: ").split()]
print(lst)

# Sample exercise Sandwitches shops
sandwitchPrice = 5;
print("Topping we have are: ")
toppings = {
    1: "Tomato",
    2: "Cheese",
    3: "Peppers",
    4: "Onions",
    5: "Olives",
}
for topping in toppings.keys():
    print("Select {} for {}".format(topping, toppings[topping]))
selectedToppings = [int(x) for x in input("Enter your topping number seperated with space: ").split()]
if len(selectedToppings) > 3:
    print("Maximum numbers of topping allowed is 3.")
else:  
    for i in selectedToppings:
        if not i in toppings:
            print("Invalid topping selected.")
            quit()
    print("Your selected toppings are: ")
    for i in selectedToppings:
        print("** {} **".format(toppings[i]))
    numSandwitches = int(input("Enter the number of sandwitches: "))
    price = numSandwitches * sandwitchPrice
    print("Your total is $" + str(price))
    print("Thank you for your purchase!")
    quit()