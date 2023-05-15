# In order to receive command line args argv is imported from sys module
import sys

lst = sys.argv # lst will contain all the args seperated by a space
# print("Welcome to profile creator, Arguments are name age gender") # Here we will collect the 3 arguments name, age and gender
# print("Your name is {} and your age is {} and you are {}".format(lst[1], lst[2], lst[3]))

# Sample ATM program
accountBal = 10000
if not len(lst) == 2:
    print("Account username should be provided before running the program as an argument.")
    quit()

while True:
    print()
    print("Welcome to XYZ Bank. \n1.Check Balance \n2.Withdraw \n3.Deposit Cash \n4.Deposit Cheque \n5.Exit Program")
    print("\nBanking account: {} Balance: ${}".format(lst[1], accountBal))
    choice = int(input("\nPlease enter the service number and press enter: "))
    if choice == 1:
        print("-> Your balance is ${}".format(str(accountBal)))
        continue
    elif choice == 2:
        withdrawAmount = float(input("Enter the amount you need to withdraw: $"))
        if withdrawAmount > accountBal:
            print("-> Maximum amount that can be withdrawn is $",str(accountBal))
            continue
        else:
            accountBal -= withdrawAmount
            print("-> You have withdrawn ${} successfully, available balance ${}".format(withdrawAmount, accountBal))
            continue
    elif choice == 3:
        depositAmount = float(input("Enter the amount you are willing to deposit: $"))
        accountBal += depositAmount
        print("-> Your deposit was successful, new balance is $",str(accountBal))
        continue
    elif choice == 4:
        checkDetails = [x for x in input("Please enter you cheque number and amount seperated by a space: ").split()]
        accountBal += float(checkDetails[1])
        print("-> Your cheque was accepted and you new balance is $", accountBal)
        continue
    elif choice == 5:
        print("Thank you for using XYZ Banking Services.")
        quit()
    else:
        print("Invalid option selected.")
        continue

