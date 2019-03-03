# ./src/sprites/Player.py
import pyglet
from config import key, keys
from src.physics import *

class Player(pyglet.sprite.Sprite):
    def __init__(self, x, y):
        image = pyglet.resource.image('resources/player/player.png')
        super(Player, self).__init__(x=x, y=y, img=image)
        self.constants = {
            'speed': 8,
            'jumping_power': 40 
        }
        self.old_x, self.old_y = self.x, self.y

    def update(self, dt):
        if keys[key.LEFT] or keys[key.RIGHT]:
            self.move(keys[key.LEFT])
        if keys[key.SPACE]:
            self.jump()
        self.y = calculate_gravity(self.y)
        if detect_floor(self.y):
            self.y = self.old_y
        if detect_world_bounds(self):
            self.x = self.old_x
        self.old_x, self.old_y = self.x, self.y

    def jump(self):
        jumping_power = self.constants.get('jumping_power')
        self.y += jumping_power

    def move(self, is_moving_left):
        speed = self.constants.get('speed')
        if is_moving_left:
            self.x -= speed
        else:
            self.x += speed
