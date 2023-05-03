

from dino_runner.utils.constants import CLOUD_1, CLOUD_2

X_POS = 1300
Y_POS = 40
X_POS_1 = 1500
Y_POS_EVIL = 450


class Scenary_Itens:
    def __init__(self):
        self.image_2 = CLOUD_2
        self.cloud_rect = self.image_2.get_rect()
        self.cloud_rect.x = X_POS
        self.cloud_rect.y = Y_POS

        self.image_1 = CLOUD_1
        self.cloud_rect_1 = self.image_1.get_rect()
        self.cloud_rect_1.x = X_POS_1
        self.cloud_rect_1.y = Y_POS

        self.cloud_speed = 13
        self.steps_count = 0

    def update(self):
        pass

    def draw_cloud_2(self, screen):
        self.steps_count -= self.cloud_speed
        self.cloud_rect.x = self.steps_count
        if self.steps_count <= -500:
            self.steps_count = 1300
        screen.blit(self.image_2,
                    (self.cloud_rect.x, self.cloud_rect.y))

    def draw_cloud_1(self, screen):
        self.cloud_rect_1.x -= self.cloud_speed
        if self.cloud_rect_1.x <= -300:
            self.cloud_rect_1.x = 1350
        screen.blit(self.image_1,
                    (self.cloud_rect_1.x, self.cloud_rect_1.y))
