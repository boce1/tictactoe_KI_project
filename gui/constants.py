import pygame
pygame.init()
pygame.font.init()

# Constants for the game
WIDTH, HEIGHT = 510, 510
BAR = 75
HEIGHT_WITH_BAR = HEIGHT + BAR
font_players = pygame.font.SysFont('Comic Sans MS', WIDTH // 5)
font_finish = pygame.font.SysFont('Comic Sans MS', WIDTH // 10)
font_score = pygame.font.SysFont('Comic Sans MS', WIDTH // 30)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)

BACKGROUND_COLOR = WHITE

FPS = 60

GAP = 5
FINISH_DELAY = 400