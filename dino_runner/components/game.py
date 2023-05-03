import pygame

from dino_runner.components.flying_obstacle.flying_manager import \
    Flying_manager
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.person import Person
from dino_runner.utils.constants import (BG, FPS, ICON, SCREEN_HEIGHT,
                                         SCREEN_WIDTH, TITLE)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 13
        self.x_pos_bg = 0
        self.y_pos_bg = -230
        self.player = Person()
        self.obstacle_manager = ObstacleManager()
        self.flying_manager = Flying_manager()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)  # chamando metodo update do person
        self.obstacle_manager.update(self)
        self.flying_manager.update(self)  # chamando update do manager mosquito

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()

        self.player.draw(self.screen)  # chamando draw do person
        # self.cloud.draw_cloud_1(self.screen)  # chamando draw das novens
        # self.cloud.draw_cloud_2(self.screen)  # chamando draw das novens
        self.obstacle_manager.draw(self.screen)
        self.flying_manager.draw(self.screen)  # chamando manager do mosquito
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
