import random

class Trader:
    def __init__(self, deposit, risk, showTrades=False, confidence=50) -> None:
        self.deposit = deposit
        self.risk = risk
        self.showTrades = showTrades
        self.confidence =confidence 

    def calculateRisk(self, amount, risk):
        return (amount / 100) * risk

    def doTrading(self):
        originalDeposit = self.deposit

        numOfTrades = int(100 / self.risk)
        for i in range(1, numOfTrades + 1):
            currentAmount = (self.deposit / 100) * self.risk

            # Check if the account has enough balance
            if self.deposit < currentAmount:
                break

            if random.random() < (self.confidence / 100):
                # Win trade
                win = currentAmount * 1.5
                self.deposit += win
                if self.showTrades:
                    print(i, ")", " +%.2f" % win, " Bal: %.2f" % self.deposit)
            else:
                # Lost Trade
                self.deposit -= currentAmount
                if self.showTrades:
                    print(i, ")", " -%.2f" % currentAmount, " Bal: %.2f" % self.deposit)

        print("\nOriginal Deposit: %.2f" % originalDeposit)
        print("Current Bal: %.2f" % self.deposit)
        print("Difference: %.2f" % (self.deposit - originalDeposit))


deposit = float(input("Please enter the deposit: "))
risk = float(input("Please enter the risk: "))
num = int(input("Number of stimulations: "))
confidence = float(input("Confidence (50% Default): ") or 50)
show = bool(input("Show trade history: "))

while num > 0:
    mt = Trader(deposit, risk, show, confidence)
    mt.doTrading()
    num -= 1
