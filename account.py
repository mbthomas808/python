class Account:
    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0.00

    def deposit(self, amount) -> bool:
        """
        Add money
        """
        try:
            amount = float(amount)
        except ValueError:
            return False
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdrawal(self, amount) -> bool:
        """
        Subtract Money
        """
        try:
            amount = float(amount)
        except ValueError:
            return False
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Retreive balance of account
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Retreive name on account
        """
        return self.__account_name
