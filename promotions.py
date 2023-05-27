from abc import ABC, abstractmethod


class Promotions(ABC):
    """This sets the standard for the others"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def add_promotion(self, total, price, quantity):
        """This too sets the standard for the others"""
        pass


class SecondHalfPrice(Promotions):
    """Every second item is half off"""
    def __init__(self, name):
        super().__init__(name)

    def add_promotion(self, total, price, quantity):
        """This code adds the promotion"""
        flag = True
        while flag is True:
            result = quantity - 2
            if result >= 0:
                quantity -= 2
                total = total - price/2
            else:
                flag = False
        return total


class ThirdOneFree(Promotions):
    """Every third item is free"""
    def __init__(self, name):
        super().__init__(name)

    def add_promotion(self, total, price, quantity):
        """This code adds the promotion"""
        flag = True
        while flag is True:
            result = quantity - 3
            if result >= 0:
                quantity -= 3
                total = total - price
            else:
                flag = False
        return total


class PercentDiscount(Promotions):
    """Each item is off by a percentage"""
    def __init__(self, name, percent):
        super().__init__(name)
        self.percentage = percent

    def add_promotion(self, total, price, quantity):
        """This code adds the promotion"""
        percent = self.percentage / 100
        result = percent * 250
        total -= result
        return total
