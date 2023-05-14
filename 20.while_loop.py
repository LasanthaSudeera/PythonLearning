# while Loop, prints upto 20, as the condition to stop the loop is when i is more than 21
i = 0
while i < 21:
    print(i)
    i+=1

# A program to display all the Odd numbers between a selected values
print("Odd or Even Range")
lst = [int(x) for x in input("Enter a range of numbers seperated by space to get the odd numbers: ").split()]
start = lst[0]
end = lst[1]
while start <= end:
    if not start %2 == 0:
        print(start)
        start += 1
    else:
        start +=1
        continue

# A program that print a range of number between selected and a max of 100, skipping multiples of 10
lst = [int(x) for x in input("Enter a range of numbers you want to generate: ").split()]
start = lst[0]
end = lst[1]
while start <= end:
    if start > 100:
        break

    if start%10 == 0:
        start +=1
        continue
    else:
        print(start)
        start +=1

    