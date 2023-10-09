class BankAccount:
    def __init__(self, accountNumber,balance):
        self._acNo = accountNumber #protected attribute
        self.__bal = balance # private attribute

    def deposit(self, amount):
        self.__bal = self.__bal+amount

    def withdraw(self,amount):
        if self.__bal <= amount:
            return("Insufficient funds")
        else:
            self.__bal = self.__bal - amount

    def checkBalance(self):
        return self.__bal
    

manneshaAccount = BankAccount("EKI876543212", 1000000)

print(manneshaAccount._acNo)

manneshaAccount.deposit(5000)
print(manneshaAccount.checkBalance())


manneshaAccount.withdraw(15000)
print(manneshaAccount.checkBalance())
