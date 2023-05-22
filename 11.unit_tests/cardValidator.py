import datetime
# Exercise validate credit card
def validateCard(expDate):
    if expDate > datetime.datetime.now().date():
        return "Valid"
    else:
        return "Not valid"