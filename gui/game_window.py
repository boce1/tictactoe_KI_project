from .constants import *
from .finish_screen import *
from .button import *
from minmax_utils import *
from math import inf
from random import shuffle

class Game_Window:
    def __init__(self, board=None):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT_WITH_BAR))
        pygame.display.set_caption("Tic Tac Toe")

        self.col_width = WIDTH // 3
        self.row_height = HEIGHT // 3

        self.human_playing = False  # False for PLAYER_X, True for PLAYER_O, TODO add fucntinon to switch sides
        self.turn = False # False for PLAYER_X, True for PLAYER_O

        self.board = board

        self.human_player_score = 0
        self.ai_player_score = 0
        self.draw_score = 0

        button_width = 100
        button_height = 30
        self.change_side_button = Button(WIDTH - button_width - GAP, HEIGHT + (BAR - button_height) // 2, button_width, button_height, display_text = "Change side")

    def choose_move(self, mouse_pos, event):
        if self.human_playing == self.turn and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = mouse_pos
            if 0 < x < WIDTH and 0 < y < HEIGHT:
                col = x // self.col_width
                row = y // self.row_height

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
            pygame.draw.line(self.window, BLACK, (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3), 5)
            pygame.draw.line(self.window, BLACK, (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT), 5)

        # Draw X and O
        for r in range(3):
            for c in range(3):
                if self.board.state[r][c] != self.board.EMPTY:
                    color = RED if self.board.state[r][c] == self.board.PLAYER_X else GREEN
                    text = font_players.render(self.board.state[r][c], True, color)
                    x = (c * self.col_width) + self.col_width // 2 - text.get_width() // 2
                    y = (r * self.row_height) + self.row_height // 2 - text.get_height() // 2
                    self.window.blit(text, (x, y))
        self.draw_bar()

    def draw_bar(self):
        pygame.draw.rect(self.window, BLACK, (0, HEIGHT, WIDTH, BAR), 2)
        human_score_text = font_score.render(f"|Human: {self.human_player_score}|", True, BLACK)
        ai_score_text = font_score.render(f"|AI: {self.ai_player_score}|", True, BLACK)
        draw_score_text = font_score.render(f"|Draws: {self.draw_score}|", True, BLACK)
        if self.human_playing:
            playing_sign = font_score.render("|You are O|", True, GREEN)
        else:
            playing_sign = font_score.render("|You are X|", True, RED)

        self.window.blit(human_score_text, (GAP, HEIGHT + (BAR - human_score_text.get_height()) // 2))
        self.window.blit(ai_score_text, (3*GAP + human_score_text.get_width(), HEIGHT + (BAR - ai_score_text.get_height()) // 2))
        self.window.blit(draw_score_text, (5*GAP + human_score_text.get_width() + ai_score_text.get_width(), HEIGHT + (BAR - draw_score_text.get_height()) // 2))
        self.window.blit(playing_sign, (11*GAP + human_score_text.get_width() + ai_score_text.get_width() +\
                                        draw_score_text.get_width(), HEIGHT + (BAR - playing_sign.get_height()) // 2))

    def draw_winning_line(self):
        y = self.row_height // 2 
        for row in self.board.state:
            if row[0] == row[1] == row[2] and row[0] != self.board.EMPTY:
                pygame.draw.line(self.window, BLACK, (self.col_width // 2, y), (WIDTH - self.col_width // 2, y), 5)
            y += self.row_height

        # Check columns
        x = self.col_width // 2
        for col in range(3):
            column = (self.board.state[0][col], self.board.state[1][col], self.board.state[2][col])
            if column[0] == column[1] == column[2] and column[0] != self.board.EMPTY:
                pygame.draw.line(self.window, BLACK, (x, self.row_height // 2), (x, HEIGHT - self.row_height // 2), 5)
            x += self.col_width
    
        # Check diagonals
        if self.board.state[0][0] == self.board.state[1][1] == self.board.state[2][2] and self.board.state[0][0] != self.board.EMPTY:
            pygame.draw.line(self.window, BLACK, (self.col_width // 2, self.row_height // 2), (WIDTH - self.col_width // 2, HEIGHT - self.row_height // 2), 5)
        if self.board.state[0][2] == self.board.state[1][1] == self.board.state[2][0] and self.board.state[0][2] != self.board.EMPTY:
            pygame.draw.line(self.window, BLACK, (WIDTH - self.col_width // 2, self.row_height // 2), (self.col_width // 2, HEIGHT - self.row_height // 2), 5)

        pygame.display.update()
        pygame.time.wait(FINISH_DELAY)

    def finish(self):
        if (not self.human_playing and is_win(self.board.PLAYER_X, self.board)) or \
            (self.human_playing and is_win(self.board.PLAYER_O, self.board)): 
            # if the player is X and X wins or player is O and O wins
            self.human_player_score += 1
            display_winner(self.window)
            self.draw_bar()
            self.change_side_button.draw(self.window)
            pygame.display.update()
            pygame.time.wait(FINISH_DELAY)

        if (not self.human_playing and is_win(self.board.PLAYER_O, self.board)) or \
            (self.human_playing and is_win(self.board.PLAYER_X, self.board)): 
            # if the player is X and X loses or player is O and O loses
            self.ai_player_score += 1
            self.draw_winning_line()
            display_loser(self.window)
            self.draw_bar()
            self.change_side_button.draw(self.window)
            pygame.display.update()
            pygame.time.wait(FINISH_DELAY)

        if is_win(self.board.PLAYER_X, self.board) or is_win(self.board.PLAYER_O, self.board):
            self.board.reset()
            self.turn = False


        if is_full(self.board):
            self.board.reset()
            self.turn = False
            self.draw_score += 1
            display_draw(self.window)
            self.draw_bar()
            self.change_side_button.draw(self.window)
            pygame.display.update()
            pygame.time.wait(FINISH_DELAY)

    def loop(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(FPS)
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.choose_move(mouse_pos, event)
                if self.change_side_button.is_clicked(event, mouse_pos):
                    self.human_playing = not self.human_playing
                    self.board.reset()
                    self.turn = False

            self.generate_move()
            self.draw_board()
            self.finish()

            self.change_side_button.draw(self.window)
            self.change_side_button.is_pressed(mouse_pos, pygame.mouse.get_pressed())

            pygame.display.update()

        pygame.quit()