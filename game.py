from player import HumanPlayer, ComputerPlayer
from rules import determine_winner
from messages import MENU, GOODBYE, INVALID_OPTION


class Game:
    def __init__(self):
        self.human = HumanPlayer()
        self.computer = ComputerPlayer()

    def run(self):
        while True:
            self.show_menu()

            choice = input("Select option: ").strip()

            if choice == "1":
                self.play()

            elif choice == "2":
                print(GOODBYE)
                break

            else:
                print(INVALID_OPTION)

    def show_menu(self):
        print(MENU)

    def play(self):
        while True:

            user_move = self.human.choose_move()

            if user_move is None:
                break

            computer_move = self.computer.choose_move()

            print(f"\nYou chose: {user_move}")
            print(f"Computer chose: {computer_move}")

            result = determine_winner(user_move, computer_move)

            print(result)

            again = input("\nPlay again? (y/n): ").lower()

            if again != "y":
                break