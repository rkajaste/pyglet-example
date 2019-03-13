# ./src/sprites/objects/Bullet.py
import pyglet
from src.physics import detect_world_bounds, detect_collision

class Bullet(pyglet.sprite.Sprite):
    def __init__(self, x, y, image, direction, bullets, targets, damage):
        super(Bullet, self).__init__(x=x, y=y, img=image)
        self.direction = direction
        self.bullets = bullets
        self.targets = targets
        self.damage = damage
        self.properties = {
            'speed': 16
        }
        self.bullets.append(self)

    def update(self, dt):
        self.move()
        if detect_world_bounds(self) or self.collides():
            self.bullets.remove(self)
            self.delete()

    def move(self):
        self.x += self.properties['speed'] * self.direction

    def collides(self):
        for target in self.targets:
            if detect_collision(self, target):
                target.get_hit(self.properties['damage'])
                return True
        return False