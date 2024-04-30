import random

class RPSPlayer:
    """A class to represent a Rock-paper-scissors player.

    Attributes:
        name (str): The name of the player.
        score (int): The score of the player.
    """

    def __init__(self, name) -> None:
        """Initialize a Rock-paper-scissors player.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.score = 0
    
class HumanPlayer(RPSPlayer):
    """A class to represent a human player."""

    def choose(self) -> str:
        """Let the human player choose rock, paper, or scissors.

        Returns:
            str: The choice of the human player.
        """
        choice = input("Please choose rock, paper, or scissors: ")
        while choice not in ['rock', 'paper', 'scissors']:
            choice = input("Invalid choice. Please choose rock, paper, or scissors: ")
        return choice

class ComputerPlayer(RPSPlayer):
    """A class to represent a computer player."""

    def choose(self) -> str:
        """Let the computer player choose rock, paper, or scissors randomly.

        Returns:
            str: The choice of the computer player.
        """
        return random.choice(['rock', 'paper', 'scissors'])