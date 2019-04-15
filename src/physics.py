#./src/physics.py

def detect_platform_collision(platforms, sprite):
    sprite.states['grounded'] = False
    for platform in platforms:
        if detect_collision(platform, sprite):
            if 'collision' in platform.properties:
                blocked_sides = platform.properties['collision']
                check_left_right = True
                platform_top = round(platform.y + platform.height)
                platform_left = round(platform.x)
                platform_bottom = round(platform.y)
                platform_right = round(platform.x + platform.width)
                if ('t' in blocked_sides and 
                    sprite.old_y >= platform_top):
                        sprite.y = platform_top
                        sprite.change_y = 0
                        sprite.states['grounded'] = True
                        check_left_right = False

                if ('b' in blocked_sides and 
                    sprite.y + sprite.height >= platform_bottom and
                    sprite.old_y + sprite.height < platform_top):
                        sprite.y = platform_bottom - sprite.height
                        check_left_right = False

                if check_left_right:
                    if ('l' in blocked_sides and 
                        sprite.x + sprite.width >= platform_left and
                        sprite.x <= platform_left):
                            sprite.x = platform_left - sprite.width
                    if ('r' in blocked_sides and 
                        sprite.x <= platform_right and
                        sprite.x + sprite.width >= platform_right):
                            sprite.x = platform_right

def calculate_gravity(change_y):
    if change_y == 0:
        change_y = -1
    else:
        change_y -= 4
    
    return change_y


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
                if 'l' in sides and sprite.x + sprite.width >= blocker.x or \
                    'r' in sides and sprite.x <= blocker.x + blocker.width:
                    sprite.direction *= -1

def detect_collision(this, other):
    return (this.x + this.width > other.x and
            other.x + other.width > this.x and
            this.y + this.height > other.y and
            other.y + other.height > this.y)