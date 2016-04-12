'''
Created on Apr 11, 2016

@author: Brandon
'''

import pygame
from pygame.locals import *
from Player import Player
from Animal import Llama, Tiger
from Fruit import Apple, Pear
import math
import time


class Display():
    def __init__(self, width=1280, height=720):
        pygame.init()
        self.width = width
        self.height = height
        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Llama Simulator 3000: Alpha v0.007')
        
        # color for background
        self.lightgreen = pygame.Color(130, 255, 130)

        # font for text display
        self.font = pygame.font.Font('freesansbold.ttf', 18)

        # lists of all things on the screen
        self.fruitlist = []
        self.llamalist = []
        self.tigerlist = []

        # Loop
        self.done = False
    
    
    #### MAIN LOOP FUCTIONS ####
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()

    def update(self):
        self.updateMap()
        self.updateLists()

    def draw(self):
        # order matters here
        self.drawMap()
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

    def drawMap(self):
        self.screen.fill(self.lightgreen)

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
            print("frame: " + str(framecount))
            framecount += 1
            self.fpsClock.tick(30)