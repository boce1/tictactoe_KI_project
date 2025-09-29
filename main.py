from minmax_utils import *
from board import Board
from gui import *

def main():
    b = Board()
    #b.print()
    #b.insert_move(0, 2, b.PLAYER_O)
    #b.print()

    game_window = Game_Window(b)
    game_window.loop()

if __name__ == "__main__":
    main()