'''
Created on Apr 11, 2016

@author: Brandon
'''

from Player import Player
from Animal import Llama, Tiger
from Fruit import Apple, Pear


class World():
    def __init__(self):
        # lists of all things on the screen
        self.fruitlist = []
        self.llamalist = []
        self.tigerlist = []

        # Loop
        self.done = False
    
    
    #### MAIN LOOP FUCTIONS ####
    def handleEvents(self):
        pass

    def update(self):
        self.updateMap()
        self.updateLists()

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

    def mainLoop(self):
        while not self.done:
            self.handleEvents()
            self.update()