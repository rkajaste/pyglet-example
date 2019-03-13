# src/sprites/enemies/ShootingEnemy.py
import pyglet
from src.sprites.enemies.Enemy import Enemy
from src.sprites.objects.Bullet import Bullet
from src.timings import has_cooldown

class ShootingEnemy(Enemy):
    def __init__(self, x, y,
          image=pyglet.resource.image('resources/enemies/enemy_red.png'),
          properties={'firing_cooldown': 20},
          is_patrolling=False,
          targets=[]):
        super(ShootingEnemy, self).__init__(x, y, 
                                            image, 
                                            is_patrolling=is_patrolling)
        self.targets=targets
        self.created_objects['bullets'] = []
        self.properties.update(properties)
        self.timer = 0
        self.last_fire = 0

    def update(self, dt):
        super().update(dt)
        self.timer += 1
        if not has_cooldown(self.timer,\
                        self.last_fire,\
                        self.properties['firing_cooldown']):
            self.timer = 0
            self.last_fire = 0
            self.fire()
    
    def fire (self):
        bullet_image = pyglet.resource.image('resources/objects/bullet_red.png')
        Bullet(
            x=self.x,
            y=self.y + self.height / 2,
            image=bullet_image,
            direction=self.direction,
            bullets=self.created_objects['bullets'],
            targets=self.enemies,
            damage=self.properties['damage']
        )