from abc import ABC, abstractmethod
from typing import List

from project.battleships.base_battleship import BaseBattleship


class BaseZone(ABC):
    def __init__(self, code: str, volume: int):
        self.volume = volume
        self.code = code
        self.ships: List[BaseBattleship] = []

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value:str):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self.__code = value

    def get_ships(self):
        self.ships = sorted(self.ships, key= lambda s: (-s.hit_strength, s.name))
        return self.ships

    @abstractmethod
    def zone_info(self):
        pass

