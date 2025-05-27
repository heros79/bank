from functools import wraps

@wraps
def validate_money(func):
    def wrapp(*args):
        a = args[1]

        if not isinstance(a, Money):
            raise ValueError('Argument must be an instance of Money')

        if a.amount <= 0:
            raise ValueError('Amount must be positive')

        return func(*args)
    return wrapp

@wraps
def validate_param(func):
    def wrapp(*args):
        a = args[1]

        if not isinstance(a, float) and not isinstance(a, int):
            raise ValueError('Argument must be an instance of Money')

        if a <= 0:
            raise ValueError('Amount must be positive')

        return func(*args)
    return wrapp

@wraps
def validate_currency(func):
    def wrapp(*args):
        current = args[0]
        other = args[1]
        if current.currency != other.currency:
            raise ValueError('Currency must be same')
        return func(*args)
    return wrapp

class Money:

    def __init__(self, amount: float, currency: str) -> None:
        if amount < 0:
            raise ValueError('Amount must be positive')

        self.__amount = amount
        self.__currency = currency

    def __eq__(self, other):
        return self.__amount == other.amount and self.__currency == other.currency

    def __hash__(self):
        return hash((self.__amount, self.__currency))

    @validate_money
    @validate_currency
    def __add__(self, other):
        total = Money(self.__amount + other.__amount, self.__currency)
        return total

    @validate_money
    @validate_currency
    def __sub__(self, other):
        total = Money(self.__amount - other.__amount, self.__currency)
        return total

    @validate_param
    def __mul__(self, other):
        total = Money(self.__amount * other, self.__currency)
        return total

    @validate_param
    def __truediv__(self, other):
        total = Money(self.__amount / other, self.__currency)
        return total

    @validate_param
    def __rmul__(self, other):
        total = Money(self.__amount * other, self.__currency)
        return total

    @validate_param
    def __rtruediv__(self, other):
        total = Money(self.__amount / other, self.__currency)
        return total

    def __str__(self):
        return f'amount={self.__amount}, currency={self.__currency}'

    def __repr__(self):
        return f'Money(amount={self.__amount}, currency={self.__currency})'

    @property
    def amount(self):
        return self.__amount

    @property
    def currency(self):
        return self.__currency