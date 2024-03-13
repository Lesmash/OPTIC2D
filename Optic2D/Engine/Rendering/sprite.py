import pygame

class SpriteRenderer:
    def __init__(self, image_path: str, position: int):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)