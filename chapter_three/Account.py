class Accounts:

    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount > 0:
            self.__balance -= amount

    def _transfer_to(self, account, amount):
        if amount <= self.__balance:
            self.withdraw(amount)
            account.deposit(amount)

