# Logs will be printed to the console by default
import logging

"""
    Logs can be configured to use a file as a log as below
"""

logging.basicConfig(filename='./log.log', level=logging.DEBUG)

logging.critical("Critical")
logging.error("Error")
logging.warning("Warning")
logging.info("Info")
logging.debug("Debug")

"""
    By default only logs above including warning, namely error and critical are printed to console.
"""

# Example usecase to handle an exception
try:
    num1 = int(input("Enter the Divisior: "))
    num2 = int(input("Enter the Dividend: "))
    ans = num2 / num1
    print("You answer is {}".format(ans))
except ZeroDivisionError:
    logging.error("You cannot divide a number by zero") # Handling for specific error
except ValueError:
    logging.error("Invalid Input, only numerals are allowed") # Handling for soecific error
except:
    logging.critical("Some unknown error occured") # Default error handler
else:
    logging.info("This will be printed if not exception") # This will reach only if there is no exception
finally:
    print("Code in finally") # This code will be executed wether there is an exception or not, in all cases