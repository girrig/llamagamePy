'''
Created on Mar 12, 2013

@author: Brandon
'''

import pygame
import time
from math import *
from Food import *

class Animal:
    image = None
    imageRect = None
    sound = ''
    #dead = 0, awake = 1, asleep = 2
    state = 1
    energy = 100
    food = 50
    direction = 0  #0 is north
    speed = 4
    quantity = 20  #how much food it's worth
    def __init__(self, pos):
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]

    def getRect(self):
        return self.imageRect
    
    def getImage(self):
        return self.image
        
    def moveto(self, food):
        try:
            #atan = arctan
            angle = atan((food.y - self.y) / (food.x - self.x))
            self.direction = angle
        except: # only happens if the objects line up pixel perfect
            self.direction = 0
        #Quadrant 1
        if(self.x < food.x and self.y < food.y):
                self.x += (self.speed * cos(angle))
                self.y += (self.speed * sin(angle))
                self.image = pygame.image.load('48llamaR.png')
        #Quadrant 2
        if(self.x > food.x and self.y < food.y):
                self.x -= (self.speed * cos(angle))
                self.y -= (self.speed * sin(angle))
                self.image = pygame.image.load('48llamaL.png')
        #Quadrant 3
        if(self.x > food.x and self.y > food.y):
                self.x -= (self.speed * cos(angle))
                self.y -= (self.speed * sin(angle))
                self.image = pygame.image.load('48llamaL.png')
        #Quadrant 4
        if(self.x < food.x and self.y > food.y):
                self.x += (self.speed * cos(angle))
                self.y += (self.speed * sin(angle))
                self.image = pygame.image.load('48llamaR.png')

        
        
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



class Llama(Animal):
    def __init__(self, pos):
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.image = pygame.image.load('48llamaidleL.png')
        self.sound = 'llamasound.wav'
        self.left = True
        
    def frame(self, fruitlist):
        #self.pos = self.pos.move(random.randint(-10,10), random.randint(-10,10))
        if self.food <= 0:
            self.state = 0
        if self.energy < 0:
            self.state = 2
            
        if self.state == 1:
            self.energy = self.energy - .005
            self.food = self.food - .05
            if self.left == True:
                self.image = pygame.image.load('48llamaidleL.png')
            if self.left != True:
                self.image = pygame.image.load('48llamaidleR.png')
                
            if self.food < 50:
                try:
                    desiredfood = self.findFood(fruitlist)
                    self.moveto(desiredfood)
                    if(self.getdistance(desiredfood) < 10):
                        (pygame.mixer.Sound(self.sound)).play()
                        self.food += desiredfood.quantity
                        fruitlist.remove(desiredfood)
                except IndexError:
                    return
                
        elif self.state == 2:
            self.energy = self.energy + .1
            self.food = self.food - .05
            if self.energy >= 100:
                self.state = 1
                
        elif self.state == 0:
            self.image = pygame.image.load("48llamadeadL.png")
        
        
        
class Tiger(Animal):
    def __init__(self, pos):
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.currentImage = pygame.image.load('48tigeridleL.png')
        self.sound = 'tigersound.mp3'

        
    def frame(self, meatlist):
        #self.pos = self.pos.move(random.randint(-10,10), random.randint(-10,10))
        if self.food <= 0:
            self.state = 0
        if self.energy < 0:
            self.state = 2
            
        if self.state == 1:
            self.energy = self.energy - .005
            self.food = self.food - .05
            if  'L' in self.image:
                self.image = pygame.image.load('48tigeridleL.png')
            if  'R' in self.image:
                self.image = pygame.image.load('48tigeridleL.png')
                
            if self.food < 50:
                try:
                    desiredfood = self.findFood(meatlist)
                    self.moveto(desiredfood)
                    if(self.getdistance(desiredfood) < 10):
                        (pygame.mixer.Sound(self.sound)).play()
                        self.food += desiredfood.quantity
                        meatlist.remove(desiredfood)
                except IndexError:
                    return
                
        elif self.state == 2:
            self.energy = self.energy + .1
            self.food = self.food - .05
            if self.energy >= 100:
                self.state = 1
                
        elif self.state == 0:
            self.image = pygame.image.load("48tigerdeadL.png")