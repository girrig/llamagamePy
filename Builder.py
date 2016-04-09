'''
Created on Jan 8, 2014

@author: Brandon
'''

import wx
import os

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname=''

        # -1 as the second size parameter instructs wxWidgets to use the default size
        wx.Frame.__init__(self, parent, title=title, size=(1280,720))
        self.CreateStatusBar() # A Status Bar in the bottom of the window

        # Add a panel so it looks correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY)


        text = wx.StaticText(self.panel, -1, "This is some random text for the sake of making this GUI maker good at some point", (10,10), (-1,-1), wx.ALIGN_CENTER)

        
        # Setting up the File menu
        filemenu = wx.Menu()
        menuNew = filemenu.Append(wx.ID_NEW, "&New"," Create a new File")
        menuOpenWorld = filemenu.Append(wx.ID_OPEN, "&Open World"," Open a world file")
        menuSaveWorld = filemenu.Append(wx.ID_SAVE, "&Save World"," Save a world file")
        menuLoadImage = filemenu.Append(wx.ID_OPEN, "&Load Image","Open an image file")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT,"&Exit"," Terminate the program")

        # Creating the Menu Bar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the File Menu to the Menu Bar
        self.SetMenuBar(menuBar)  # Adding the Menu Bar to the Frame content
        
        # Events
        self.Bind(wx.EVT_MENU, self.onNew, menuNew)
        self.Bind(wx.EVT_MENU, self.onOpenWorld, menuOpenWorld)
        self.Bind(wx.EVT_MENU, self.onSaveWorld, menuSaveWorld)
        self.Bind(wx.EVT_MENU, self.onLoadImage, menuLoadImage)
        self.Bind(wx.EVT_MENU, self.onAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.onExit, menuExit)
        
        
    def onNew(self, e):
        return
    
    def onOpenWorld(self, e):
        """ Open a file"""
        box = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if box.ShowModal() == wx.ID_OK:
            self.filename = box.GetFilename()
            self.dirname = box.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        box.Destroy()
        
    def onSaveWorld(self, e):
        return
    
    def onLoadImage(self, e):
        box = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if box.ShowModal() == wx.ID_OK:
            self.picName = box.GetFilename()
            self.picDir = box.GetDirectory()
            temp = self.picDir + "\\" + self.picName
            p = wx.Image(temp, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            wx.StaticBitmap(self, -1, p, (10, 50), (p.GetWidth(), p.GetHeight()))
        box.Destroy()
    
    def onAbout(self, e):
        # Create a message dialog box
        box = wx.MessageDialog(self, " A sample editor \n in wxPython", "About Llama Game World Builder", wx.OK)
        box.ShowModal() # Shows it
        box.Destroy() # finally destroy it when finished

    def onExit(self, e):
        self.Close(True)  # Close the frame


app = wx.App(False)
frame = MainWindow(None, "Llama Game World Builder")
frame.Show()
app.MainLoop()