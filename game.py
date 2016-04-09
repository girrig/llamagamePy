import pygame
from pygame.locals import *    
from pygame import Color
from map import Map

GAME_ABOUT = """about:
    -using tileset and numpy 2D array for map data.
    -randomizes tiles, and creates roads
    
    -Howto set/get tile at loc=(x,y)
        tiles[x,y] = 2
        tileid = tiles[x,y]
    
"""
GAME_TITLE = "maptiles numpy {nin.example} "
GAME_HOTKEYS = """== Hotkeys! ===
    space = randomize tiles
    ESC    = quit
    s = toggle scrolling
"""
    
class Game():
    """game Main entry point. handles intialization of game and graphics.    
    members:
        map : map.Map() instance
    """
    done  = False
    
    def __init__(self, width=640, height=480):
        """Initialize PyGame"""        
        pygame.init()
        self.width, self.height = width, height
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(GAME_TITLE)
        
        self.map = Map(self)

        print GAME_TITLE
        print GAME_ABOUT
        print GAME_HOTKEYS
        
            
    def main_loop(self):
        """Game() main loop"""        
        while not self.done:
            # get key input, move, draw.
            self.handle_events()
            self.draw()                      
            self.clock.tick(60)
        
    def handle_events(self):
        """handle events."""
        events = pygame.event.get()
        for event in events:            
            if event.type == pygame.QUIT: sys.exit()            
            # event: keydown
            elif event.type == KEYDOWN:
                # exit on Escape
                if event.key == K_ESCAPE: self.done = True
                # toggle bool
                elif event.key == K_s: self.map.scrolling = not self.map.scrolling
                elif event.key== K_SPACE:
                    # random map
                    self.map.randomize()    
                    
            elif event.type == MOUSEMOTION:
                self.map.scroll(event.rel)

    def draw(self):
        """render screen"""
        self.screen.fill(Color("black")) 
        self.map.draw()    
        pygame.display.flip()
