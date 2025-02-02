class Account:
    def __init__(self):
        self.owner = input("Enter account owner's name: ")
        self.balance = float(input("Enter initial balance: "))

    def deposit(self):
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self):
        amount = float(input("Enter withdrawal amount: "))
        if amount > self.balance:
            print("Insufficient funds! Withdrawal denied.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive.")

acc = Account()


acc.deposit()
acc.withdraw()
acc.withdraw()
acc.deposit()
