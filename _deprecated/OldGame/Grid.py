'''
Created on Aug 9, 2012

@author: Brandon
'''

from Cell import *
import math


class Grid:
    #grid is z*z
    def __init__(self, z):

        #Length of cells array is the number of cells
        self.cells = []
        #dictionary of all the x and y coordinates
        self.cell_lookup = {}
        
        self.max_x = 0
        self.max_y = 0
        self.min_x = 0
        self.min_y = 0
        
        #upper left most visible cell
        self.ref_x = -z
        self.ref_y = -z
        
        
        for x in range(-z,z):
            for y in range(-z,z):
                self.generateCell(x,y)


    def generateCell(self,x,y):
        cell = Cell()
        pos = len(self.cells)
        cell.x = x
        cell.y = y
        #keeping track of max_x
        if cell.x > self.max_x:
            self.max_x = cell.x
        #keeping track of max_y
        if cell.y > self.max_y:
            self.max_y = cell.y
        #keeping track of min_x
        if cell.x < self.min_x:
            self.min_x = cell.x
        #keeping track of min_y
        if cell.y < self.min_y:
            self.min_y = cell.y
        
        #getting current cell's position
        self.cell_lookup[str(x)+","+str(y)] = pos
        cell.position = pos
        
        #WEBBING~~~~
        #north
        try:
            n = self.cell_lookup[str(cell.x)+","+str((cell.y)+1)]
        except KeyError:
            pass
        else:
            self.cells[n].south = pos
            cell.north = n
        #east
        try:
            e = self.cell_lookup[str((cell.x)+1)+","+str(cell.y)]
        except KeyError:
            pass
        else:
            self.cells[e].west = pos
            cell.east = e
        #south
        try:
            s = self.cell_lookup[str(cell.x)+","+str((cell.y)-1)]
        except KeyError:
            pass
        else:
            self.cells[s].north = pos
            cell.south = s
        #west
        try:
            w = self.cell_lookup[str((cell.x)-1)+","+str(cell.y)]
        except KeyError:
            pass
        else:
            self.cells[w].east = pos
            cell.west = w
        self.cells.append(cell)


    def GridToWin(self, size, grid_x, grid_y):
        win_x = (grid_x * size) + int(size/2)
        win_y = (grid_y * size) + int(size/2)
        #OLD CODE THAT SORT OF WORKED (AND MAKES MORE SENSE)
        #win_x = abs(self.ref_x - grid_x)*(math.sqrt(size))
        #win_y = abs(self.ref_y - grid_y)*(math.sqrt(size))
        return win_x, win_y