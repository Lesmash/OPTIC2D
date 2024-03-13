from Engine.Rendering.sprite import *

class Player:
    def __init__(self, name, money, age):
        self.name = name
        self.money = money
        self.age = age

        self.sprite = SpriteRenderer('./Engine/Assets/cat.png', (150, 150))

    def draw(self, screen):
        self.sprite.draw(screen)