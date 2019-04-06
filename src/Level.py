#./src/Level.py
import pyglet
from pyglet.gl import *
import os
import pytmx
from pytmx.util_pyglet import load_pyglet
from src.sprites.player.Player import Player
from src.sprites.enemies.Enemy import Enemy
from src.sprites.enemies.ShootingEnemy import ShootingEnemy
from src.physics import detect_platform_collision, detect_world_bounds, detect_blockers

class Level:
    def __init__(self):
        path = os.path.abspath("resources/tilemaps/level.tmx")
        self.tilemap = load_pyglet(path)
        self.height = self.tilemap.height * self.tilemap.tileheight
        self.platforms = self.tilemap.get_layer_by_name('platforms')
        self.walls = self.tilemap.get_layer_by_name('walls')
        self.blockers = self.tilemap.get_layer_by_name('blockers')
        self.tilemap_batch = pyglet.graphics.Batch()
        self.sprite_batch = pyglet.graphics.Batch()
        self.platform_layer = pyglet.graphics.OrderedGroup(0)
        self.sprite_layer = pyglet.graphics.OrderedGroup(1)
        self.texture_atlas = pyglet.image.atlas.TextureAtlas(width=128, height=32)
        self.player = None
        self.enemies = []
        self.enemy_targets = []
        self.load_map()

    def load_map(self):
        texture_gid_dict = {}
        for layer in self.tilemap.visible_tile_layers:
            for x, y, gid in self.tilemap.layers[layer]:
                x *= self.tilemap.tilewidth
                y = int(self.height - ((y + 1) * self.tilemap.tileheight))
                vertex_positions = [
                    x + self.tilemap.tilewidth, y + self.tilemap.tileheight,
                    x, y + self.tilemap.tileheight,
                    x, y,
                    x + self.tilemap.tilewidth, y
                ]
                if gid not in texture_gid_dict and gid != 0:
                    image = self.tilemap.get_tile_image_by_gid(gid)
                    atlas_image = self.texture_atlas.add(image)
                    atlas_image.tex_coords = (
                        atlas_image.tex_coords[6],
                        atlas_image.tex_coords[10],
                        0.0,
                        atlas_image.tex_coords[9],
                        atlas_image.tex_coords[7],
                        0.0,
                        atlas_image.tex_coords[0],
                        atlas_image.tex_coords[4],
                        0.0,
                        atlas_image.tex_coords[3],
                        atlas_image.tex_coords[1],
                        0.0
                    )
                    texture_gid_dict[gid] = atlas_image.tex_coords
                if gid != 0:
                    self.tilemap_batch.add(4, GL_QUADS, self.platform_layer,
                                            ('v2f/static', vertex_positions),
                                            ('t3f/static', texture_gid_dict[gid]))
        for group in self.tilemap.visible_object_groups:
            for obj in self.tilemap.layers[group]:
                obj.y = int(self.height - obj.y - obj.height)
                if obj.name == "player":
                    self.player = Player(
                        obj.x, obj.y, 
                        targets=self.enemies, 
                        batch=self.tilemap_batch, 
                        group=self.sprite_layer
                    )
                    self.enemy_targets.append(self.player)
                elif obj.name == "enemy":
                    if obj.type == "shooting":
                        enemy = ShootingEnemy(
                            obj.x, obj.y, 
                            targets=self.enemy_targets,
                            batch=self.tilemap_batch,
                            is_patrolling=obj.properties.get('patrolling'),
                            group=self.sprite_layer
                        )
                    else:
                        enemy = Enemy(
                            obj.x, obj.y,
                            is_patrolling=obj.properties.get('patrolling'),
                            batch=self.tilemap_batch,
                            group=self.sprite_layer
                        )
                    self.enemies.append(enemy)

    def update(self, dt):
        self.player.updateAll(dt)
        detect_platform_collision(self.platforms, self.player)
        detect_world_bounds(self.walls, self.player)
        for enemy in self.enemies:
            enemy.updateAll(dt)
            detect_platform_collision(self.platforms, enemy)
            detect_blockers(self.blockers, enemy)
            detect_world_bounds(self.walls, enemy, enemies=self.enemies)

    def draw(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture_atlas.texture.id)
        self.tilemap_batch.draw()
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_BLEND)

