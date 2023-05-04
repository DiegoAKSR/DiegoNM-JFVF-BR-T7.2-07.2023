import pygame

from dino_runner.utils.constants import MOSQUITO

X_POS = 1500
Y_POS = 440


'''class Mosquito(Flying_obstacle):
    def __init__(self, image):
        super().__init__(image)'''


class Mosquito_per:
    def __init__(self):
        self.image = MOSQUITO[0]
        self.mosquito_rect = self.image.get_rect()
        self.mosquito_rect.x = float(X_POS)
        self.mosquito_rect.y = Y_POS

        self.steps_count = 0
        self.list_mosquitos = []
        self.mosquito_move1 = False
        self.mosquito_move2 = False
        self.runer = True

        self.collisions = 0
        self.last_collision_resolved = True

    def update(self, game):

        if self.runer == True:
            self.run()

        if self.mosquito_rect.y == 440:
            self.mosquito_move1 = False
            self.mosquito_move2 = True

        if self.mosquito_rect.y == 300:
            self.mosquito_move2 = False
            self.mosquito_move1 = True

        if self.mosquito_move1:

            self.move1()

        if self.mosquito_move2:

            self.move2()

        if game.player.person_rect.colliderect(self.mosquito_rect):
            if self.last_collision_resolved:
                self.collisions += 1
                print(self.collisions)
                game.player.person_life.cont += 1
                self.last_collision_resolved = False
        else:
            self.last_collision_resolved = True

        '''if game.player.person_rect.colliderect(self.mosquito_rect):

            if game.player.person_attack == True:

                print('top')

            else:
                pass
                # game.life.cont += 1
                # pygame.time.delay(10)
                # game.playing = False
'''
        if self.steps_count > 5:
            self.steps_count = 0

    def move1(self):
        self.mosquito_rect.y += float(0.7)

    def move2(self):
        self.mosquito_rect.y -= float(0.7)

    def run(self):
        self.image = MOSQUITO[self.steps_count//2]
        # self.mosquito_rect.y = Y_POS
        self.steps_count += 1
        self.mosquito_rect.x -= 3
        if self.mosquito_rect.x < -50:
            self.mosquito_rect.x = X_POS

    def mosquito_dead(self):
        pass

    def draw(self, screen):
        screen.blit(
            self.image, (self.mosquito_rect.x, self.mosquito_rect.y))
