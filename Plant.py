'''
Created on Sep 14, 2013

@author: Brandon
'''

from random import randint

class Plant:
    quantity = 1
    def __init__(self, pos):
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
class Grass(Plant):
    def __init__(self, pos):
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.color = (0, 224, 0)
    
    def getColor(self):
        return self.color