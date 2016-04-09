'''
Created on Mar 12, 2013

@author: Brandon
'''

class Player:
    def __init__(self):
        self.x_loc = 0
        self.y_loc = 0
        self.name = "player" #user entered eventually
        
        #called photo instead of image to prevent confusion
        self.photo = "tile_test.jpg" #temp photo
    
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