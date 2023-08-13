class Account:
    def __init__(self, name: str):
        """
        Initial function to be run on start-up
        Name Param: The name of the account
        """
        self.__account_name = name
        self.__account_balance = 0.00

    def deposit(self, amount: float) -> bool:
        """
        Add money
        Amount param: The amount looking to be deposited
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

    def withdrawal(self, amount: float) -> bool:
        """
        Subtract Money
        Amount param: The amount looking to be withdrawn
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
        Returns account balance, a private variable
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Retreive name on account
        Returns account name, a private variable
        """
        return self.__account_name
