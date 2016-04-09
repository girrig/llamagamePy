'''
Created on Aug 25, 2013

@author: Brandon
'''

import pygame
import random


class Food:
    def __init__(self, pos):
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.image = None
        self.quantity = 0
    
    def getImage(self):
        return self.image
        
class Pear(Food):
    def __init__(self, pos):
        Food.__init__(self, pos)
        self.image = pygame.image.load('24pear.png')
        self.quantity = 15
        
class RottenPear(Food):
    def __init__(self, pos):
        Food.__init__(self, pos)
        self.image = pygame.image.load('24pearrotten.png')
        self.quantity = -15
    
    