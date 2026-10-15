
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: ${amount}")

    def check_balance(self):
        print(f"Account owner: {self.owner}")
        print(f"Current balance: ${self.__balance}")


# Create an account
account1 = BankAccount("Rajput", 1000)

# Call methods
account1.check_balance()

account1.deposit(500)
account1.withdraw(200)

account1.check_balance()
