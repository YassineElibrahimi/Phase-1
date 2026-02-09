# Deliverable:
# BankAccount class with proper encapsulation, inheritance for different account types, and transaction history.



from datetime import datetime


class BankAccount:
    def __init__(self,account_number, holder_name, balance, account_type):
        self.account_number = account_number
        self.holder_name    = holder_name
        self._balance       = balance
        self.account_type   = account_type
        self._transaction   = []
        # self._interest      = []

    def get_balance(self):
        return self._balance

    def deposit(self,amount):
        if amount <= 0:
            print("Invalid, You can't deposit a negative number")
        else:
            self._balance += amount
            self._record_transaction("deposit",f"{amount}")

    def withdraw(self,amount):
        if amount >= self._balance:
            print("Invalid, You don't have enough money to withdraw")
        else:
            self._balance -= amount
            self._record_transaction("withdraw",f"{amount}")

    def _record_transaction(self,operation_type,amount):
        date = datetime.now()
        transaction_Data = {"operation" : operation_type,
                            "amount"    : amount,
                            "date"      : date}
        self._transaction.append(transaction_Data)
    def __str__(self):
        return f"| {self.account_type} | {self.account_number} | {self.holder_name} | {self._balance} |"


class SavingsAccount(BankAccount):# with interest rate
    def __init__(self, account_number, holder_name, balance, interest_rate=0.02):
        super().__init__(account_number, holder_name, balance, "Saving account")
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self._balance * self.interest_rate
        self._balance+= interest

    def withdraw(self,amount):
        if amount > 500:
            print("You can only withdraw 500 per day")
        else:
            self._balance -= amount
            self._record_transaction("withdraw",f"{amount}")


class CheckingAccount(BankAccount): # with overdraft limit
    def __init__(self, account_number, holder_name, balance, overdraft_limit =-100):
        super().__init__(account_number, holder_name, balance, "Checking account")
        self.overdraft_limit = overdraft_limit

    def withdraw(self,amount):
        if self._balance - amount < self.overdraft_limit:
            print("Declined: Would exceed overdraft limit")
        else:
            self._balance -= amount