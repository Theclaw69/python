class Account:
    def __init__(self, name: str):
 
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount: float) -> bool:
       
        if amount <= 0:
            return False
        else:
            self.account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:

        if amount <= 0 or amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True

    def get_balance(self) -> float:

        return self.account_balance

    def get_name(self) -> str:

        return self.account_name