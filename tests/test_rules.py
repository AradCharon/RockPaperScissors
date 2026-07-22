import pytest

from rules import determine_winner
from constants import Move


@pytest.mark.parametrize(
    "player, computer, expected",
    [
        (Move.ROCK, Move.ROCK, "It's a tie!"),
        (Move.PAPER, Move.PAPER, "It's a tie!"),
        (Move.SCISSORS, Move.SCISSORS, "It's a tie!"),

        (Move.ROCK, Move.SCISSORS, "You win!"),
        (Move.PAPER, Move.ROCK, "You win!"),
        (Move.SCISSORS, Move.PAPER, "You win!"),

        (Move.ROCK, Move.PAPER, "Computer wins!"),
        (Move.PAPER, Move.SCISSORS, "Computer wins!"),
        (Move.SCISSORS, Move.ROCK, "Computer wins!"),
    ],
)
def test_determine_winner(player, computer, expected):
    assert determine_winner(player, computer) == expected