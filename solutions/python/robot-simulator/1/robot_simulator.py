# Globals for the directions
# Change the values as you see fit
from typing import Literal

EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos

    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)

    def _move_ahead(self, step: int = 1):
        if self.direction == NORTH:
            self.y_pos += step
        if self.direction == EAST:
            self.x_pos += step
        if self.direction == SOUTH:
            self.y_pos -= step
        if self.direction == WEST:
            self.x_pos -= step

    def _rotate(self, direction: Literal["L", "R"]):
        move = 1 if direction == "L" else 3
        self.direction = (self.direction + move) % 4

    def move(self, actions: str):
        for action in actions:
            if action in "A":
                self._move_ahead()
            if action in "LR":
                self._rotate(action)
