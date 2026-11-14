class BankAccount:

    def __init__(self, account_number, holder_name, balance: float = 0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        print("Account Holder:", self.holder_name)
        print("Account Number:", self.account_number)
        print("Current Balance: ₹", self.balance)


acc_no = input("Enter Account Number: ")
name = input("Enter Account Holder Name: ")
balance = float(input("Enter Initial Balance: "))

account = BankAccount(acc_no, name, balance)

while True:
    print("\n--- BANK ACCOUNT MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.get_balance()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")