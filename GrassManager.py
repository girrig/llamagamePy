'''
Created on Nov 25, 2013

@author: Brandon
'''

from Plant import *

class GrassManager:
    def __init__(self):
        #list of all grass objects
        self.grasslist = []
        self.tgrasslist = []
        #a quick way to figure out if a grass object exists at a certain location
        #holds a grass object
        self.grass_lookup = {}

    def getGrasslist(self):
        return self.grasslist
    
    def updateGrasslist(self):
        for each in self.tgrasslist:
            self.grasslist.append(each)
        self.tgrasslist = []
    
    def createGrass(self, pos):
        g = Grass(pos)
        self.grass_lookup[str(g.x)+","+str(g.y)] = g
        self.grasslist.append(g)
    
    def frame(self, screenX, screenY, grassX, grassY):
        self.spread(screenX, screenY, grassX, grassY)
    
    def spread(self, screenX, screenY, grassX, grassY):
        if (grassY > 0):
            self.spreadN(grassX, grassY)
            if (grassX > 0):
                self.spreadW(grassX, grassY)
                self.spreadNW(grassX, grassY)
            if (grassX < screenX-1):
                self.spreadNE(grassX, grassY)
                self.spreadE(grassX, grassY)
        if (grassY < screenY-1):
            self.spreadS(grassX, grassY)
            if (grassX > 0):
                self.spreadSW(grassX, grassY)
            if (grassX < screenX-1):
                self.spreadSE(grassX, grassY)
    
    def spreadN(self, x, y):
        try:
            self.grass_lookup[str(x)+","+str(y-1)]
        except KeyError:
            g = Grass((x, y-1))
            self.grass_lookup[str(x)+","+str(y-1)] = g
            self.tgrasslist.append(g)
    
    def spreadNE(self, x, y):
        try:
            self.grass_lookup[str(x+1)+","+str(y-1)]
        except KeyError:
            g = Grass((x+1, y-1))
            self.grass_lookup[str(x+1)+","+str(y-1)] = g
            self.tgrasslist.append(g)
    
    def spreadE(self, x, y):
        try:
            self.grass_lookup[str(x+1)+","+str(y)]
        except KeyError:
            g = Grass((x+1, y))
            self.grass_lookup[str(x+1)+","+str(y)] = g
            self.tgrasslist.append(g)
    
    def spreadSE(self, x, y):
        try:
            self.grass_lookup[str(x+1)+","+str(y+1)]
        except KeyError:
            g = Grass((x+1, y+1))
            self.grass_lookup[str(x+1)+","+str(y+1)] = g
            self.tgrasslist.append(g)
    
    def spreadS(self, x, y):
        try:
            self.grass_lookup[str(x)+","+str(y+1)]
        except KeyError:
            g = Grass((x, y+1))
            self.grass_lookup[str(x)+","+str(y+1)] = g
            self.tgrasslist.append(g)
    
    def spreadSW(self, x, y):
        try:
            self.grass_lookup[str(x-1)+","+str(y+1)]
        except KeyError:
            g = Grass((x-1, y+1))
            self.grass_lookup[str(x-1)+","+str(y+1)] = g
            self.tgrasslist.append(g)
    
    def spreadW(self, x, y):
        try:
            self.grass_lookup[str(x-1)+","+str(y)]
        except KeyError:
            g = Grass((x-1, y))
            self.grass_lookup[str(x-1)+","+str(y)] = g
            self.tgrasslist.append(g)
    
    def spreadNW(self, x, y):
        try:
            self.grass_lookup[str(x-1)+","+str(y-1)]
        except KeyError:
            g = Grass((x-1, y-1))
            self.grass_lookup[str(x-1)+","+str(y-1)] = g
            self.tgrasslist.append(g)