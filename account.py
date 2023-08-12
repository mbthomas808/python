class Account:
    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0.00

    def deposit(self, amount: float) -> bool:
        """
        Adds money to balance
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdrawal(self, amount: float) -> bool:
        """
        Subtracts money from balance
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Gets private variable account_balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Gets private variable account_name
        """
        return self.__account_name

