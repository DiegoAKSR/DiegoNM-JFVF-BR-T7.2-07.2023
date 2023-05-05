import pygame

from dino_runner.utils.constants import (ICON_SHIELD, ICON_SWORD_ACTIVE,
                                         ICON_SWORD_INATIVE,
                                         ICON_SWORD_TWO_ACTIVE,
                                         ICON_SWORD_TWO_INATIVE)


class Icons:
    def __init__(self):
        # sword one
        self.image = ICON_SWORD_ACTIVE[0]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = 120
        self.image_rect.y = 10
        self.count = 0
        self.inative_show = 0
        self.active_set = False
        self.score_sword_one = 0
        # sword two
        self.image_2 = ICON_SWORD_TWO_ACTIVE[0]
        self.image_2_rect = self.image_2.get_rect()
        self.image_2_rect.x = 175
        self.inative_show_2 = 0
        self.active_set_2 = False
        self.score_sword_two = 0

        # icon shield
        self.image_shield = ICON_SHIELD[0]
        self.image_shield_rect = self.image_shield.get_rect()
        self.image_shield_rect.x = 230

    def update(self, game):

        if self.active_set:
            self.active_one()
        else:
            self.inative_one()

        if self.active_set_2:
            self.active_two()

        else:
            self.inative_two()

        if self.score_sword_one >= 150:
            self.active_set = True

        if self.score_sword_two >= 150:
            self.active_set_2 = True

        if game.player.person_attack:
            if self.active_set:
                self.score_sword_one = 0
                self.active_set = False
            else:
                self.inative_show = 1
                self.inative_one()

        if game.player.person_attack_2:
            if self.active_set_2:
                self.score_sword_two = 0
                self.active_set_2 = False
            else:
                self.inative_show_2 = 1
                self.inative_two()

        self.score_sword_one += 1
        self.score_sword_two += 1

        self.inative_show = 0
        self.inative_show_2 = 0

        self.count += 1
        if self.count > 40:
            self.count = 0

    # ICONS SWORD
    def active_one(self):
        self.image = ICON_SWORD_ACTIVE[self.count//21]

    def active_two(self):
        self.image_2 = ICON_SWORD_TWO_ACTIVE[self.count//21]

    def inative_one(self):
        self.image = ICON_SWORD_INATIVE[self.inative_show]

    def inative_two(self):
        self.image_2 = ICON_SWORD_TWO_INATIVE[self.inative_show_2]

    # ICONS SHIELD
    def icon_shield_draw(self, screen):
        screen.blit(
            self.image_shield, (self.image_shield_rect.x, self.image_rect.y))

    def draw(self, screen):
        screen.blit(
            self.image, (self.image_rect.x, self.image_rect.y))
        screen.blit(
            self.image_2, (self.image_2_rect.x, self.image_rect.y))
