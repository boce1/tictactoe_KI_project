def is_win(player_sign, board):
    # Check rows
    for row in board.state:
        if all(cell == player_sign for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board.state[row][col] == player_sign for row in range(3)):
            return True

    # Check diagonals
    for i in range(3):
        if all(board.state[i][i] == player_sign for i in range(3)):
            return True
        if all(board.state[i][2 - i] == player_sign for i in range(3)):
            return True
        
    return False