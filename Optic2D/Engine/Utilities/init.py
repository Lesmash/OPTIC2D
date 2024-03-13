import pygame
from configparser import ConfigParser
from Engine.Rendering.shapes import Shapes
from Engine.Rendering.sprite import SpriteRenderer
from Engine.Utilities.input import InputHandler

class Game:
    def __init__(self, config_file):
        pygame.init()

        config = ConfigParser()
        config.read(config_file)

        self.input = InputHandler()

        self.width = int(config.get('Screen', 'WIDTH'))
        self.height = int(config.get('Screen', 'HEIGHT'))
        self.title = str(config.get('Screen', 'TITLE'))
        self.bg_color = (
            int(config.get('Screen', 'BACKGROUND_R')),
            int(config.get('Screen', 'BACKGROUND_G')),
            int(config.get('Screen', 'BACKGROUND_B'))
        )

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.shapes = Shapes(self.screen)
        self.running = True

        # self.sprite = SpriteRenderer('./Engine/Assets/cat.png', (150, 150))

    def run(self):
        while self.running:
            self.input.handle_events()
            self.update()
            self.render()
                
        pygame.quit()

    def update(self):
        # if self.input.is_key_pressed('w'):
        #     self.sprite.rect.y -= 1
        # if self.input.is_key_pressed('s'):
        #     self.sprite.rect.y += 1
        # if self.input.is_key_pressed('d'):
        #     self.sprite.rect.x += 1
        # if self.input.is_key_pressed('a'):
        #     self.sprite.rect.x -= 1
        ...

    def render(self):
        self.screen.fill(self.bg_color)

        # self.sprite.draw(self.screen)

        self.shapes.draw_rectangle((255, 0, 0), (100, 100, 50, 50))
        self.shapes.draw_circle((0, 0, 255), (200, 200), 30)

        pygame.display.flip()
