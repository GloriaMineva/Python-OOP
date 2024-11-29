from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    def __init__(self, code: str):
        super().__init__(code, 8)

    def zone_info(self):
        if len(self.ships) > 0:
            royal_ships_count = [s for s in self.ships if s.__class__.__name__ == 'RoyalBattleship']
            result = "@Pirate Zone Statistics@\n"
            result += f'Code: {self.code}; Volume: {self.volume}\n'
            result += f'Battleships currently in the Pirate Zone: {len(self.ships)}, {len(royal_ships_count)} out of them are Royal Battleships.\n'
            self.get_ships()
            ships_names = [s.name for s in self.ships]
            result += f'#{", ".join(ships_names)}#\n'
            return result


