# Objective: Deepen OOP skills by extending the banking system with customer management and bank operations.

# Features:
# Create customers with personal info
# Open multiple accounts per customer (checking/savings)
# Transfer between accounts (same customer + different customers)
# Bank-level statistics: total deposits, most valuable customer
# Transaction fees for certain operations

from datetime import datetime




# Customer Class: Manages multiple accounts, personal details
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
            self._record_transaction("deposit",amount)

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self._balance:
            print("Invalid, You don't have enough money to withdraw")
        else:
            self._balance -= amount
            self._record_transaction("withdraw",amount)

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
            self._record_transaction("withdraw",amount)


class CheckingAccount(BankAccount): # with overdraft limit
    def __init__(self, account_number, holder_name, balance, overdraft_limit =-100):
        super().__init__(account_number, holder_name, balance, "Checking account")
        self.overdraft_limit = overdraft_limit

    def withdraw(self,amount):
        if self._balance - amount < self.overdraft_limit:
            print("Declined: Would exceed overdraft limit")
        else:
            self._balance -= amount

class Customer:
    def __init__(self, customer_id, name, contact):
        self.customer_id = customer_id
        self.name = name
        self.contact = contact
        self.accounts = [] #contian "Saving"/"checking" # List of BankAccount objects

    def add_account(self, account) -> None:
        self.accounts.append(account) # Add BankAccount object

    def remove_account(self, account_number):
        for i, account in enumerate(self.accounts):
            if account.account_number == account_number:
                self.accounts.pop(i)
                print(f"Account {account_number} removed")
                return
        print(f"Account {account_number} not found")

    def get_total_balance(self):
        total = 0
        for account in self.accounts:
            total += account.get_balance()  # Use public getter
        return total

    def transfer(self, from_account, to_account, amount, fee_percent=0.02):
        # from_account and to_account are BankAccount objects
        if amount <= 0:
            print("Amount must be positive")
        elif from_account.get_balance() < amount:
            print("Insufficient funds")
        else:
            # Check if accounts belong to same customer
            if to_account in self.accounts:
                # Same customer - no fee
                from_account.withdraw(amount)
                to_account.deposit(amount)
            else:
                # Different customer - apply fee
                fee = amount * fee_percent
                total = amount + fee
                if from_account.get_balance() < total:
                    print(f"Insufficient funds including ${fee:.2f} fee")
                else:
                    from_account.withdraw(total)
                    to_account.deposit(amount)
                    print(f"Transfer complete. Fee: ${fee:.2f}")

class Bank:
    def __init__(self, bank_name):  # Not customer_id
        self.bank_name = bank_name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer_id):
        for i, customer in enumerate(self.customers):
            if customer.customer_id == customer_id:
                self.customers.pop(i)
                print(f"Customer {customer_id} removed")
                return
        print(f"Customer {customer_id} not found")


    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def total_deposits(self):
        total = 0
        for customer in self.customers:
            total += customer.get_total_balance()
        return total

    def richest_customer(self):
        if not self.customers:
            return None
        richest = self.customers[0]
        for customer in self.customers:
            if customer.get_total_balance() > richest.get_total_balance():
                richest = customer
        return richest


def main():
    # Create bank
    bank = Bank("G.M.Y.M")

    # Create customers
    alice = Customer("C001", "Alice Smith", "alice@email.com")
    bob = Customer("C002", "Bob Johnson", "bob@email.com")

    # Add accounts
    alice.add_account(CheckingAccount("ACC1001", "Alice Smith", 5000))
    alice.add_account(SavingsAccount("ACC1002", "Alice Smith", 10000))
    bob.add_account(CheckingAccount("ACC2001", "Bob Johnson", 3000))

    # Add customers to bank
    bank.add_customer(alice)
    bank.add_customer(bob)

    # Test operations
    print(f"Bank: {bank.bank_name}")
    print(f"Total deposits: ${bank.total_deposits():.2f}")

    richest = bank.richest_customer()
    if richest:
        print(f"Richest customer: {richest.name} (${richest.get_total_balance():.2f})")

    # Test transfer
    alice_savings = alice.accounts[1]  # Savings account
    bob_checking = bob.accounts[0]  # Checking account

    print(f"\nBefore transfer - Alice: ${alice.get_total_balance():.2f}, Bob: ${bob.get_total_balance():.2f}")
    alice.transfer(alice_savings, bob_checking, 1000)
    print(f"After transfer - Alice: ${alice.get_total_balance():.2f}, Bob: ${bob.get_total_balance():.2f}")


if __name__ == "__main__":
    main()

# PS : SavingsAccount.withdraw() doesn't call parent's _record_transaction() (but still works). Do a research to know why!

# later :
# Add customer  : maybe I will generate a random ID per costumer
# Add more validation for account numbers
# Format transaction dates better