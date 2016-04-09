'''
Created on Aug 25, 2013

@author: Brandon
'''

import random


class Food:
    def __init__(self, pos):
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.quantity = random.randint(5, 15)
        