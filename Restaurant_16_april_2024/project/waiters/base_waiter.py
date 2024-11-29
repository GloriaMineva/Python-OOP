from abc import ABC, abstractmethod


class BaseWaiter(ABC):
    def __init__(self, name: str, hours_worked: int):
        self.hours_worked = hours_worked
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not 3 <= len(value.strip()) <= 50:
            raise ValueError("Waiter name must be between 3 and 50 characters in length!")
        self.__name = value
        
    @property
    def hours_worked(self):
        return self.__hours_worked
    
    @hours_worked.setter
    def hours_worked(self, value):
        if value < 0:
            raise ValueError("Cannot have negative hours worked!")
        self.__hours_worked = value

    @abstractmethod
    def calculate_earnings(self):
        pass

    @abstractmethod
    def report_shift(self):
        pass

    def __str__(self):
        total_earnings = self.calculate_earnings()
        return f"Name: {self.name}, Total earnings: ${total_earnings:.2f}"