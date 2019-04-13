#./src/Camera.py
import pyglet
from pyglet.gl import *

class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.texture = pyglet.image.Texture.create(self.width, self.height)
    
    def __enter__(self):
        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, self.width, 0, self.height, -1, 1)
        glMatrixMode(GL_MODELVIEW)

    @staticmethod
    def set(x=0, y=0, z=0):
        glTranslatef(int(-x), int(-y), int(-z))

    def __exit__(self, *args):
        buffer = pyglet.image.get_buffer_manager().get_color_buffer()
        self.texture.blit_into(buffer, 0, 0, 0)

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        glColor3f(1.0, 1.0, 1.0)

        self.texture.blit(0, 0, width=self.width, height=self.height)

