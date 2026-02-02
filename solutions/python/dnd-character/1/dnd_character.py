from math import floor
import random
from itertools import cycle


class Character:
    def __init__(self, name: str = "hero"):
        self.name = name
        self.strength = self._init_abi()
        self.dexterity = self._init_abi()
        self.constitution = self._init_abi()
        self.intelligence = self._init_abi()
        self.wisdom = self._init_abi()
        self.charisma = self._init_abi()
        self._abilitites = [
            self.strength, self.dexterity, self.constitution,
            self.intelligence, self.wisdom, self.charisma
        ]
        self._ability_cycle = cycle(self._abilitites)

        self.hitpoints = 10 + modifier(self.constitution)

    def _troll(self, limit: int) -> int:
        return random.randint(1, limit)

    def _init_abi(self, limit: int = 6, t: int = 4, drop: int = 1) -> int:
        return sum(sorted([self._troll(limit) for _ in range(t)])[drop:])

    def ability(self) -> int:
        return next(self._ability_cycle)


def modifier(value: int) -> int:
    return floor((value - 10) / 2)
