'''
Created on Mar 12, 2013

@author: Brandon
'''

import time
from math import *
from Food import *

class Unit:
    def __init__(self):
        self.pos = (320, 240)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.currentImage = '48unitidleL.png'
        self.energy = 100
        self.food = 100
        self.speed = 4
        
    
    def frame(self, foodlist):
        #self.pos = self.pos.move(random.randint(-10,10), random.randint(-10,10))
        self.food = self.food - .05
        self.energy = self.energy - .005
        if  'L' in self.currentImage:
            self.currentImage = '48unitidleL.png'
        if  'R' in self.currentImage:
            self.currentImage = '48unitidleR.png'
        if self.food < 50:
            try:
                desiredfood = self.findFood(foodlist)
                self.moveto(desiredfood)
                if(self.getdistance(desiredfood) < 10):
                    self.food += desiredfood.quantity
                    foodlist.remove(desiredfood)
            except IndexError:
                return
        #if self.energy < 0:
            
        #=======================================================================
        # if self.pos.top < 0:
        #     self.pos.top = 0
        # if self.pos.left < 0:
        #     self.pos.left = 0
        # if self.pos.bottom > 480:
        #     self.pos.bottom = 480
        # if self.pos.right > 640:
        #     self.pos.right = 640
        #=======================================================================
        
    def moveto(self, food):
        #atan = arctan
        angle = atan((food.y - self.y) / (food.x - self.x))
        #Quadrant 1
        if(self.x < food.x and self.y < food.y):
                self.x += (self.speed * cos(angle))
                self.y += (self.speed * sin(angle))
                self.currentImage = '48unitR.png'
        #Quadrant 2
        if(self.x > food.x and self.y < food.y):
                self.x -= (self.speed * cos(angle))
                self.y -= (self.speed * sin(angle))
                self.currentImage = '48unitL.png'
        #Quadrant 3
        if(self.x > food.x and self.y > food.y):
                self.x -= (self.speed * cos(angle))
                self.y -= (self.speed * sin(angle))
                self.currentImage = '48unitL.png'
        #Quadrant 4
        if(self.x < food.x and self.y > food.y):
                self.x += (self.speed * cos(angle))
                self.y += (self.speed * sin(angle))
                self.currentImage = '48unitR.png'

        
        
    def findFood(self, foodlist):
        #initial setup
        shortestDistance = self.getdistance(foodlist[0])
        closestFood = foodlist[0]
        #finding closest food
        for each in foodlist:
            if(self.getdistance(each) < shortestDistance):
                shortestDistance = self.getdistance(each)
                closestFood = each
        return closestFood
            
    def getdistance(self, item):
        distance = sqrt(((item.y - self.y)**2) + ((item.x - self.x)**2))
        return distance