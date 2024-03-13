import pygame

class Shapes:
    def __init__(self, screen):
        self.screen = screen

    def draw_rectangle(self, color, rect):
        pygame.draw.rect(self.screen, color, rect)

    def draw_circle(self, color, position, radius):
        pygame.draw.circle(self.screen, color, position, radius)