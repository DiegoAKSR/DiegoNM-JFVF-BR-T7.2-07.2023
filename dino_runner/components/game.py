import pygame

from dino_runner.components.flying_obstacle.flying_manager import \
    Flying_manager
from dino_runner.components.life import Life
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.person import Person
from dino_runner.utils.constants import (BG, BG_2, BG_CLOUD, BG_TER, FPS, ICON,
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
        self.x_pos_bg = 0
        self.x_pos_bg_ter = 0
        self.x_pos_bg_cloud = 0
        self.y_pos_bg = -230
        self.y_pos_bg_ter = 520
        self.y_pos_bg_cloud = -150
        self.player = Person()
        self.obstacle_manager = ObstacleManager()
        self.flying_manager = Flying_manager()

        # Pontuação
        self.score = 0

    def execute(self):
        self.executing = True

        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_game(self):
        self.score = 0
        self.game_speed = 13
        self.obstacle_manager.obstacles.clear()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        # chamando metodo update do person
        self.player.update(user_input, self)
        self.obstacle_manager.update(self)
        self.flying_manager.update(self)  # chamando update do manager mosquito
        self.update_score()

    def update_score(self):
        self.score += 1

        if self.score % 100 == 0:
            self.game_speed += 1

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()

        self.player.draw(self.screen)  # chamando draw do person
        self.obstacle_manager.draw(self.screen)
        self.flying_manager.draw(self.screen)  # chamando manager do mosquito
        self.draw_score()

        pygame.display.update()
        pygame.display.flip()

    def draw_score(self):
        FONT_STYLE = "freesansbold.ttf"
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0, 0, 0))

        text_rect = text.get_rect()
        text_rect.center = (1000, 50)

        self.screen.blit(text, text_rect)

    ###########
    '''def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed'''

    def draw_background(self):
        self.draw_cloud()
        self.draw_background_2()
        self.draw_background_ter()

    def draw_cloud(self):
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

    def draw_background_ter(self):
        image_width = BG_TER.get_width()
        self.screen.blit(BG_TER, (self.x_pos_bg_ter, self.y_pos_bg_ter))
        self.screen.blit(
            BG_TER, (image_width + self.x_pos_bg_ter, self.y_pos_bg_ter))
        if self.x_pos_bg_ter <= -image_width:
            self.screen.blit(
                BG_TER, (image_width + self.x_pos_bg_ter, self.y_pos_bg_ter))
            self.x_pos_bg_ter = 0
        self.x_pos_bg_ter -= self.game_speed

    def draw_background_2(self):

        image_width = BG_2.get_width()
        self.screen.blit(BG_2, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG_2, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(
                BG_2, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= (self.game_speed / 2)
    ##############################

    def show_menu(self):
        self.screen.fill((255, 255, 255))

        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        FONT_STYLE = "freesansbold.ttf"
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render("Press any key to start", True, (0, 0, 0))

        text_rect = text.get_rect()
        text_rect.center = (half_screen_width, half_screen_height)
        self.screen.blit(text, text_rect)

        self.death_count = "dfsdfsd"
        text = font.render(f"Death: {self.death_count}", True, (255, 0, 0))
        text_rect.center = (100, 100)
        self.screen.blit(text, text_rect)

        pygame.display.flip()

        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

            elif event.type == pygame.KEYDOWN:
                self.run()
