# src/sprites/enemies/Enemy.py
import pyglet
from src.physics import calculate_gravity, detect_world_bounds, detect_floor

class Enemy(pyglet.sprite.Sprite):
    def __init__(self, x, y,
          image=pyglet.resource.image('resources/enemies/enemy_red.png'),
          is_patrolling=False):
      super(Enemy, self).__init__(x=x, y=y, img=image)
      self.states = {
        'is_patrolling': is_patrolling
      }
      self.properties = {
        'speed': 8,
        'max_health': 3,
        'damage': 1
      }
      self.health = self.properties['max_health']
      self.created_objects = {}
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
    
    def updateAll(self, dt):
        self.update(dt)
        for objects in self.created_objects:
            for obj in objects:
                obj.update(dt)

    def drawAll(self):
        self.draw()
        for objects in self.created_objects:
            for obj in objects:
                obj.draw()

    def move(self):
        speed = self.properties['speed']
        self.x += speed * self.direction

    def get_hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die (self):
        self.kill()