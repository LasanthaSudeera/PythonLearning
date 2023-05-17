try:
    num = int(input("Enter an even number: "))
    assert num%2==0, "You have entered a invalid number"
    print("You entered an even number")
except AssertionError as obj:
    print(obj)

print("After assertion")