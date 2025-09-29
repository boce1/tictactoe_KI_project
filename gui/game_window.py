from .constants import *
from minmax_utils import *

class Game_Window:
    def __init__(self, board=None):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic Tac Toe")

        self.row_width = WIDTH // 3
        self.col_height = HEIGHT // 3

        self.player_turn = False # False for PLAYER_X, True for PLAYER_O, TODO add fucntinon to switch sides
        self.turn = False # False for PLAYER_X, True for PLAYER_O

        self.board = board

    def choose_move(self, mouse_pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = mouse_pos
            if 0 <= x <= WIDTH and 0 <= y <= HEIGHT:
                col = x // self.row_width
                row = y // self.col_height

                if self.board.state[row][col] == self.board.EMPTY:
                    player = self.board.PLAYER_O if self.turn else self.board.PLAYER_X
                    self.board.insert_move(row, col, player)
                    self.turn = not self.turn

    def draw_board(self):
        self.window.fill((255, 255, 255))

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
        if not self.player_turn and is_win(self.board.PLAYER_X, self.board) or \
            self.player_turn and is_win(self.board.PLAYER_O, self.board): 
            # if the player is X and X wins or player is O and O wins
            print("You won!")
        if not self.player_turn and is_win(self.board.PLAYER_O, self.board) or \
            self.player_turn and is_win(self.board.PLAYER_X, self.board): 
            # if the player is X and X loses or player is O and O loses
            print("You lost!")
        
        if is_win(self.board.PLAYER_X, self.board) or is_win(self.board.PLAYER_O, self.board):
            self.board.reset()
            self.turn = False


    def loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                mouse_pos = pygame.mouse.get_pos()
                self.choose_move(mouse_pos, event)
            self.draw_board()
            self.finish()
            # row = int(input("Enter row (0-2): "))
            # col = int(input("Enter column (0-2): "))
            # player = input("Enter player (X/O): ").strip().upper()
            # try:
            #     board.insert_move(row, col, player)
            # except ValueError as e:
            #     print(e)
        pygame.quit()