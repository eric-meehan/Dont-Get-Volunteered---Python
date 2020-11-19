"""
 Eric Meehan
 2020-11-19
 Don't Get Volunteered
"""

from ChessBoard import ChessBoard
from Knight import Knight
import sys

def main():
    # The user may define the dimensions of the board, source position, and destination as arguments
    if len(sys.argv) > 1:
        try:
            # Get the board Length from the first argument
            Length = int(sys.argv[1])
            # Get the board Width from the second argument
            Width = int(sys.argv[2])
            # Get the Source from the third argument
            Source = int(sys.argv[3])
            # Get the Destination from the fourth argument
            Destination = int(sys.argv[4])
        except:
            print("Invalid input")
    else:
        # Alternatively, an 8x8 board will be used with a default Source of 0 and Destination of 1
        Length = 8
        Width = 8
        Source = 0
        Destination = 1
    # Define the ChessBoard
    Board = ChessBoard(Length, Width)
    # Instantiate the Knight
    knight = Knight(Source)
    # Generate a tree of possible moves until the destination is reached
    while knight != Destination:
        knight.ExplorePossibleMoves(Board)
    print(knight.MovesMade)

main()
