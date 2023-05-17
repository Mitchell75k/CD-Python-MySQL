class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}, Interest Rate: {self.int_rate}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate * self.balance 
        else:
            print("You're broke!")
        return self

# use a classmethod to print all instances of a Bank Account's info (couldn't get this to work)
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()


# Instanciation Test
user_mitchell = BankAccount(0.01, 50)
user_mitchell.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()

user_ashley = BankAccount(0.03, 1000)
user_ashley.deposit(100).deposit(100).withdraw(10).withdraw(10).withdraw(10).withdraw(10).yield_interest().display_account_info()

BankAccount.print_all_accounts()