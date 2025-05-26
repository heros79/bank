class Money:

    def __init__(self, amount: float, currency: str) -> None:
        if amount <= 0:
            raise ValueError('Amount must be positive')

        self.__amount = amount
        self.__currency = currency

    def validate_money(func):
        def wrapp(*args):
            a = args[1]

            if not isinstance(a, Money):
                raise ValueError('Argument must be an instance of Money')

            if a.__amount <= 0:
                raise ValueError('Amount must be positive')

            return func(*args)
        return wrapp

    def validate_param(func):
        def wrapp(*args):
            a = args[1]

            if not isinstance(a, float) and not isinstance(a, int):
                raise ValueError('Argument must be an instance of Money')

            if a <= 0:
                raise ValueError('Amount must be positive')

            return func(*args)
        return wrapp


    def __eq__(self, other):
        return self.__amount == other.__amount and self.__currency == other.__currency

    def __hash__(self):
        return hash((self.__amount, self.__currency))

    @validate_money
    def __add__(self, other):

        if self.__currency != other.__currency:
            raise ValueError('Currencies must match')

        return Money(self.__amount + other.__amount, self.__currency)

    @validate_money
    def __sub__(self, other):
        if self.__currency != other.__currency:
            raise ValueError('Currencies must match')

        return Money(self.__amount - other.__amount, self.__currency)

    @validate_param
    def __mul__(self, other):
        return Money(self.__amount * other, self.__currency)

    @validate_param
    def __truediv__(self, other):
        return Money(self.__amount / other, self.__currency)

    def __str__(self):
        return str(f'amount={self.__amount}, currency={self.__currency}')

    @property
    def amount(self):
        return self.__amount


if __name__ == '__main__':
    m = Money(42, 'USD') / 2.36
    print(m)