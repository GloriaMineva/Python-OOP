from abc import ABC, abstractmethod

valid_types = ['Regular', 'VIP']


class BaseClient(ABC):
    def __init__(self, name: str, membership_type: str):
        self.membership_type = membership_type
        self.name = name
        self.points = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Client name should be determined!")
        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in valid_types:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount: float):
        pass

    def apply_discount(self):
        discount = 0
        remaining_points = 0
        if self.points >= 100:
            discount = 10
            remaining_points = self.points - 100
            self.points -= 100
        elif 50 <= self.points < 100:
            discount = 5
            remaining_points = self.points - 50
            self.points -= 50
        elif self.points < 50:
            discount = 0
            remaining_points = self.points
        discount_and_points = (discount, remaining_points)
        return discount_and_points

