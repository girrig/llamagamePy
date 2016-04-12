'''
Created on Feb 10, 2013

@author: Brandon
'''

import pygame
from pygame.locals import *
from Player import Player
from Animal import Llama, Tiger
from Fruit import Apple, Pear
import math
import time


class Debug():
    def __init__(self, width=1280, height=720):
        pygame.init()
        self.width = width
        self.height = height
        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Llama Simulator 3000: Alpha v0.007')
        
        # color for background
        self.lightgreen = pygame.Color(130, 255, 130)

        # mouse
        self.mouseX, self.mouseY = 0, 0

        # font for text display
        self.font = pygame.font.Font('freesansbold.ttf', 18)

        # lists of all things on the screen
        self.fruitlist = []
        self.llamalist = []
        self.tigerlist = []

        # Player
        self.player = Player((self.width/2, self.height/2))

        # Loop
        self.done = False
    
    
    #### MAIN LOOP FUCTIONS ####
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
                    self.player.moveUp = True
                    self.player.moveDown = False
                    if not self.player.moveLeft and not self.player.moveRight:
                        # only change the direction to up if the player wasn't moving left/right
                        self.player.direction = 'up'
                elif event.key == K_DOWN:
                    self.player.moveDown = True
                    self.player.moveUp = False
                    if not self.player.moveLeft and not self.player.moveRight:
                        self.player.direction = 'down'
                elif event.key == K_LEFT:
                    self.player.moveLeft = True
                    self.player.moveRight = False
                    if not self.player.moveUp and not self.player.moveDown:
                        self.player.direction = 'left'
                elif event.key == K_RIGHT:
                    self.player.moveRight = True
                    self.player.moveLeft = False
                    if not self.player.moveUp and not self.player.moveDown:
                        self.player.direction = 'right'
                elif event.key == K_c:  # clears everything
                    del self.fruitlist[:]
                    del self.llamalist[:]
                    del self.tigerlist[:]
                elif event.key == K_l:
                    self.llamalist.append(Llama((self.mouseX, self.mouseY)))
                elif event.key == K_p:
                    self.fruitlist.append(Pear((self.mouseX, self.mouseY)))
                elif event.key == K_a:
                    self.fruitlist.append(Apple((self.mouseX, self.mouseY)))
                elif event.key == K_t:
                    self.tigerlist.append(Tiger((self.mouseX, self. mouseY)))
            elif event.type == KEYUP:
                if event.key == K_UP:
                    self.player.moveUp = False
                    # if the player was moving in a sideways direction before, change the self.direction the player is facing.
                    if self.player.moveLeft:
                        self.player.direction = 'left'
                    if self.player.moveRight:
                        self.player.direction = 'right'
                elif event.key == K_DOWN:
                    self.player.moveDown = False
                    if self.player.moveLeft:
                        self.player.direction = 'left'
                    if self.player.moveRight:
                        self.player.direction = 'right'
                elif event.key == K_LEFT:
                    self.player.moveLeft = False
                    if self.player.moveUp:
                        self.player.direction = 'up'
                    if self.player.moveDown:
                        self.player.direction = 'down'
                elif event.key == K_RIGHT:
                    self.player.moveRight = False
                    if self.player.moveUp:
                        self.player.direction = 'up'
                    if self.player.moveDown:
                        self.player.direction = 'down'

    def update(self):
        self.updateMap()
        self.updateLists()
        self.updatePlayer()

    def draw(self):
        # order matters here
        self.drawMap()
        self.drawPlayer()
        self.drawLists()

    #### SUB FUNCTIONS ####
    def updateMap(self):
        pass

    def updateLists(self):
        # Llama
        for each in self.llamalist:
            each.update(self.fruitlist)

        # Tiger
        for each in self.tigerlist:
            each.update(self.llamalist)

    def updatePlayer(self):
        self.player.update()

    def drawMap(self):
        self.screen.fill(self.lightgreen)

    def drawPlayer(self):
        self.player.paint(self.screen)

    def drawLists(self):
        # Fruit
        for each in self.fruitlist:
            # fruit is 24x24 so half is 12
            self.screen.blit(each.getImage(), (int(each.x - 12), int(each.y - 12)))

        # Llama
        for each in self.llamalist:
            each.paint(self.screen)

        # Tiger
        for each in self.tigerlist:
            each.paint(self.screen)

    def mainLoop(self):
        framecount = 0  # frame count for debugging
        while not self.done:
            self.handleEvents()
            self.update()
            self.draw()

            # updates certain sections of the screen based on parameters (No parameters = full screen refresh)
            pygame.display.update()
            #print("frame: " + str(framecount))
            framecount += 1
            self.fpsClock.tick(30)