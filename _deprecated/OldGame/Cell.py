'''
Created on Aug 6, 2012

@author: Brandon
'''

#import pygame.image

class Cell:
    def __init__(self):
        self.position = None
        self.north = None
        self.east = None
        self.south = None
        self.west = None
        self.x = None
        self.y = None
        self.display = False