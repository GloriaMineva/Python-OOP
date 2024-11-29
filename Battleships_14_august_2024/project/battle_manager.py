from typing import List

from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone

valid_zones = {'PirateZone': PirateZone, 'RoyalZone': RoyalZone}
valid_ships = {'RoyalBattleship': RoyalBattleship, 'PirateBattleship': PirateBattleship}
class BattleManager:
    def __init__(self):
        self.zones: List[BaseZone] = []
        self.ships: List[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in valid_zones:
            raise Exception("Invalid zone type!")
        try:
            existing_zone = next(el for el in self.zones if el.code == zone_code)
            raise Exception("Zone already exists!")
        except StopIteration:
            new_zone = valid_zones[zone_type](zone_code)
            self.zones.append(new_zone)
            return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in valid_ships:
            raise Exception(f"{ship_type} is an invalid type of ship!")
        new_ship = valid_ships[ship_type](name, health, hit_strength)
        self.ships.append(new_ship)
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"
        if ship.health == 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"
        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"
        if zone.__class__.__name__[:5] == ship.__class__.__name__[:5]:
            ship.is_attacking = True
        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1
        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        try:
            existing_ship = next(s for s in self.ships if s.name == ship_name)
            if not existing_ship.is_available:
                return "The ship participates in zone battles! Removal is impossible!"
            self.ships.remove(existing_ship)
            return f"Successfully removed ship {ship_name}."
        except StopIteration:
            return f"No ship with this name!"

    def start_battle(self, zone: BaseZone):
        if len(zone.ships) <= 1:
            return "Not enough participants. The battle is canceled."
        attack_ships = [s for s in zone.ships if s.is_attacking]
        target_ships = [s for s in zone.ships if not s.is_attacking]
        if len(attack_ships) == 0 or len(target_ships) == 0:
            return "Not enough participants. The battle is canceled."
        attack_ships = sorted(attack_ships, key= lambda s: -s.hit_strength)
        target_ships = sorted(target_ships, key=lambda s: -s.health)
        strongest_attacker = attack_ships[0]
        healthier_target = target_ships[0]
        strongest_attacker.attack()
        healthier_target.take_damage(strongest_attacker)
        if healthier_target.health == 0:
            self.ships.remove(healthier_target)
            zone.ships.remove(healthier_target)
            zone.volume += 1
            return f"{healthier_target.name} lost the battle and was sunk."
        if strongest_attacker.ammunition == 0:
            self.ships.remove(strongest_attacker)
            zone.ships.remove(strongest_attacker)
            zone.volume += 1
            return f"{strongest_attacker.name} ran out of ammunition and leaves."
        return "Both ships survived the battle."

    def get_statistics(self):
        result = ''
        available_ships_names = [s.name for s in self.ships if s.is_available]
        result += f'Available Battleships: {len(available_ships_names)}\n'
        if len(available_ships_names) > 0:
            result += f'#{", ".join(available_ships_names)}#\n'
        self.zones = sorted(self.zones, key=lambda s: s.code)
        result += '***Zones Statistics:***\n'
        result += f'Total Zones: {len(self.zones)}\n'
        for zone in self.zones:
            result += zone.zone_info()
        return result
