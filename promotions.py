from abc import ABC, abstractmethod


class Promotions(ABC):
    def __init__(self, name):
        self.name = name


class SecondHalfPrice(Promotions):
    def __init__(self, name):
        super().__init__(name)


class ThirdOneFree(Promotions):
    def __init__(self, name):
        super().__init__(name)


class PercentDiscount(Promotions):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percentage = percent



