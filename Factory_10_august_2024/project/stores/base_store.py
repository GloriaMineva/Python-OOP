from abc import ABC, abstractmethod
from typing import List

from project.products.base_product import BaseProduct


class BaseStore(ABC):
    def __init__(self, name: str, location: str, capacity: int):
        self.capacity = capacity
        self.location = location
        self.name = name
        self.products: List[BaseProduct] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if ' ' in value.strip() or len(value.strip()) != 3:
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value
        
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value

    def get_estimated_profit(self):
        products_sum = sum([el.price for el in self.products])
        estimated_profit = products_sum * 0.1
        return f"Estimated future profit for {len(self.products)} products is {estimated_profit:.2f}"

    @property
    @abstractmethod
    def store_type(self):
        pass


    @abstractmethod
    def store_stats(self):
        pass
