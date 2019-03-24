# ./main.py
import pyglet
from pyglet.gl import *
from config import key, keys
from src.Level import Level

class Game(pyglet.window.Window):
    def __init__(self):
        super(Game, self).__init__(width=800, height=600, fullscreen=False)
        pyglet.clock.schedule_interval(self.update, 1 / 120.0)
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