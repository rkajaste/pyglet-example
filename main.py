# ./main.py
import pyglet
from pyglet.gl import *
from src.sprites.player.Player import Player
from src.sprites.enemies.Enemy import Enemy
from config import key, keys

class Game(pyglet.window.Window):
    def __init__(self):
        super(Game, self).__init__(width=800, height=600, fullscreen=False)
        pyglet.clock.schedule_interval(self.update, 1 / 120.0)
        self.player = Player(100, 100)
        self.enemy = Enemy(600, 100, is_patrolling=True)

    def update(self, dt):
        self.push_handlers(keys)
        self.player.update(dt)
        self.enemy.update(dt)

    def on_draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.player.draw()
        self.enemy.draw()
        
if __name__ == '__main__':
    game = Game()
    pyglet.app.run()