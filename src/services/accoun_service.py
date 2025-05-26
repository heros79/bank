from decimal import Decimal

from src.enums.enums import CurrencyType
from src.models.account_model import Account


class AccountService:

    def __init__(self, user_id: int, account_number: str):
        self.__user_id = user_id
        self.__account_number = account_number
        self.__account = None


    def increase_amount(self, currency: str, amount: Decimal) -> bool:
        AccountService.validation_currency_and_amount(currency, amount)

        self.__account = self.__get_account(self.__user_id,self.__account_number)

        if currency != self.__account.currency_type:
            raise ValueError('Currency must be equal to balance.currency')

        balance = self.__account.balance + Decimal(amount)
        self.__account.balance = balance
        return True


    async def decrease_amount(self, currency: str, amount: Decimal) -> bool:
        AccountService.validation_currency_and_amount(currency, amount)

        self.__account = self.__get_account(self.__user_id,self.__account_number)

        if currency != self.__account.currency_type:
            raise ValueError('Currency must be equal to balance.currency')

        if self.__account.balance - Decimal(amount) < 0:
            raise ValueError('Amount must be not negative')

        balance = self.__account.balance - Decimal(amount)
        self.__account.balance = balance

        return True


    def __get_account(self, user_id: int, account_number: str) -> Account:
        return Account(user_id, account_number)

    @classmethod
    def validation_currency_and_amount(cls, currency: str, amount: Decimal) -> None:
        if currency not in CurrencyType:
            raise ValueError('Currency must be one of: ' + str(CurrencyType))

        if amount <= 0:
            raise ValueError('Amount must be positive')

