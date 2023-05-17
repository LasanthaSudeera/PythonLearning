# Defining a custom exception
class OverTheLimitException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def withdraw(amount):
    if amount > 500:
        raise OverTheLimitException("Max per day is 500")
    
withdraw(300)


# Example password validation exception
class InvalidPasswordException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def createPassword(password):
    if(len(password) < 8):
        raise InvalidPasswordException("Your password is weak")
    print("Good password")

try:
    createPassword('123')
except InvalidPasswordException as obj:
    print(obj)