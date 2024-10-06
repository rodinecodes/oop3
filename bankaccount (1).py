class BankAccount:
    interest_rate = 0.05  

    def __init__(self, account_holder):
        self.account_holder = account_holder  
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def apply_interest(self):
        self.balance += self.balance * BankAccount.interest_rate

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

account1 = BankAccount("luyima rodine")
account2 = BankAccount("kwagala dave")
account3 = BankAccount("najjemba zahara")
account4 = BankAccount("lynet kk")

account1.deposit(1000)
account1.withdraw(200)
account1.apply_interest()
account1.display_account_info()

account2.deposit(2000)
account2.withdraw(150)
account2.apply_interest()
account2.display_account_info()

account3.deposit(5500)
account3.withdraw(1205)
account3.apply_interest()
account3.display_account_info()

account4.deposit(3759)
account4.withdraw(55)
account4.apply_interest()
account4.display_account_info()



