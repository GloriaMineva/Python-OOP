from abc import ABC, abstractmethod


class BaseBattleship(ABC):
    def __init__(self, name: str, health: int, hit_strength: int, ammunition: int):
        self.ammunition = ammunition
        self.hit_strength = hit_strength
        self.health = health
        self.name = name
        self.is_attacking = False
        self.is_available = True
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise ValueError("Ship name must contain only letters!")
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            value = 0
        self.__health = value

    @property
    def ammunition(self):
        return self.__ammunition

    @ammunition.setter
    def ammunition(self, value):
        if value < 0:
            value = 0
        self.__ammunition = value

    def take_damage(self, enemy_battleship):
        self.health -= enemy_battleship.hit_strength

    @abstractmethod
    def attack(self):
        pass


