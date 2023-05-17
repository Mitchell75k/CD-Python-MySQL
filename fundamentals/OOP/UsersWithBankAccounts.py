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


# New class User--------------------------------------------------------------
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=.02,balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"{self.name} has a Checkings Balance of: ${self.account.balance}")
        return self

    # def transfer_money(self, other_user, amount):       <--- Didn't have time to get this to work
    #     self.account.balance -= amount
    #     other_user.account.balance += amount
    #     return self

# Instanciation Test for BankAccount-------------------------------------------
user_mitchell = BankAccount(0.01, 50)
user_mitchell.deposit(100).deposit(100).deposit(100).withdraw(50).display_account_info().yield_interest().display_account_info()

user_ashley = BankAccount(0.03, 1000)
user_ashley.deposit(50).deposit(50).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()

# New instances of User--------------------------------------------------------

user_mitchell = User("Mitchell", "Alexis75k@icloud.com")
user_mitchell.make_deposit(100).make_withdrawal(50).display_user_balance()


user_ashley = User("Ashley", "Ashley202@burrito.com")
user_ashley.make_deposit(500).make_withdrawal(50).display_user_balance()


