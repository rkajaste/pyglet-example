# ./main.py
import pyglet
from pyglet.gl import *
from config import key, keys
from src.Level import Level
from config import SCREEN_WIDTH
from config import SCREEN_HEIGHT
from config import FULLSCREEN

class Game(pyglet.window.Window):
    def __init__(self):
        super(Game, self).__init__(width=SCREEN_WIDTH, 
                                    height=SCREEN_HEIGHT,
                                    fullscreen=FULLSCREEN)
        pyglet.clock.schedule_interval(self.update, 1 / 60.0)
        self.level = Level()

    def update(self, dt):
        self.push_handlers(keys)
        self.level.update(dt)

    def on_draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.level.draw()
        
        
if __name__ == '__main__':
    game = Game()
    pyglet.app.run()