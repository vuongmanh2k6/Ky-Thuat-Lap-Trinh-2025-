class Bank:
    Account_type = "Savings"
    location = "Guntur"

    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.Account_type = Bank.Account_type
        self.location = Bank.location

    def __repr__(self):
        print("Welcome to the SBI ATM Machine")
        print("-------------------------------------")
        account_pin = int(input("Please enter your PIN number: "))

        if account_pin == 123:
            self.Account()
        else:
            print("PIN Incorrect. Please try again")
            self.Error()

        return f"{self.name}, {self.Account_Number}"

    def Error(self):
        account_pin = int(input("Please enter your PIN number again: "))
        if account_pin == 123:
            self.Account()
        else:
            print("PIN Incorrect. Please try again")
            self.Error()

    def Account(self):
        print(f"Your Card Number is: XXXX XXXX XXXX {str(self.Account_Number)[-4:]}")
        print("Would you like to Deposit / Withdraw / Check Balance?")
        print("""
1) Balance
2) Withdraw
3) Deposit
4) Quit
""")
        option = int(input("Please enter your choice: "))

        if option == 1:
            self.Balance()
        elif option == 2:
            self.Withdraw()
        elif option == 3:
            self.Deposit()
        elif option == 4:
            self.Exit()

    def Balance(self):
        print("Balance:", self.balance)
        self.Account()

    def Withdraw(self):
        w = int(input("Please enter amount to withdraw: "))
        if self.balance >= w and w > 0:
            self.balance -= w
            print("Your transaction is successful!")
            print("Your Balance:", self.balance)
        else:
            print("Transaction cancelled due to insufficient funds.")
        self.Account()

    def Deposit(self):
        d = int(input("Please enter amount to deposit: "))
        self.balance += d
        print("Your transaction is successful!")
        print("Balance:", self.balance)
        self.Account()

    def Exit(self):
        print("Exit")


# Create object
t1 = Bank("Mahesh", 1453210145, 5000)

print(t1)
