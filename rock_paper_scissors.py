"""
Simple rock, paper, scissors game

Author: phortheman
"""
import random
from enum import Enum, auto

class Hand(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    @classmethod
    def validInput( cls, value ) -> bool:
        return value in cls.__members__


def main():

    wins: int = 0
    games: int = 0

    while True:
        cpuHand = Hand( random.randint(1,3) )

        print( "Rock, paper or scissors? Q to quit" )
        playerInput = input("-> ").upper()

        if playerInput == "Q":
            break
        elif not Hand.validInput( playerInput ):
            print( "Please enter rock, paper or scissors only!" )
            continue

        playerHand = Hand[ playerInput ]

        print( f"CPU: {cpuHand.name}   Player: {playerHand.name}" )

        if playerHand is cpuHand:
            print( "Draw!" )
        elif playerHand is Hand.PAPER and cpuHand is Hand.SCISSORS:
            print( "CPU wins!" )
        elif playerHand is Hand.SCISSORS and cpuHand is Hand.ROCK:
            print( "CPU wins!" )
        elif playerHand is Hand.ROCK and cpuHand is Hand.PAPER:
            print( "CPU wins!" )
        else:
            wins =+ 1
            print( "Player Wins!" )

        games += 1

    if games != 0:
        print( f"Win percentage: {wins/games:.2%}" )


if __name__ == "__main__":
    main()