import random
from constants import Move
from messages import MOVE_MENU, PLEASE_ENTER_NUMBER, INVALID_MOVE


class Player:
    """Base class for all players."""

    def choose_move(self):
        raise NotImplementedError("Subclasses must implement choose_move().")


class HumanPlayer(Player):
    """Human player."""

    def choose_move(self):
        while True:
            print(MOVE_MENU)

            choice = input("Enter your choice: ").strip()

            if choice == "0":
                return None

            if not choice.isdigit():
                print(PLEASE_ENTER_NUMBER)
                continue

            choice = int(choice)

            if choice == 1:
                return Move.ROCK
            elif choice == 2:
                return Move.PAPER
            elif choice == 3:
                return Move.SCISSORS
            else:
                print(INVALID_MOVE)


class ComputerPlayer(Player):
    """Computer player."""

    def choose_move(self):
        return random.choice(list(Move))