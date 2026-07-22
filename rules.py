from constants import Move
from messages import PLAYER_WIN, COMPUTER_WIN, TIE


WIN_RULES = {
    Move.ROCK: Move.SCISSORS,
    Move.PAPER: Move.ROCK,
    Move.SCISSORS: Move.PAPER,
}


def determine_winner(player_move: Move, computer_move: Move) -> str:
    """
    Determines the winner of a round.

    Args:
        player_move: The player's move.
        computer_move: The computer's move.

    Returns:
        A string describing the result.
    """

    if player_move == computer_move:
        return TIE

    if WIN_RULES[player_move] == computer_move:
        return PLAYER_WIN

    return COMPUTER_WIN