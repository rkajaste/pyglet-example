# ./main.py
import pyglet
from pyglet.gl import *
from src.sprites.player.Player import Player
from src.sprites.enemies.Enemy import Enemy
from src.sprites.enemies.ShootingEnemy import ShootingEnemy
from config import key, keys

class Game(pyglet.window.Window):
    def __init__(self):
        super(Game, self).__init__(width=800, height=600, fullscreen=False)
        pyglet.clock.schedule_interval(self.update, 1 / 120.0)
        self.enemies = []
        self.player = Player(100, 100, self.enemies)
        self.enemies.extend([
            Enemy(600, 100, is_patrolling=True),
            ShootingEnemy(600, 100, targets=[self.player])
        ])
        
    def update(self, dt):
        self.push_handlers(keys)
        self.player.updateAll(dt)
        for enemy in self.enemies:
            enemy.updateAll(dt)

    def on_draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.player.drawAll()
        for enemy in self.enemies:
            enemy.drawAll()
        
if __name__ == '__main__':
    game = Game()
    pyglet.app.run()