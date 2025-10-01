from .constants import *
from .finish_screen import *
from minmax_utils import *
from math import inf
from random import shuffle

class Game_Window:
    def __init__(self, board=None):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic Tac Toe")

        self.row_width = WIDTH // 3
        self.col_height = HEIGHT // 3

        self.human_playing = True  # False for PLAYER_X, True for PLAYER_O, TODO add fucntinon to switch sides
        self.turn = False # False for PLAYER_X, True for PLAYER_O

        self.board = board

    def choose_move(self, mouse_pos, event):
        if self.human_playing == self.turn and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = mouse_pos
            if 0 <= x <= WIDTH and 0 <= y <= HEIGHT:
                col = x // self.row_width
                row = y // self.col_height

                if self.board.state[row][col] == self.board.EMPTY:
                    player = self.board.PLAYER_O if self.turn else self.board.PLAYER_X
                    self.board.insert_move(row, col, player)
                    self.turn = not self.turn

    def find_moves(self):
        moves = []
        even_cells = []
        odd_cells = []
        for r in range(3):
            for c in range(3):
                if self.board.state[r][c] == self.board.EMPTY:
                    if (r + c) % 2 == 0:
                        even_cells.append((r, c))
                    else:
                        odd_cells.append((r, c))
        shuffle(even_cells)
        shuffle(odd_cells)
        moves.extend(even_cells)
        moves.extend(odd_cells)        
        return moves

    def generate_move(self):
        if self.turn != self.human_playing:
            best_move = None
            best_score = -inf
            player = self.board.PLAYER_O if not self.human_playing else self.board.PLAYER_X

            for move in self.find_moves():
                r, c = move
                if self.board.state[r][c] == self.board.EMPTY:
                    self.board.insert_move(r, c, player)
                    score = minimax(self.board, 9, -inf, inf, False, player)
                    self.board.state[r][c] = self.board.EMPTY  # Undo move
                    if score > best_score:
                        best_score = score
                        best_move = (r, c)
            if best_move:
                self.board.insert_move(best_move[0], best_move[1], player)
                self.turn = not self.turn

    def draw_board(self):
        self.window.fill(BACKGROUND_COLOR)

        # Draw grid lines
        for i in range(1, 3):
            pygame.draw.line(self.window, (0, 0, 0), (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3), 5)
            pygame.draw.line(self.window, (0, 0, 0), (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT), 5)

        # Draw X and O
        for r in range(3):
            for c in range(3):
                if self.board.state[r][c] != self.board.EMPTY:
                    color = RED if self.board.state[r][c] == self.board.PLAYER_X else GREEN
                    text = font_players.render(self.board.state[r][c], True, color)
                    x = (c * self.row_width) + self.row_width // 2 - text.get_width() // 2
                    y = (r * self.col_height) + self.col_height // 2 - text.get_height() // 2
                    self.window.blit(text, (x, y))

        pygame.display.update()

    def finish(self):
        if not self.human_playing and is_win(self.board.PLAYER_X, self.board) or \
            self.human_playing and is_win(self.board.PLAYER_O, self.board): 
            # if the player is X and X wins or player is O and O wins
            # print("You won!")
            display_winner(self.window)
        if not self.human_playing and is_win(self.board.PLAYER_O, self.board) or \
            self.human_playing and is_win(self.board.PLAYER_X, self.board): 
            # if the player is X and X loses or player is O and O loses
            # print("You lost!")
            display_loser(self.window)

        if is_win(self.board.PLAYER_X, self.board) or is_win(self.board.PLAYER_O, self.board):
            self.board.reset()
            self.turn = False
        if is_full(self.board):
            # print("It's a draw!")
            self.board.reset()
            self.turn = False

            display_draw(self.window)


    def loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                mouse_pos = pygame.mouse.get_pos()
                self.choose_move(mouse_pos, event)
            self.generate_move()
            self.draw_board()
            self.finish()
        pygame.quit()