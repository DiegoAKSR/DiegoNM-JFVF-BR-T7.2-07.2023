import pygame

from dino_runner.utils.constants import (ATTACKING, DUCKING, JUMPING,
                                         JUMPING_LEFT, RUNNING, RUNNING_LEFT)

X_POS = 0
Y_POS = 380
Y_POS_DUCK = 395
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
        self.person_left = False
        self.person_right = False
        self.person_attack = False

        self.jump_vel = JUMP_VEL

    def update(self, user_input):

        if user_input[pygame.K_UP]:
            self.person_jump = True
            self.person_run = False

        elif user_input[pygame.K_DOWN]:
            self.person_duck = True
            self.person_run = False

        elif not self.person_jump:
            self.person_run = True

        if user_input[pygame.K_LEFT]:
            self.person_left = True
            self.person_run = False

        if user_input[pygame.K_RIGHT]:
            self.person_right = True
            self.person_run = False

        if user_input[pygame.K_0]:
            self.person_attack = True

        if self.person_run:
            self.run()

        elif self.person_jump:
            self.jump()

        elif self.person_duck:
            self.duck()

        if self.person_left:
            self.move_left()
            if not self.person_jump:
                self.run_left()

        if self.person_right:
            self.move_right()
            if not self.person_jump:
                self.run()
        if self.person_attack:
            self.attack()

        if self.steps_count > 14:
            self.steps_count = 0

    def run(self):
        self.image = RUNNING[self.steps_count//2]
        self.person_rect.y = Y_POS
        self.steps_count += 1

    def run_left(self):
        self.image = RUNNING_LEFT[self.steps_count//2]
        self.person_rect.y = Y_POS
        self.steps_count += 1

    def duck(self):
        self.image = DUCKING[1]
        self.person_rect.y = Y_POS_DUCK

    def jump(self):
        self.image = JUMPING[self.steps_count//2]
        self.steps_count += 1

        if self.person_left:
            self.image = JUMPING_LEFT[self.steps_count//2]
        if self.person_jump:
            self.person_rect.y -= self.jump_vel*4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.person_rect.y = Y_POS
            self.person_jump = False
            self.jump_vel = JUMP_VEL

    def move_left(self):
        print("chegou left", self.person_rect.x)

        if self.person_rect.x >= 0:
            if self.person_left:
                self.person_rect.x -= 10
        self.person_left = False

    def move_right(self):
        print("chegou right", self.person_rect.x)
        if self.person_rect.x <= 1000:
            if self.person_right:
                self.person_rect.x += 7
        self.person_right = False

    def attack(self):
        print(self.steps_count)
        self.image = ATTACKING[self.steps_count//3]
        self.person_rect.y -= 15
        self.steps_count += 1
        if self.steps_count >= 13:
            self.person_attack = False
            self.steps_count = 0

    def draw(self, screen):
        screen.blit(self.image, (self.person_rect.x, self.person_rect.y))
