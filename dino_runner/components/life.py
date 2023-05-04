
from dino_runner.utils.constants import HEART_LIFE, SCREEN_HEIGHT, SCREEN_WIDTH


class Life:
    def __init__(self):
        self.image = HEART_LIFE[0]
        self.image_rect = self.image.get_rect()
        self.image_rect.x = 20
        self.image_rect.y = 20
        self.cont = 0
        self.dead = False

    def damage_life(self):
        self.image = HEART_LIFE[self.cont]
        if self.cont == 3:
            self.cont += 1
            self.dead = True

    def draw(self, screen):
        screen.blit(
            self.image, (self.image_rect.x, self.image_rect.y))
