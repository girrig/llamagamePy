'''
Created on Mar 12, 2013

@author: Brandon
'''

import pygame
import time
from math import *
import Animation


animations = {}
sounds = ''

class Player:
    def __init__(self, pos):
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.anim_frame = 0
        
        # dead = 0, awake = 1, asleep = 2
        self.state = 1
        self.energy = 100
        self.food = 100
        self.direction = 0  # 0 is north
        self.speed = 2

    def getAnimation(self, action):
        global animations
        try:
            return animations[action]
        except:
            animations = Animation.loadAnimations("human")
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
        try:
            angle = atan((food.y - self.y) / (food.x - self.x))
            self.direction = angle
        except:  # only happens if the objects line up pixel perfect
            self.direction = 0
        #Quadrant 1
        if(self.x < food.x and self.y < food.y):
                self.x += (self.speed * cos(angle))
                self.y += (self.speed * sin(angle))
                self.getAnimation("right_run.00" + str(self.anim_frame))
        #Quadrant 2
        if(self.x > food.x and self.y < food.y):
                self.x -= (self.speed * cos(angle))
                self.y -= (self.speed * sin(angle))
                self.getAnimation("left_run.00" + str(self.anim_frame))
        #Quadrant 3
        if(self.x > food.x and self.y > food.y):
                self.x -= (self.speed * cos(angle))
                self.y -= (self.speed * sin(angle))
                self.getAnimation("left_run.00" + str(self.anim_frame))
        #Quadrant 4
        if(self.x < food.x and self.y > food.y):
                self.x += (self.speed * cos(angle))
                self.y += (self.speed * sin(angle))
                self.getAnimation("right_run.00" + str(self.anim_frame))