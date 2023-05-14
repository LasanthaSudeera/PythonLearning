# IF statements
if True == True:
    print("Its' definetly true")

# Else If
if True == False:
    print("Will never come here")
elif True == True:
    print("Its true")
else:
    print("Will never come here")

# Odd Even checker
print("Is your number ODD or EVEN? Want to find out?")
number = int(input("Enter a number: "))
if number == 0:
    print("Enter a number more than ZERO, cause ZERO IS ZERO")
elif number % 2 == 0:
    print("Your number is EVEN")
else:
    print("Your number is ODD")

# Exam grader
print("Welcome to Exam grader.")
markLst = [float(x) for x in input("Enter you marks seperated by a space for \nScience \nChemistry \nPhysics \n-> ").split()]
if len(markLst) < 3 or len(markLst) > 3:
    print("Max | Min of three subjects are required.")
    quit()
for i in markLst:
    if i < 35:
        print("Congratulations you have failed the exams!")
        quit()
average = 0
for i in markLst:
    average += float(i)
average /= 3
if average <= 59:
    print("Your grade is C")
elif average <= 69:
    print("Your grade is B")
else:
    print("Your grade is A")