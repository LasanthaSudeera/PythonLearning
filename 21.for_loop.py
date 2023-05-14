# FOR loop, prints numbers from 50 to 70 
for i in range(50,71):  # 71 because the max is ignored
    print(i)

# Break the loop on 5
print("Break loop on 5")
for i in range(1, 12):
    if i == 5:
        break
    else:
        print(i)

# Skip if the number is a multiple of 3
print("Skips multiples of 3")
for i in range(1, 21):
    if int(i) % 3 == 0:
        continue
    print(i)

# Mutilpication table generator
multiplier = int(input("Enter a multiper to generate a multiplication table: "))
for i in range(0,13):
    print("{} X {} = {}".format(multiplier, i, multiplier * i))

# Check if the given number is prime or not
number = int(input("Enter a number to check Prime or Not Prime: "))
primeFlag = True
for i in range(2, number-1):
    if(number%i == 0):
        primeFlag = False
        break
if primeFlag:
    print("The number is a prime number")
else:
    print("The number is not a prime number")

