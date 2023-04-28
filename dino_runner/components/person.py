import pygame

from dino_runner.utils.constants import DUCKING, JUMPING, RUNNING

X_POS = 0
Y_POS = 315
Y_POS_DUCK = 340
JUMP_VEL = 8.5


class Person:
    def __init__(self):
        self.image = RUNNING[0]
        self.person_rect = self.image.get_rect()
        self.person_rect.x = X_POS
        self.person_rect.y = Y_POS

        self.steps_count = 0
        self.person_run = True
        self.person_jump = False
        self.person_duck = False

        self.jump_vel = JUMP_VEL

    def update(self, user_input):

        if user_input[pygame.K_UP]:
            self.person_jump = True
            self.person_run = False
        elif user_input[pygame.K_UP]:
            self.person_duck = True
            self.person_run = False
        elif user_input[pygame.K_DOWN]:
            self.person_duck = True
            self.person_run = False
        elif not self.person_jump:
            self.person_run = True

        if self.person_run:
            self.run()

        elif self.person_jump:
            self.jump()

        elif self.person_duck:
            self.duck()

        if self.steps_count > 9:
            self.steps_count = 0

    def run(self):
        self.image = RUNNING[self.steps_count//5]
        self.person_rect.y = Y_POS
        self.steps_count += 1

    def duck(self):
        self.image = DUCKING[self.steps_count//5]
        self.person_rect.y = Y_POS_DUCK
        self.steps_count += 1

    def jump(self):
        self.image = JUMPING

        if self.person_jump:
            self.person_rect.y -= self.jump_vel*4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.person_rect.y = Y_POS
            self.person_jump = False
            self.jump_vel = JUMP_VEL

    def draw(self, screen):
        screen.blit(self.image, (self.person_rect.x, self.person_rect.y))
