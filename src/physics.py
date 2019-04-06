#./src/physics.py

gravity_strength = 5
world_width = 800

def detect_platform_collision(platforms, sprite):
    for platform in platforms:
        if detect_collision(platform, sprite):
            if 'collision' in platform.properties:
                sides = platform.properties['collision']
                if 'l' in sides and sprite.x + sprite.width >= platform.x:
                    sprite.x = sprite.old_x
                if 'r' in sides and sprite.x <= platform.x + platform.width:
                    sprite.x = sprite.old_x
                if 't' in sides and sprite.old_y >= platform.y + platform.height:
                    sprite.y = platform.y + platform.height
                if 'b' in sides:
                    sprite.y = sprite.old_y

def calculate_gravity(current_y):
    current_y -= gravity_strength
    return current_y

def detect_world_bounds(walls, sprite, enemies=None):
    kill_sprite = False
    for wall in walls:
        if detect_collision(wall, sprite):
            if wall.name == 'wall_left' or wall.name == 'wall_right':
                sprite.x = sprite.old_x
            if wall.type == 'death' or wall.name == 'wall_bottom':
                sprite.get_hit(1)    
                kill_sprite = True

    sprite.old_x, sprite.old_y = sprite.x, sprite.y
    if kill_sprite:
        if enemies is not None:
            enemies.remove(sprite)
        sprite.die()

def detect_blockers(blockers, sprite):
    for blocker in blockers:
        if detect_collision(blocker, sprite):
            if 'collision' in blocker.properties:
                sides = blocker.properties['collision']
                if 'l' in sides and sprite.x + sprite.width >= blocker.x:
                    sprite.direction *= -1
                if 'r' in sides and sprite.x <= blocker.x + blocker.width:
                    sprite.direction *= -1

def detect_collision(this, other):
    return (this.x + this.width > other.x and
            other.x + other.width > this.x and
            this.y + this.height > other.y and
            other.y + other.height > this.y)