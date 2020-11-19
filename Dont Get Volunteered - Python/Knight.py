"""
 Eric Meehan
 2020-11-19
 
 Class representation of a knight
 """

class Knight():
    def __init__(self, Source):
        # Initialize the knight with a starting position
        # CurrentPosition represents all of the possible current positions, so it is initialized as an array
        self.CurrentPosition = [Source]
        # Store the number of moves made by the piece
        self.MovesMade = 0
        
    def __ne__(self, Destination):
        # Performs a binary search on CurrentPosition for the Destination
        First = 0
        Last = len(self.CurrentPosition) - 1
        while First <= Last:
            Middle = int((First + Last) / 2)
            if self.CurrentPosition[Middle] == Destination:
                return False
            elif self.CurrentPosition[Middle] > Destination:
                Last = Middle - 1
            else:
                First = Middle + 1
        return True

    def ExplorePossibleMoves(self, Board):
        # Uses the CurrentPosition list to find possible moves
        # Duplicate CurrentPosition to allow that list to be manipulated
        SourcePosition = self.CurrentPosition
        # Empty CurrentPosition
        self.CurrentPosition = []
        # Iterate over the CurrentPosition list
        for each in SourcePosition:
            coordinates = Board.CoordinatePosition(each)
            if (Board.IsOnBoard(coordinates[0] + 1, coordinates[1] + 2)):
                self.CurrentPosition.append(Board.NumericPosition(coordinates[0] + 1, coordinates[1] + 2))
            if (Board.IsOnBoard(coordinates[0] + 1, coordinates[1] - 2)):
                self.CurrentPosition.append(Board.NumericPosition(coordinates[0] + 1, coordinates[1] - 2))
            if (Board.IsOnBoard(coordinates[0] - 1, coordinates[1] - 2)):
                self.CurrentPosition.append(Board.NumericPosition(coordinates[0] - 1, coordinates[1] - 2))
            if (Board.IsOnBoard(coordinates[0] - 1, coordinates[1] + 2)):
                self.CurrentPosition.append(Board.NumericPosition(coordinates[0] - 1, coordinates[1] + 2))
            if (Board.IsOnBoard(coordinates[0] + 2, coordinates[1] + 1)):
                self.CurrentPosition.append(Board.NumericPosition(coordinates[0] + 2, coordinates[1] + 1))
            if (Board.IsOnBoard(coordinates[0] + 2, coordinates[1] - 1)):
                self.CurrentPosition.append(Board.NumericPosition(coordinates[0] + 2, coordinates[1] - 1))
            if (Board.IsOnBoard(coordinates[0] - 2, coordinates[1] - 1)):
                self.CurrentPosition.append(Board.NumericPosition(coordinates[0] - 2, coordinates[1] - 1))
            if (Board.IsOnBoard(coordinates[0] - 2, coordinates[1] + 1)):
                self.CurrentPosition.append(Board.NumericPosition(coordinates[0] - 2, coordinates[1] + 1))
        # Sort the CurrentPosition list
        self.SortCurrentPosition()
        # Increment MovesMade
        self.MovesMade += 1
                
    def SortCurrentPosition(self):
        # Use a bubble sort to organize CurrentPosition
        for i in range(len(self.CurrentPosition)):
            for n in range(len(self.CurrentPosition) - i - 1):
                if self.CurrentPosition[n] > self.CurrentPosition[n + 1]:
                    temp = self.CurrentPosition[n]
                    self.CurrentPosition[n] = self.CurrentPosition[n + 1]
                    self.CurrentPosition[n + 1] = temp

    
