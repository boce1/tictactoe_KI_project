from minmax_utils import *
from board import Board
from gui import *

def main():
    b = Board()
    game_window = Game_Window(b)
    game_window.loop()

if __name__ == "__main__":
    main()