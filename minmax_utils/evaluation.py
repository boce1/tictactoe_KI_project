from .board_check import is_win, is_full

score_two_signs = 1
score_two_sign_on_edges = 2

def evaluate(board, ai_player):
    # # #
    # if the player_turn is False -> the maximazing player is X
    # if the player_turn is True -> the maximazing player is O
    # # #
    maximazing_player = ai_player
    minimizing_player = board.PLAYER_O if ai_player == board.PLAYER_X else board.PLAYER_X

    # Check for terminal states
    score = 0
    
    main_diagonal = (board.state[0][0], board.state[1][1], board.state[2][2])
    anti_diagonal = (board.state[0][2], board.state[1][1], board.state[2][0])

    # evaluate the position where theres 2 signs
    for row in board.state:
        if row.count(maximazing_player) == 2 and row.count(board.EMPTY) == 1:
            score += score_two_signs
        if row.count(maximazing_player) == 2 and row.count(board.EMPTY) == 1:
            score -= score_two_signs

    for col in range(3):
        column = (board.state[0][col], board.state[1][col], board.state[2][col])
        if column.count(maximazing_player) == 2 and column.count(board.EMPTY) == 1:
            score += score_two_signs
        if column.count(minimizing_player) == 2 and column.count(board.EMPTY) == 1:
            score -= score_two_signs

    if main_diagonal.count(maximazing_player) == 2 and main_diagonal.count(board.EMPTY) == 1:
        score += score_two_signs
    if main_diagonal.count(minimizing_player) == 2 and main_diagonal.count(board.EMPTY) == 1:
        score -= score_two_signs
    
    if anti_diagonal.count(maximazing_player) == 2 and anti_diagonal.count(board.EMPTY) == 1:
        score += score_two_signs
    if anti_diagonal.count(minimizing_player) == 2 and anti_diagonal.count(board.EMPTY) == 1:
        score -= score_two_signs

    # evaluate the move where the player places its sign on the corners
    for row in board.state:
        if row[0] == row[2] == maximazing_player and row[1] == board.EMPTY:
            score += score_two_sign_on_edges
        if row[0] == row[2] == minimizing_player and row[1] == board.EMPTY:
            score -= score_two_sign_on_edges

    for col in range(3):
        column = (board.state[0][col], board.state[1][col], board.state[2][col])
        if column[0] == column[2] == maximazing_player and column[1] == board.EMPTY:
            score += score_two_sign_on_edges
        if column[0] == column[2] == minimizing_player and column[1] == board.EMPTY:
            score -= score_two_sign_on_edges

    if main_diagonal[0] == main_diagonal[2] == maximazing_player and main_diagonal[1] == board.EMPTY:
        score += score_two_sign_on_edges
    if main_diagonal[0] == main_diagonal[2] == minimizing_player and main_diagonal[1] == board.EMPTY:
        score -= score_two_sign_on_edges
    
    if anti_diagonal[0] == anti_diagonal[2] == maximazing_player and anti_diagonal[1] == board.EMPTY:
        score += score_two_sign_on_edges
    if anti_diagonal[0] == anti_diagonal[2] == minimizing_player and anti_diagonal[1] == board.EMPTY:
        score -= score_two_sign_on_edges

    return score