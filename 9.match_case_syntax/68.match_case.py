x = 5

match x:
    case 1 | 4:
        print("One or four")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:  # _ is wild card, default case
        print("Default case")


# Using with constents
class MatchCases:
    withdraw = 1
    deposit = 2
    balance = 3


result = 1

match result:
    case MatchCases.withdraw:
        print("Withdrawing")
    case MatchCases.deposit:
        print("Deposit")
    case MatchCases.balance:
        print("Balance")
    case _:
        print("Invalid")
