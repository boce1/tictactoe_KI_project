from .evaluation import evaluate
from .board_check import is_win, is_full
from math import inf

def minimax(board, depth, is_maximizing, ai_player):
    human_player = board.PLAYER_O if ai_player == board.PLAYER_X else board.PLAYER_X

    if is_win(ai_player, board):
        return inf
    if is_win(human_player, board):
        return -inf
    if is_full(board):
        return 0  # Draw
    if depth == 0:
        return evaluate(board, ai_player)
    
    if is_maximizing:
        best_score = -inf
        for r in range(3):
            for c in range(3):
                if board.state[r][c] == board.EMPTY:
                    board.insert_move(r, c, ai_player)
                    score = minimax(board, depth - 1, False, ai_player)
                    board.state[r][c] = board.EMPTY  # Undo move
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = inf
        for r in range(3):
            for c in range(3):
                if board.state[r][c] == board.EMPTY:
                    board.insert_move(r, c, human_player)
                    score = minimax(board, depth - 1, True, ai_player)
                    board.state[r][c] = board.EMPTY  # Undo move
                    best_score = min(score, best_score)
        return best_score