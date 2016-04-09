'''
Created on Feb 10, 2013

@author: Brandon
'''

import pygame
from pygame.locals import *
import pyganim
from Player import Player
from Animal import Llama, Tiger
from Food import Apple, Pear
import math
import time


class World():
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Llama Simulator 3000: Alpha v0.005')

        self.lightgreen = pygame.Color(130, 255, 130)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)
        self.white = pygame.Color(255, 255, 255)
        self.black = pygame.Color(0, 0, 0)
        
        #mouse
        self.mouseX, self.mouseY = 0, 0

        self.fontObj = pygame.font.Font('freesansbold.ttf', 18)

        # lists of all things on the screen
        self.fruitlist = []
        self.llamalist = []
        
        
        # Player
        self.player = Player((self.width/2, self.height/2))
        self.direction = 'down'
        self.moveUp = self.moveDown = self.moveLeft = self.moveRight = False
        
        # Move Conductor
        self.conductorlist = []
        self.conductorlist.append(self.player.getAnimationList())
        self.moveConductor = pyganim.PygConductor(self.conductorlist)
        
        # Loop
        self.done = False

    def draw(self):
        self.screen.fill(self.lightgreen)
        # update map

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEMOTION:
                self.mouseX, self.mouseY = event.pos
            elif event.type == MOUSEBUTTONUP:
                continue  # maybe a movement action?
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == K_UP:
                    self.moveUp = True
                    self.moveDown = False
                    if not self.moveLeft and not self.moveRight:
                        # only change the direction to up if the player wasn't moving left/right
                        self.direction = 'up'
                elif event.key == K_DOWN:
                    self.moveDown = True
                    self.moveUp = False
                    if not self.moveLeft and not self.moveRight:
                        self.direction = 'down'
                elif event.key == K_LEFT:
                    self.moveLeft = True
                    self.moveRight = False
                    if not self.moveUp and not self.moveDown:
                        self.direction = 'left'
                elif event.key == K_RIGHT:
                    self.moveRight = True
                    self.moveLeft = False
                    if not self.moveUp and not self.moveDown:
                        self.direction = 'right'
                elif event.key == K_c:  # clears everything
                    i = 0
                    length = len(self.fruitlist)
                    while i < length:
                        self.fruitlist.remove(self.fruitlist[0])
                        i += 1
                    length = len(self.meatlist)
                    while i < length:
                        self.fruitlist.remove(self.meatlist[0])
                        i += 1
                    length = len(self.tigerlist)
                    while i < length:
                        self.fruitlist.remove(self.tigerlist[0])
                        i += 1
                elif event.key == K_l:
                    i = Llama((self.mouseX, self.mouseY))
                    self.llamalist.append(i)
                elif event.key == K_p:
                    i = Pear((self.mouseX, self.mouseY))
                    self.fruitlist.append(i)
                elif event.key == K_a:
                    i = Apple((self.mouseX, self.mouseY))
                    self.fruitlist.append(i)
            elif event.type == KEYUP:
                if event.key == K_UP:
                    self.moveUp = False
                    # if the player was moving in a sideways direction before, change the self.direction the player is facing.
                    if self.moveLeft:
                        self.direction = 'left'
                    if self.moveRight:
                        self.direction = 'right'
                elif event.key == K_DOWN:
                    self.moveDown = False
                    if self.moveLeft:
                        self.direction = 'left'
                    if self.moveRight:
                        self.direction = 'right'
                elif event.key == K_LEFT:
                    self.moveLeft = False
                    if self.moveUp:
                        self.direction = 'up'
                    if self.moveDown:
                        self.direction = 'down'
                elif event.key == K_RIGHT:
                    self.moveRight = False
                    if self.moveUp:
                        self.direction = 'up'
                    if self.moveDown:
                        self.direction = 'down'
        
        # moving
        if self.moveUp or self.moveDown or self.moveLeft or self.moveRight:
            self.moveConductor.play()
            # draw the correct walking/running sprite from the animation object
            if self.direction == 'up':
                self.player.getAnimation('back_walk').blit(self.screen, (self.player.x, self.player.y))
            elif self.direction == 'down':
                self.player.getAnimation('front_walk').blit(self.screen, (self.player.x, self.player.y))
            elif self.direction == 'left':
                self.player.getAnimation('left_walk').blit(self.screen, (self.player.x, self.player.y))
            elif self.direction == 'right':
                self.player.getAnimation('right_walk').blit(self.screen, (self.player.x, self.player.y))
            
            # actually move the position of the player
            if self.moveUp:
                self.player.y -= self.player.speed
            if self.moveDown:
                self.player.y += self.player.speed
            if self.moveLeft:
                self.player.x -= self.player.speed
            if self.moveRight:
                self.player.x += self.player.speed
        # standing still
        else:
            self.moveConductor.stop()
            if self.direction == 'up':
                self.screen.blit(self.player.getImages('back_standing'), (self.player.x, self.player.y))
            elif self.direction == 'down':
                self.screen.blit(self.player.getImages('front_standing'), (self.player.x, self.player.y))
            elif self.direction == "left":
                self.screen.blit(self.player.getImages('left_standing'), (self.player.x, self.player.y))
            elif self.direction == "right":
                self.screen.blit(self.player.getImages('right_standing'), (self.player.x, self.player.y))

    def updateLists(self):
        # Fruit
        for each in self.fruitlist:
            # fruit is 24x24 so half is 12
            self.screen.blit(each.getImage(), (int(each.x - 12), int(each.y - 12)))
        
        # Llama
        for each in self.llamalist:
            each.frame(self.fruitlist)
            # moving
            if each.moving:
                each.moveConductor.play()
                # draw the correct walking/running sprite from the animation object
                if ((each.direction > 315) or (each.direction < 45)):
                    each.getAnimation('back_walk').blit(self.screen, (each.x, each.y))
                    print("back_walk")
                elif ((each.direction > 135) and (each.direction < 225)):
                    each.getAnimation('front_walk').blit(self.screen, (each.x, each.y))
                    print("front_walk")
                elif ((each.direction >= 225) and (each.direction <= 315)):
                    each.getAnimation('left_walk').blit(self.screen, (each.x, each.y))
                    print("left_walk")
                elif ((each.direction >= 45) and (each.direction <= 135)):
                    each.getAnimation('right_walk').blit(self.screen, (each.x, each.y))
                    print("right_walk")
            # standing still
            else:
                each.moveConductor.stop()
                if ((each.direction > 315) or (each.direction < 45)):
                    self.screen.blit(each.getImages('back_standing'), (each.x, each.y))
                elif ((each.direction > 135) and (each.direction < 225)):
                    self.screen.blit(each.getImages('front_standing'), (each.x, each.y))
                elif ((each.direction >= 225) and (each.direction <= 315)):
                    self.screen.blit(each.getImages('left_standing'), (each.x, each.y))
                elif ((each.direction >= 45) and (each.direction <= 135)):
                    self.screen.blit(each.getImages('right_standing'), (each.x, each.y))


    def mainLoop(self):
        framecount = 0  # frame count for debugging
        while not self.done:
            self.draw()
            self.handleEvents()
            self.updateLists()
            
            # updates certain sections of the screen based on parameters (No parameters = full screen refresh)
            pygame.display.update()
            print("frame: " + str(framecount))
            framecount += 1
            self.fpsClock.tick(30)