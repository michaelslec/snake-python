import random
from game import Game

class Apple():
    def __init__(self):
        self.setNewLocation()
    
    def setNewLocation(self):
        self.x = random.randint(0, Game.CELLWIDTH - 1)
        self.y = random.randint(0, Game.CELLHEIGHT - 1)
        