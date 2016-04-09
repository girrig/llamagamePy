'''
Created on Sep 13, 2012

@author: Brandon
'''

import Tkinter as tk
#import pygame.image



class Unit:
    def __init__(self):
        self.x_loc = 0
        self.y_loc = 0
        self.name = "player"
        
        
        self.photo = "tile_test.jpg"
    
    def getXLoc(self):
        return self.x_loc
    
    def getYLoc(self):
        return self.y_loc
    
    def setXLoc(self, value):
        self.x_loc = value
    
    def setYLoc(self, value):
        self.y_loc = value
    
    def getPhoto(self):
        return self.photo
    
    def setPhoto(self, image):
        self.photo = image
        
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name