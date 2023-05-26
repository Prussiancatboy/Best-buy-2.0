import store
import products
from abc import ABC, abstractmethod

class Promotions(ABC):
    pass


class SecondHalfPrice(Promotions):
    pass

class ThirdOneFree(Promotions):
    pass

class





    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)