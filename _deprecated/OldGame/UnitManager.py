'''
Created on Dec 29, 2012

@author: Brandon
'''

from Unit import *
from PIL import Image, ImageTk

class UnitManager:
    def __init__(self):
        self.unit = Unit()

    
    
    #Everything is shifted by 180 degrees logically because the top of the window is 0 and as your variable increases the entity moves down
    def moveNorth(self):
        y = self.unit.getYLoc()
        self.unit.setYLoc(y - 1)
 
    def moveEast(self):
        x = self.unit.getXLoc()
        self.unit.setXLoc(x + 1)
        
    def moveSouth(self):
        y = self.unit.getYLoc()
        self.unit.setYLoc(y + 1)
        
    def moveWest(self):
        x = self.unit.getXLoc()
        self.unit.setXLoc(x - 1)
        
    def ResizeImage(self, image, size):
        img = ImageTk.PhotoImage(Image.open(image))
        return img
        #return image.resize((size,size), Image.ANTIALIAS)