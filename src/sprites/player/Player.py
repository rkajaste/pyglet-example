# ./src/sprites/player/Player.py
import pyglet
from config import key, keys
from src.physics import calculate_gravity, detect_world_bounds, detect_floor
from src.timings import has_cooldown
from src.sprites.objects.Bullet import Bullet

class Player(pyglet.sprite.Sprite):
    def __init__(self, 
            x, y, 
            targets,
            image=pyglet.resource.image('resources/player/player.png'),
            batch=None, 
            group=None):
        super(Player, self).__init__(x=x, y=y, img=image, batch=batch, group=group)
        self.batch = batch
        self.group = group
        self.properties = {
            'speed': 8,
            'jumping_power': 40,
            'firing_cooldown': 20,
            'max_health': 3,
            'damage': 1
        }
        self.health = self.properties['max_health']
        self.targets = targets
        self.bullets = []
        self.direction = 1
        self.last_fire = 0
        self.timer = 0
        self.old_x, self.old_y = self.x, self.y

    def update(self, dt):
        self.timer += 1
        if keys[key.LEFT] or keys[key.RIGHT]:
            if keys[key.LEFT] and self.direction == 1:
                self.direction *= -1
            elif keys[key.RIGHT] and self.direction == -1:
                self.direction *= -1
            self.move()
        if keys[key.UP]:
            self.jump()
        if keys[key.SPACE] and not\
        has_cooldown(self.timer,\
                    self.last_fire,\
                    self.properties['firing_cooldown']):
            self.timer = 0
            self.last_fire = 0
            self.fire()
        self.y = calculate_gravity(self.y)
        if detect_floor(self.y):
            self.y = self.old_y
        if detect_world_bounds(self):
            self.x = self.old_x
        self.old_x, self.old_y = self.x, self.y

    def updateAll(self, dt):
        self.update(dt)
        for bullet in self.bullets:
            bullet.update(dt)

    def drawAll(self):
        self.draw()
        for bullet in self.bullets:
            bullet.draw()

    def jump(self):
        jumping_power = self.properties['jumping_power']
        self.y += jumping_power

    def move(self):
        speed = self.properties['speed']
        self.x += speed * self.direction

    def fire (self):
        bullet_image = pyglet.resource.image('resources/objects/bullet_white.png')
        Bullet(
            x=self.x,
            y=self.y + self.height / 2,
            image=bullet_image,
            direction=self.direction,
            bullets=self.bullets,
            targets=self.targets,
            damage=self.properties['damage'],
            batch=self.batch,
            group=self.group
        )

    def get_hit (self, damage):
        self.health -= damage

    def die (self):
        self.respawn(100, 100)
    
    def respawn(self, x, y):
        self.x, self.y = x, y
        self.health = self.properties['max_health']
        self.timer = 0
        self.last_fire = 0
        