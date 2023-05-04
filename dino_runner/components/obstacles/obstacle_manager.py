import random

import pygame

from dino_runner.components.obstacles.stump import Stump, Stump_large
from dino_runner.utils.constants import STUMP, STUMP_LARGE


class ObstacleManager:

    def __init__(self):
        self.obstacles = []
        self.collisions = 0
        self.last_collision_resolved = True

    def update(self, game):
        if len(self.obstacles) == 0:

            self.rand = random.randint(0, 1)

            if self.rand == 0:
                self.obstacles.append(Stump(STUMP[random.randint(0, 2)]))

            elif self.rand == 1:
                self.obstacles.append(Stump_large(STUMP_LARGE[0]))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.person_rect.colliderect(obstacle.rect):
                if self.last_collision_resolved:
                    self.collisions += 1
                    print(self.collisions)
                    game.player.person_life.cont += 1
                    self.last_collision_resolved = False
            else:
                self.last_collision_resolved = True

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
