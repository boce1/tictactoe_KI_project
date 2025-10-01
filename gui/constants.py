import pygame
pygame.init()
pygame.font.init()

# Constants for the game
WIDTH, HEIGHT = 600, 600
font_players = pygame.font.SysFont('Comic Sans MS', WIDTH // 5)
font_finish = pygame.font.SysFont('Comic Sans MS', WIDTH // 10)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BACKGROUND_COLOR = WHITE

FPS = 60