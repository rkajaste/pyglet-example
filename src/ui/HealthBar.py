import pyglet
from pyglet.gl import *

class HealthBar:
    def __init__(self, x, y, batch, group):
        self.x = x
        self.y = y
        self.batch = batch
        self.group = group
        self.blocks = []
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
            block = self.batch.add(4, GL_QUADS, self.group,
                                    ('v2f/static', vertex_positions),
                                    ('c3f/dynamic', (
                                                0, 1.0, 0,
                                                1.0, 0, 0,
                                                1.0, 0, 0,
                                                0, 1.0, 0
                                                )))
            self.blocks.append(block)

    def pop_blocks(self, damage):
        if damage > len(self.blocks):
            damage = len(self.blocks) - 1
        for i in range(damage):
            self.blocks[len(self.blocks) - 1].delete()
            self.blocks.pop()