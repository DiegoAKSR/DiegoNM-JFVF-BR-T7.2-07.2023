import pygame

from dino_runner.components.background_manager import Background_manager
from dino_runner.components.flying_obstacle.flying_manager import \
    Flying_manager
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.pause_menu import Pause
from dino_runner.components.person import Person
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import (DEFAULT_TYPE, FPS, ICON, MENU_PAUSE,
                                         SCREEN_HEIGHT, SCREEN_WIDTH, TITLE)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 13
        self.player = Person()
        self.obstacle_manager = ObstacleManager()
        self.flying_manager = Flying_manager()
        self.backgroun_manager = Background_manager()
        ########################
        self.power_up_manager = PowerUpManager()
        self.pause_menu = Pause()

        # Pontuação
        self.score = 0

        self.reset = True
        self.pause = False

        self.player_life_person = self.player.life_person

    def execute(self):
        self.executing = True
        while self.executing:

            if self.pause_menu.show_menu:
                self.handle_events_on_menu()

            elif not self.playing:
                self.pause_menu.show_menu_1(self)

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        if self.reset:
            self.reset_game()

        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_game(self):
        self.score = 0
        self.game_speed = 13
        self.obstacle_manager.obstacles.clear()
        self.power_up_manager.reset_power_ups()
        self.flying_manager.list_mosquito.clear()
        self.player.person_life.cont = 0
        self.player.life_person = 3

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.obstacle_manager.update(self)
        self.flying_manager.update(self)  # chamando update do manager mosquito
        self.power_up_manager.update(self)
        self.pause_menu.update(user_input, self)
        self.update_score()

    def update_score(self):
        self.score += 1

        if self.score % 100 == 0:
            self.game_speed += 1

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))

        self.backgroun_manager.draw_background(self.screen)

        self.player.draw(self.screen)  # chamando draw do person
        self.obstacle_manager.draw(self.screen)
        self.flying_manager.draw(self.screen)  # chamando manager do mosquito
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        self.pause_menu.draw(self.screen, self)

        self.draw_score()

        # pygame.display.update()
        pygame.display.update()
        pygame.display.flip()

    def draw_score(self):
        FONT_STYLE = "freesansbold.ttf"
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0, 0, 0))

        text_rect = text.get_rect()
        text_rect.center = (1000, 50)

        self.screen.blit(text, text_rect)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round(
                (self.player.power_up_time_up - pygame.time.get_ticks())/1000, 2)

            if self.player.type == "default":
                if time_to_show >= 0:
                    FONT_STYLE = "freesansbold.ttf"
                    font = pygame.font.Font(FONT_STYLE, 22)
                    text = font.render(f"{time_to_show}", True, (0, 0, 0))

                    text_rect = text.get_rect()
                    text_rect.x = 500
                    text_rect.y = 50

                    self.screen.blit(text, text_rect)

                else:
                    self.player.has_power_up = False
                    self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    if self.pause_menu.show_menu or not self.player.life_person == 3:
                        if self.player.life_person > 0:
                            self.reset = False
                            self.pause = False
                            self.run()

                if event.key == pygame.K_KP_ENTER:
                    self.reset = True
                    self.pause = False
                    self.run()
