def is_win(player_sign, board):
    # Check rows
    for row in board.state:
        if row[0] == row[1] == row[2] == player_sign:
            return True

    # Check columns
    for col in range(3):
        column = (board.state[0][col], board.state[1][col], board.state[2][col])
        if column[0] == column[1] == column[2] == player_sign:
            return True

    # Check diagonals
    if board.state[0][0] == board.state[1][1] == board.state[2][2] == player_sign:
        return True
    if board.state[0][2] == board.state[1][1] == board.state[2][0] == player_sign:
        return True
        
    return False

def is_full(board):
    for row in board.state:
        for cell in row:
            if cell == board.EMPTY:
                return False
    return True

