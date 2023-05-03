import random

import pygame

from dino_runner.components.obstacles.stump import Stump, Stump_large
from dino_runner.utils.constants import STUMP, STUMP_LARGE


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

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
                pygame.time.delay(10)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
