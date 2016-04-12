'''
Created on Mar 12, 2013

@author: Brandon
'''

import pygame
import time
from math import *
import Animation


animations = {}
sounds = {}

class Player:
    def __init__(self, pos):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.anim_frame = 0
        
        self.energy = 100
        self.food = 100
        self.quanity = 100
        
        # dead = 0, awake = 1, asleep = 2
        self.state = 1
        self.moveUp = self.moveDown = self.moveLeft = self.moveRight = False
        self.direction = 'down'
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
    
    def update(self):
        if self.moveUp:
            self.pos_y -= self.speed
        if self.moveDown:
            self.pos_y += self.speed
        if self.moveLeft:
            self.pos_x -= self.speed
        if self.moveRight:
            self.pos_x += self.speed
    
    def paint(self, screen):
        if self.moveUp or self.moveDown or self.moveLeft or self.moveRight:  # moving
            # draw the correct walking/running sprite from the animation object
            if self.direction == 'up':
                screen.blit(self.getAnimation('back_walk.00' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            elif self.direction == 'down':
                screen.blit(self.getAnimation('front_walk.00' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            elif self.direction == 'left':
                screen.blit(self.getAnimation('left_walk.00' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            elif self.direction == 'right':
                screen.blit(self.getAnimation('right_walk.00' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            self.update_anim()
        else:  # standing still
            self.anim_frame = 0
            if self.direction == 'up':
                screen.blit(self.getAnimation('_back_stand'), (self.pos_x, self.pos_y))
            elif self.direction == 'down':
                screen.blit(self.getAnimation('_front_stand'), (self.pos_x, self.pos_y))
            elif self.direction == "left":
                screen.blit(self.getAnimation('_left_stand'), (self.pos_x, self.pos_y))
            elif self.direction == "right":
                screen.blit(self.getAnimation('_right_stand'), (self.pos_x, self.pos_y))