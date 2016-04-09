'''
Created on Jul 28, 2012

@author: Brandon
'''
import Tkinter as tk
#import pygame.image
from Grid import *
from UnitManager import *

class World(tk.Frame):
    def __init__(self, parent, size=32):
        
        self.grid = Grid(7)
        
        self.unitmanager = UnitManager()


        self.total_x = self.grid.max_x + (self.grid.min_x * -1)
        self.total_y = self.grid.max_y + (self.grid.min_y * -1)
        self.size = size
        self.x = (self.grid.max_x + 1 - self.grid.min_x)
        self.y = (self.grid.max_y + 1 - self.grid.min_y)
        
        
        canvas_width = self.x * size
        canvas_height = self.y * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0, width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)
        
        #making the player
        tempx,tempy = self.grid.GridToWin(self.size, 0,0)
        img = self.unitmanager.ResizeImage(self.unitmanager.unit.getPhoto(), self.size)
        self.canvas.create_image(tempx, tempy, image=img, tags=self.unitmanager.unit.getName(), anchor="nw")
        self.canvas.coords("player", tempx, tempy)
        self.canvas.tag_raise("player")

        #this binding will cause a refresh if the user interactively changes the window size
        self.canvas.bind("<Configure>", self.refresh)


    
    def refresh(self, event):
        if event.type == "2":
            tempx,tempy = self.grid.GridToWin(self.size, 0,0)
            img = self.unitmanager.ResizeImage(self.unitmanager.unit.getPhoto(), self.size)
            self.canvas.create_image(tempx, tempy, image=img, tags=self.unitmanager.unit.getName(), anchor="nw")
            self.canvas.coords("player", tempx, tempy)
            self.canvas.tag_raise("player")
        else:
            '''Redraw the board, possibly in response to window being resized'''
            xsize = (int(event.width)-1) / self.x
            ysize = (int(event.height)-1) / self.y
            self.size = min(xsize, ysize)
            self.canvas.delete("square")
            for row in range(self.x - self.grid.min_x):
                #print("self.x", self.x)
                #print("self.grid.min_x", self.grid.min_x)
                #print ("row ", row)
                for col in range(self.y - self.grid.min_y):
                    #print("self.y", self.y)
                    #print("self.grid.min_y", self.grid.min_y)
                    #print("col ", col)
                    try:
                        self.grid.cell_lookup[str(row + self.grid.min_x)+","+str(col + self.grid.min_y)]
                    except KeyError:
                        pass
                    else:
                        x1 = col * self.size
                        y1 = row * self.size
                        x2 = x1 + self.size
                        y2 = y1 + self.size
                        #if (row + self.grid.min_x) == self.unitmanager.unit.x_loc and (col + self.grid.min_y) == self.unitmanager.unit.y_loc:
                        #    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="blue", tags="square")
                        #else:
                        self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", tags="square")
                        #photo = PhotoImage(file="testtile.gif")
                        #self.canvas.create_image(image=photo)
        
    def key(self, event):
    #shows key or tk code for the key
        #Kills Window
        if event.keysym == 'Escape':
            root.destroy()
        if event.keysym == 'Up':
            self.unitmanager.moveNorth()
            self.refresh(event)
        if event.keysym == 'Right':
            self.unitmanager.moveEast()
            self.refresh(event)
        if event.keysym == 'Down':
            self.unitmanager.moveSouth()
            self.refresh(event)
        if event.keysym == 'Left':
            self.unitmanager.moveWest()
            self.refresh(event)


if __name__ == "__main__":

    root = tk.Tk()
    world = World(root)
    world.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    root.bind_all('<Key>', world.key)
    
    root.mainloop()