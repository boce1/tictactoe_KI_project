import pygame
from .constants import *

delay = 200

def display_winner(window):
    window.fill(BACKGROUND_COLOR)
    text = font_finish.render("You won", True, BLACK)
    window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(delay)

def display_loser(window):
    window.fill(BACKGROUND_COLOR)
    text = font_finish.render("You lost", True, BLACK)
    window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(delay)

def display_draw(window):
    window.fill(BACKGROUND_COLOR)
    text = font_finish.render("It's a draw", True, BLACK)
    window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(delay)
