from Engine.Utilities.init import *
from player import Player  






if __name__ == '__main__':

    game = Game('./Engine/config.cfg')
    game.run()

    p = Player('Juke', 42, 16)
    p.draw(game.screen)