#./src/physics.py

gravity_strength = 5
world_width = 800

def calculate_gravity(current_y):
    current_y -= gravity_strength
    return current_y

def detect_floor(current_y):
    return current_y <= 0

def detect_world_bounds(obj):
    return obj.x <= 0 or obj.x + obj.width >= world_width

def detect_collision(this, other):
    return (this.x + this.width > other.x and
            other.x + other.width > this.x and
            this.y + this.height > other.y and
            other.y + other.height > this.y)