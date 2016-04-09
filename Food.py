'''
Created on Aug 25, 2013

@author: Brandon
'''

import pygame
import random


images = {}

class Food:
    def __init__(self, pos):
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.image = None
        self.quantity = 0
    
    def getImage(self):
        return self.image

class Apple(Food):
    images = {}
    def __init__(self, pos):
        Food.__init__(self, pos)
        self.image = pygame.image.load('images/apple/24apple.png')
        self.quantity = 15


class Pear(Food):
    images = {}
    def __init__(self, pos):
        Food.__init__(self, pos)
        self.image = pygame.image.load('images/pear/24pear.png')
        self.quantity = 15