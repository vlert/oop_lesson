class Account:
    def __init__(self, account_number, account_type, account_name, initial_balance):
        self.account_number = account_number
        self.account_type = account_type
        self.account_name = account_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Depositing {amount} to {self.account_number}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawing {amount} from {self.account_number}")
        else:
            print(
                f"Withdrawal amount {amount} exceeds the balance of {self.balance} for {self.account_number} account.")

    def show_account_details(self):
        print(f"Showing details for {self.account_number}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Account Name: {self.account_name}")
        print(f"Balance: {self.balance}")


account1 = Account("0000", "saving", "David Patterson", 1000)
account2 = Account("0001", "checking", "John Hennessy", 2000)

account1.show_account_details()
account1.deposit(50)
account1.show_account_details()
account1.withdraw(25)
account1.show_account_details()

account2.show_account_details()
account2.deposit(300)
account2.show_account_details()
account2.withdraw(5000)

