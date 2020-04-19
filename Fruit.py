import pygame

images = {}


class Fruit:
    def __init__(self, pos):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.image = None
        self.quantity = 0

    def getImage(self):
        return self.image


class Apple(Fruit):
    images = {}

    def __init__(self, pos):
        Fruit.__init__(self, pos)
        self.image = pygame.image.load('images/apple/24apple.png')
        self.quantity = 15

    def update(self):
        pass


class Pear(Fruit):
    images = {}

    def __init__(self, pos):
        Fruit.__init__(self, pos)
        self.image = pygame.image.load('images/pear/24pear.png')
        self.quantity = 15

    def update(self):
        pass
