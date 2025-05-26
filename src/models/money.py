class Money:

    def __init__(self, amount, currency):
        if amount <= 0:
            raise ValueError('Amount must be positive')

        self.__amount = amount
        self.__currency = currency


    def __eq__(self, other):
        return self.__amount == other.__amount and self.__currency == other.__currency

    def __hash__(self):
        return hash((self.__amount, self.__currency))

    def __add__(self, other):
        if self.__currency != other.__currency:
            raise ValueError('Currencies must match')

        if other.__amount <= 0:
            raise ValueError('Amount must be positive')

        return Money(self.__amount + other.__amount, self.__currency)

    def __sub__(self, other):
        if self.__currency != other.__currency:
            raise ValueError('Currencies must match')

        if other.__amount <= 0:
            raise ValueError('Amount must be positive')

        return Money(self.__amount - other.__amount, self.__currency)