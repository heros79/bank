from decimal import Decimal

from src.enums.enums import CurrencyType


class Account:

    def __init__(self, user_id: int, account_number: str):
        self.__user_id = user_id
        self.__account_number = account_number
        self.__currency_type = CurrencyType.AMD.value
        self.__balance = Decimal(15000)

    @property
    def balance(self) -> Decimal:
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError('Balance cannot be negative')
        self.__balance = value

    @property
    def currency_type(self) -> str:
        return self.__currency_type