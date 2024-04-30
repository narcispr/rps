#!/usr/bin/env python3

from rps.players import RPSPlayer, HumanPlayer, ComputerPlayer

class RockPaperScissors:
    """A class to represent a Rock-paper-scissors game

    Attributes:
        player1 (RPSPlayer): The first player.
        player2 (RPSPlayer): The second player.
        max_turns (int): The maximum number of turns in the game.
    """
    
    def __init__(self, player1: RPSPlayer, player2: RPSPlayer, max_turns:int=3) -> None:
        """Initialize a Rock-paper-scissors game.

        Args:
            player1 (RPSPlayer): The first player.
            player2 (RPSPlayer): The second player.
            max_turns (int, optional): The maximum number of turns in the game. Defaults to 3.
        """
        
        self.player1 = player1
        self.player2 = player2
        self.max_turns = max_turns
    
    def play(self):
        """Play the Rock-paper-scissors game."""

        for t in range(self.max_turns):
            p1_choice = self.player1.choose()
            p2_choice = self.player2.choose()
            print(f"Turn {t+1}:")
            print(f"{self.player1.name} chooses {p1_choice}")
            print(f"{self.player2.name} chooses {p2_choice}")
            if p1_choice == p2_choice:
                print("It's a tie!")
            elif p1_choice == 'rock' and p2_choice == 'scissors':
                print(f"{self.player1.name} wins!")
                self.player1.score += 1
            elif p1_choice == 'scissors' and p2_choice == 'paper':
                print(f"{self.player1.name} wins!")
                self.player1.score += 1
            elif p1_choice == 'paper' and p2_choice == 'rock':
                print(f"{self.player1.name} wins!")
                self.player1.score += 1
            else:
                print(f"{self.player2.name} wins!")
                self.player2.score += 1
        
        print("Game over!")
        print(f"{self.player1.name} score: {self.player1.score}")
        print(f"{self.player2.name} score: {self.player2.score}")
        
        if self.player1.score > self.player2.score:
            print(f"{self.player1.name} wins the game!")
        elif self.player1.score < self.player2.score:
            print(f"{self.player2.name} wins the game!")
        else:
            print("It's a tie!")

def main():
    player1 = HumanPlayer("Human")
    player2 = ComputerPlayer("Computer")
    game = RockPaperScissors(player1, player2)
    game.play()

if __name__ == "__main__":
    main()
