'''
Created on Mar 12, 2013

@author: Brandon
'''

import pygame
import time
from math import *
import Fruit
import Animation


animations = {}
sounds = {}

class Animal:
    def __init__(self, pos):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.anim_frame = 0
        
        self.energy = 100
        self.food = 60
        self.quantity = 0
        
        # dead = 0, awake = 1, asleep = 2
        self.state = 1
        self.moving = False
        self.direction = 0  # 0 is north
        self.speed = 4
    
    
    def getAnimation(self, action):
        global animations
        try:
            return animations[action]
        except:
            animations = Animation.loadAnimations("animal")
            return animations[action]

    def getAnimationList(self):
        global animations
        return animations
    
    def update_anim(self):
        if self.anim_frame < 5:
            self.anim_frame += 1
        else:
            self.anim_frame = 0
        
    def moveto(self, food):
        self.moving = True
        try:
            angle = atan((food.pos_y - self.pos_y) / (food.pos_x - self.pos_x))
            self.direction = angle
        except:  # only happens if the objects line up pixel perfect
            self.direction = 0
        #Quadrant 1
        if(self.pos_x < food.pos_x and self.pos_y < food.pos_y):
                self.pos_x += (self.speed * cos(angle))
                self.pos_y += (self.speed * sin(angle))
        #Quadrant 2
        if(self.pos_x > food.pos_x and self.pos_y < food.pos_y):
                self.pos_x -= (self.speed * cos(angle))
                self.pos_y -= (self.speed * sin(angle))
        #Quadrant 3
        if(self.pos_x > food.pos_x and self.pos_y > food.pos_y):
                self.pos_x -= (self.speed * cos(angle))
                self.pos_y -= (self.speed * sin(angle))
        #Quadrant 4
        if(self.pos_x < food.pos_x and self.pos_y > food.pos_y):
                self.pos_x += (self.speed * cos(angle))
                self.pos_y += (self.speed * sin(angle))

    def findFood(self, foodlist):
        # initial setup
        shortestDistance = self.getdistance(foodlist[0])
        closestFood = foodlist[0]
        # finding closest food
        for each in foodlist:
            if(self.getdistance(each) < shortestDistance):
                shortestDistance = self.getdistance(each)
                closestFood = each
        return closestFood
            
    def getdistance(self, item):
        distance = sqrt(((item.pos_y - self.pos_y)**2) + ((item.pos_x - self.pos_x)**2))
        return distance



class Llama(Animal):
    animations = {}
    sounds = {}
    def __init__(self, pos):
        Animal.__init__(self, pos)
        self.quanity = 10
        
    
    def update(self, fruitlist):
        # they are not moving unless a condition sets them to moving
        self.moving = False
        
        if self.food <= 0:
            self.state = 0
        if self.energy < 0:
            self.state = 2
            
        if self.state == 1:
            self.energy = self.energy - .005
            self.food = self.food - .05
                
            if self.food < 50:
                try:
                    desiredfood = self.findFood(fruitlist)
                    self.moveto(desiredfood)
                    if(self.getdistance(desiredfood) < 10):
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
            pass
    
    def paint(self, screen):
        if self.moving:
            # draw the correct walking/running sprite from the animation object
            if ((self.direction > 315) or (self.direction < 45)):
                screen.blit(self.getAnimation('back_walk.00' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            elif ((self.direction > 135) and (self.direction < 225)):
                screen.blit(self.getAnimation('front_walk.00' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            elif ((self.direction >= 225) and (self.direction <= 315)):
                screen.blit(self.getAnimation('left_walk.00' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            elif ((self.direction >= 45) and (self.direction <= 135)):
                screen.blit(self.getAnimation('right_walk.00' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            self.update_anim()
        else:  # standing still
            self.anim_frame = 0
            if ((self.direction > 315) or (self.direction < 45)):
                screen.blit(self.getAnimation('_back_stand'), (self.pos_x, self.pos_y))
            elif ((self.direction > 135) and (self.direction < 225)):
                screen.blit(self.getAnimation('_front_stand'), (self.pos_x, self.pos_y))
            elif ((self.direction >= 225) and (self.direction <= 315)):
                screen.blit(self.getAnimation('_left_stand'), (self.pos_x, self.pos_y))
            elif ((self.direction >= 45) and (self.direction <= 135)):
                screen.blit(self.getAnimation('_right_stand'), (self.pos_x, self.pos_y))
        if self.state == 0:
            if ((self.direction > 315) or (self.direction < 45)):
                screen.blit(self.getAnimation('_back_dead'), (self.pos_x, self.pos_y))
            elif ((self.direction > 135) and (self.direction < 225)):
                screen.blit(self.getAnimation('_front_dead'), (self.pos_x, self.pos_y))
            elif ((self.direction >= 225) and (self.direction <= 315)):
                screen.blit(self.getAnimation('_left_dead'), (self.pos_x, self.pos_y))
            elif ((self.direction >= 45) and (self.direction <= 135)):
                screen.blit(self.getAnimation('_right_dead'), (self.pos_x, self.pos_y))
        
        
        
class Tiger(Animal):
    animations = {}
    sounds = {}
    def __init__(self, pos):
        Animal.__init__(self,pos)
        self.quantity = 20
        
    def update(self, meatlist):
        # they are not moving unless a condition sets them to moving
        self.moving = False
        
        if self.food <= 0:
            self.state = 0
        if self.energy < 0:
            self.state = 2
            
        if self.state == 1:
            self.energy = self.energy - .005
            self.food = self.food - .05
                
            if self.food < 50:
                try:
                    desiredfood = self.findFood(meatlist)
                    self.moveto(desiredfood)
                    if(self.getdistance(desiredfood) < 10):
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
            pass
            
    def paint(self, screen):
        if self.moving:
            # draw the correct walking/running sprite from the animation object
            if ((self.direction > 315) or (self.direction < 45)):
                screen.blit(self.getAnimation('back_walk.00' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            elif ((self.direction > 135) and (self.direction < 225)):
                screen.blit(self.getAnimation('front_walk.00' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            elif ((self.direction >= 225) and (self.direction <= 315)):
                screen.blit(self.getAnimation('left_walk.00' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            elif ((self.direction >= 45) and (self.direction <= 135)):
                screen.blit(self.getAnimation('right_walk.00' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            self.update_anim()
        else:  # standing still
            self.anim_frame = 0
            if ((self.direction > 315) or (self.direction < 45)):
                screen.blit(self.getAnimation('_back_stand'), (self.pos_x, self.pos_y))
            elif ((self.direction > 135) and (self.direction < 225)):
                screen.blit(self.getAnimation('_front_stand'), (self.pos_x, self.pos_y))
            elif ((self.direction >= 225) and (self.direction <= 315)):
                screen.blit(self.getAnimation('_left_stand'), (self.pos_x, self.pos_y))
            elif ((self.direction >= 45) and (self.direction <= 135)):
                screen.blit(self.getAnimation('_right_stand'), (self.pos_x, self.pos_y))
        if self.state == 0:
            if ((self.direction > 315) or (self.direction < 45)):
                screen.blit(self.getAnimation('_back_dead'), (self.pos_x, self.pos_y))
            elif ((self.direction > 135) and (self.direction < 225)):
                screen.blit(self.getAnimation('_front_dead'), (self.pos_x, self.pos_y))
            elif ((self.direction >= 225) and (self.direction <= 315)):
                screen.blit(self.getAnimation('_left_dead'), (self.pos_x, self.pos_y))
            elif ((self.direction >= 45) and (self.direction <= 135)):
                screen.blit(self.getAnimation('_right_dead'), (self.pos_x, self.pos_y))