import pygame

from dino_runner.utils.constants import (BG_2, BG_CLOUD, BG_TER, SCREEN_HEIGHT,
                                         SCREEN_WIDTH)


class Background_manager:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game_speed = 13
        self.x_pos_bg = 0
        self.x_pos_bg_ter = 0
        self.x_pos_bg_cloud = 0
        self.y_pos_bg = -230
        self.y_pos_bg_ter = 520
        self.y_pos_bg_cloud = -150

    def draw_background(self, screen):
        self.draw_cloud(self.screen)
        self.draw_background_2(self.screen)
        self.draw_background_ter(self.screen)

    def draw_cloud(self, screen):
        self.screen.fill((8, 166, 213))
        image_width = BG_CLOUD.get_width()
        self.screen.blit(BG_CLOUD, (self.x_pos_bg_cloud, self.y_pos_bg_cloud))
        self.screen.blit(
            BG_CLOUD, (image_width + self.x_pos_bg_cloud, self.y_pos_bg_cloud))
        if self.x_pos_bg_cloud <= -image_width:
            self.screen.blit(
                BG_CLOUD, (image_width + self.x_pos_bg_cloud, self.y_pos_bg_cloud))
            self.x_pos_bg_cloud = 0
        self.x_pos_bg_cloud -= (self.game_speed / 4)

    def draw_background_ter(self, screen):
        image_width = BG_TER.get_width()
        self.screen.blit(BG_TER, (self.x_pos_bg_ter, self.y_pos_bg_ter))
        self.screen.blit(
            BG_TER, (image_width + self.x_pos_bg_ter, self.y_pos_bg_ter))
        if self.x_pos_bg_ter <= -image_width:
            self.screen.blit(
                BG_TER, (image_width + self.x_pos_bg_ter, self.y_pos_bg_ter))
            self.x_pos_bg_ter = 0
        self.x_pos_bg_ter -= self.game_speed

    def draw_background_2(self, screen):

        image_width = BG_2.get_width()
        self.screen.blit(BG_2, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG_2, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(
                BG_2, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= (self.game_speed / 2)
