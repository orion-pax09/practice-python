class BankAccount:
    def __init__(self,current_balance,account_name,account_number):
        self.current_balance=current_balance
        self.account_name=account_name
        self.account_number=account_number
    def __str__(self):
        return f"{self.account_name} account's current balance is ${self.current_balance}"
    def deposits(self,amount):
        self.current_balance +=amount
        return f"{self.account_name},${amount} has been deposited, current balance:-${self.current_balance}"
    def withdraw(self,amount):
        if amount < 0:
            return f"your current balance is zero"
        else:
            self.current_balance -=amount
            return f"{self.account_name},${amount} has been successfully withdrawn,current balance:{self.current_balance}"
p1=BankAccount(current_balance=8000000,account_name="Muhammad Hamza Khan",account_number=3310251666049)
print(p1.deposits(56000))
print(p1.withdraw(6500))
print(p1)