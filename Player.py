import time
from math import *

import pygame

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

    # Draw the correct walking/running sprite from the animation object
    def paint(self, screen):
        if self.moveUp or self.moveDown or self.moveLeft or self.moveRight:
            if self.direction == 'up':
                screen.blit(self.getAnimation('walk_up_0' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            elif self.direction == 'down':
                screen.blit(self.getAnimation('walk_down_0' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            elif self.direction == 'left':
                screen.blit(self.getAnimation('walk_left_0' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            elif self.direction == 'right':
                screen.blit(self.getAnimation('walk_right_0' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            self.update_anim()
        else:  # Idle
            if self.direction == 'up':
                screen.blit(self.getAnimation('idle_up_0' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            elif self.direction == 'down':
                screen.blit(self.getAnimation('idle_down_0' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            elif self.direction == "left":
                screen.blit(self.getAnimation('idle_left_0' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            elif self.direction == "right":
                screen.blit(self.getAnimation('idle_right_0' + str(self.anim_frame)), (self.pos_x, self.pos_y))
            self.update_anim()
