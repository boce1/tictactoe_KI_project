class Board:
    def __init__(self):
        self.PLAYER_X = "X"
        self.PLAYER_O = "O"
        self.EMPTY = " "

        self.state = [[self.EMPTY for _ in range(3)] for _ in range(3)]
    
    def insert_move(self, row, col, player):
        if player not in [self.PLAYER_X, self.PLAYER_O]:
            raise ValueError("Invalid player")
        if row < 0 or row >= 3 or col < 0 or col >= 3:
            raise ValueError("Invalid cell position ({}, {})".format(row, col))
        if self.state[row][col] != self.EMPTY:
            raise ValueError("Cell already occupied")
        
        self.state[row][col] = player

    def reset(self):
        self.state = [[self.EMPTY for _ in range(3)] for _ in range(3)]

    def print(self):
        # debug print
        print("-------------") 
        for row in self.state:
            print("|", end=" ")
            print(" | ".join(row), end=" |\n")
            print("-------------") 