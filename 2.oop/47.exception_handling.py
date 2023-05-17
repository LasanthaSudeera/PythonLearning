# Example zeo division error handling
try:
    num1 = int(input("Enter the Divisior: "))
    num2 = int(input("Enter the Dividend: "))
    ans = num2 / num1
    print("You answer is {}".format(ans))
except ZeroDivisionError:
    print("You cannot divide a number by zero") # Handling for specific error
except ValueError:
    print("Invalid Input, only numerals are allowed") # Handling for soecific error
except:
    print("Some unknown error occured") # Default error handler
else:
    print("This will be printed if not exception") # This will reach only if there is no exception
finally:
    print("Code in finally") # This code will be executed wether there is an exception or not, in all cases