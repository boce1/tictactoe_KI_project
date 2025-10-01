import pygame
from .constants import *

class Button:
    def __init__(self, x, y, width, height, border_color = BLACK, color = WHITE, presed_color = GRAY, display_text = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_color = border_color
        self.color = color
        self.presed_color = presed_color
        self.actual_color = color
        self.display_text = display_text
        self.render_text = font_score.render(display_text, True, BLACK) if display_text else None

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, self.border_color, (self.x, self.y, self.width, self.height), 1)
        win.blit(self.render_text, (self.x + self.width // 2 - self.render_text.get_width() // 2, self.y + self.height // 2 - self.render_text.get_height() // 2))

    def is_mouse_in(self, mouse_pos):
        if(self.x <= mouse_pos[0] <= self.x + self.width and
           self.y <= mouse_pos[1] <= self.y + self.height):
            return True
        return False

    def is_mouse_pressed(self, mouse_pressed): # for coloring
        if mouse_pressed[0]:
            return True
        return False
    
    def is_pressed(self, mouse_pos, mouse_pressed):
        if self.is_mouse_in(mouse_pos) and self.is_mouse_pressed(mouse_pressed):
            self.color = self.presed_color
        else:
            self.color = self.actual_color

    def is_clicked(self, event, mouse_pos): # for event handling
        if self.is_mouse_in(mouse_pos):
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                return True
        return False