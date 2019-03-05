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
        'is_patrolling': is_patrolling
      }
      self.properties = {
        'speed': 8
      }
      self.properties.update(properties)
      self.direction = -1
      self.old_x, self.old_y = self.x, self.y

    def update(self, dt):
        if self.states['is_patrolling']:
            self.move()
        self.y = calculate_gravity(self.y)
        if detect_floor(self.y):
            self.y = self.old_y
        if detect_world_bounds(self):
            self.direction *= -1
            self.x = self.old_x
        self.old_x, self.old_y = self.x, self.y

    def move(self):
        speed = self.properties['speed']
        self.x += speed * self.direction