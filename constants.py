from enum import Enum, auto


class Move(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    def __str__(self):
        return self.name.capitalize()

