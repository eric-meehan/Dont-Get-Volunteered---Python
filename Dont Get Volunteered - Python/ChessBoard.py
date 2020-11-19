"""
 Eric Meehan
 2020-11-18
 
 Class representation of a chess board that can be of any size
 """
 
 class ChessBoard():
    __init__(self, Length, Width):
        # Initialize a chess board to the provided length and width
        self.Length = Length
        self.Width = Width
        self.Board = [[n + (n * i) for n in range(Width)] for i in range (Length)]
        
    def NumericPosition(x, y):
        # Converts coordinates to a numeric position
        return self.Board[y][x]
    
    def CoordinatePosition(x):
        # Converts a numeric position to coordinates
        for i in range(self.Length):
            for n in range(self.Width):
                if self.Board[i][n] == x:
                    return (n, y)
                    
    def IsOnBoard(x, y):
        return x >= 0 and x < self.Width and y >= 0 and y < self.Length
