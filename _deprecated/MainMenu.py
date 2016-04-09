'''
Created on Apr 11, 2014

@author: Brandon
'''

import pygame
from pygame.locals import *

class MainMenu():
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Llama Simulator 3000: Alpha v0.005')

        self.white = pygame.Color(255, 255, 255)
        
        #mouse
        self.mouseX, self.mouseY = 0, 0

        self.fontObj = pygame.font.Font('freesansbold.ttf', 18)
        
        # Loop
        self.done = False

    def draw(self):
        self.screen.fill(self.white)
        # update menu
        
        

    def handleEvents(self):
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEMOTION:
                self.mouseX, self.mouseY = event.pos
            elif event.type == MOUSEBUTTONUP:
                continue  # figure out where mouse was clicked and execute that action if there is one
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()

    def mainLoop(self):
        framecount = 0  # frame count for debugging
        while not self.done:
            self.draw()
            self.handleEvents()
            
            # updates certain sections of the screen based on parameters (No parameters = full screen refresh)
            pygame.display.update()
            print("frame: " + str(framecount))
            framecount += 1
            self.fpsClock.tick(30)