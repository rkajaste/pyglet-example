#./src/ui/HealthBar.py
from pyglet.gl import GL_QUADS
from src.ui.InterfaceComponent import InterfaceComponent

class HealthBar(InterfaceComponent):
    def __init__(self, x, y, batch):
        super(HealthBar, self).__init__(x, y, batch)
        self.health_points = []
        self.offset = 30
        self.size = 20

    def populate(self, health):
        for i in range(health):
            right = (self.x + self.size) + (self.offset * i)
            left = self.x + (self.offset * i)
            top = self.y + self.size
            bottom = self.y
            vertex_positions = [
                right, top,
                left, top,
                left, bottom,
                right, bottom
            ]
            health_point = self.batch.add(4, GL_QUADS, None,
                                    ('v2f/static', vertex_positions),
                                    ('c3B/static', (
                                        0, 255, 0,
                                        0, 255, 0,
                                        0, 255, 0,
                                        0, 255, 0
                                    )))
            self.health_points.append(health_point)

    def pop_health(self, damage):
        if damage > len(self.health_points):
            damage = len(self.health_points) - 1
        for __ in range(damage):
            self.health_points[len(self.health_points) - 1].delete()
            self.health_points.pop()