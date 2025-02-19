class Account:
    def __init__(self, account_number, pin, name, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.name = name
        self.balance = balance
        self.transactions = []

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient amount"
        self.balance -= amount
        self.transactions.append(f"Withdraw: -VND {amount}")
        return f"Withdrawn ${amount}. New balance: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +${amount}")
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def transfer(self, receiver, amount):
        if amount > self.balance:
            return "Insufficient amount"
        self.balance -= amount
        receiver.balance += amount
        self.transactions.append(f"Transfer: -VND{amount} to {receiver.account_number}")
        receiver.transactions.append(f"Transfer: +VND{amount} from {self.account_number}")
        return f"Transferred ${amount} to {receiver.account_number}"

    def get_balance(self):
        return f"Balance: VND {self.balance}"

    def get_transaction_history(self):
        return self.transactions if self.transactions else ["No transactions"]

    def get_info(self):
        return f"Account Number: {self.account_number}  Name: {self.name}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            return True
        return False

    def account_info(self):
        return [account for account in self.accounts.values()]

    def cancel_account(self, account_number):
        del self.accounts[account_number]
