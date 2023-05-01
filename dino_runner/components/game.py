import pygame

from dino_runner.components.person import Person
from dino_runner.components.scenery_items import Scenary_Itens
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
        self.cloud = Scenary_Itens()

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

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()

        self.player.draw(self.screen)  # chamando draw do person
        self.cloud.draw_cloud_1(self.screen)  # chamando draw das novens
        self.cloud.draw_cloud_2(self.screen)  # chamando draw das novens
        self.cloud.draw_obs_tree(self.screen)  # chamando draw do EVIL
        self.cloud.draw_obs_tree_2(self.screen)  # chamando draw do EVIL

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
