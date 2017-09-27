class Account:
    def __init__(self, id1=0, balance=100.0, annualIntrestrate=0.0):
        print("init done")
        self.__id1 = id1
        self.__balance = balance
        self.__annualIntrestrate = annualIntrestrate

    def getid(self):
        return self.__id1

    def getbalance(self):
        return self.__balance

    def getannualIntrestrate(self):
        return self.annualIntrestrate

    def setid(self, id1):
        self.__id1 = id1

    def setbalance(self, balance):
        self.__balance = balance

    def setannualIntrestrate(self, annualIntrestrate):
        self.annualIntrestrate = annualIntrestrate

    def getmonthlyIntrestrate(self):
        return self.__annualIntrestrate / 1200

    def getmonthlyIntrest(self):
        return self.__balance * self.getmonthlyIntrestrate()

    def withdraw(self, amount):
        if (self.__balance - amount < 1000):
            print("cannot withdraw insufficient balance")
        else:
            self.__balance = self.__balance - amount
        return

    def deposit(self, amount):
        self.__balance = self.__balance + amount


def main():
    account = Account(1122, 20000, 4.5)
    print("The Account id is " + str(account.getid()))
    print("The Balance Available is " + str(account.getbalance()))
    print("The Monthly Intrestrate is" + str(account.getmonthlyIntrestrate()))
    print("The Monthly Intrest is " + str(account.getmonthlyIntrest()))

    account.deposit(2500)
    print("The Balance Available after deposit is" + str(account.getbalance()))

    account.withdraw(3000)
    print("The Balance Available after withdraw is" + str(account.getbalance()))


main()