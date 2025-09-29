from .board_check import is_win

def evaluate(board, player_turn):
    # # #
    # if the player_turn is False -> the maximazing player is X
    # if the player_turn is True -> the maximazing player is O
    # # #
    maximazing_player = board.PLAYER_O if player_turn else board.PLAYER_X
    minimizing_player = board.PLAYER_X if player_turn else board.PLAYER_O

    if is_win(maximazing_player, board):
        return 10
    elif is_win(minimizing_player, board):
        return -10

    return 0