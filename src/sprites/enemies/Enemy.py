# src/sprites/enemies/Enemy.py
import pyglet
from src.physics import calculate_gravity, detect_world_bounds, detect_floor

class Enemy(pyglet.sprite.Sprite):
    def __init__(self, x, y,
          image=pyglet.resource.image('resources/enemies/enemy_red.png'),
          properties={},
          is_patrolling=False):
      super(Enemy, self).__init__(x=x, y=y, img=image)
      self.states = {
        'is_moving_left': True,
        'is_patrolling': is_patrolling
      }
      self.properties = {
        'speed': 8
      }
      self.properties.update(properties)
      self.old_x, self.old_y = self.x, self.y

    def update(self, dt):
        is_moving_left = self.states['is_moving_left']
        if self.states['is_patrolling']:
            self.move(is_moving_left)
        self.y = calculate_gravity(self.y)
        if detect_floor(self.y):
            self.y = self.old_y
        if detect_world_bounds(self):
            self.states['is_moving_left'] = not is_moving_left
            self.x = self.old_x
        self.old_x, self.old_y = self.x, self.y

    def move(self, is_moving_left):
        speed = self.properties['speed']
        if is_moving_left:
            self.x -= speed
        else:
            self.x += speed