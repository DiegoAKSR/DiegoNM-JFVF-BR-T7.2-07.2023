import pygame

from dino_runner.utils.constants import (MENU_INICIO, MENU_PAUSE,
                                         MENU_PAUSE_DEAD, MENU_PAUSE_DEAD_0,
                                         SCREEN_HEIGHT, SCREEN_WIDTH)

FONT_STYLE = "freesansbold.ttf"


class Pause:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.show_menu = False
        self.image = MENU_PAUSE
        self.image_rect = self.image.get_rect()
        # FONT
        FONT_STYLE = "freesansbold.ttf"
        self.font = pygame.font.Font(FONT_STYLE, 22)

    def update(self, user_input, game):
        if user_input[pygame.K_p]:
            self.show_menu = True
            game.playing = False

        if self.show_menu:
            if user_input[pygame.K_c] or user_input[pygame.K_KP_ENTER]:
                self.show_menu = False

    def draw(self, screen, game):

        if self.show_menu:
            half_screen_height = SCREEN_HEIGHT // 2
            half_screen_width = SCREEN_WIDTH // 2
            self.image = MENU_PAUSE
            self.image_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(
                self.image, self.image_rect)

            text = self.font.render(
                f" {game.player.life_person}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width - 178,
                                half_screen_height - 192)
            self.screen.blit(text, text_rect)

            pygame.display.flip()
            game.handle_events_on_menu()

    def show_menu_1(self, game):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        self.image_rect.center = (half_screen_width, half_screen_height)
        if game.player.life_person == 3:
            self.image = MENU_INICIO
            self.screen.blit(
                self.image, (-10, -15))

        elif game.player.life_person == 0:
            self.image = MENU_PAUSE_DEAD_0
            self.image_rect.center = (
                half_screen_width, half_screen_height)
            self.screen.blit(
                self.image, self.image_rect)
            text = self.font.render(
                f" {game.player.life_person}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width - 178,
                                half_screen_height - 192)
            self.screen.blit(text, text_rect)

        elif game.player.life_person < 3:
            self.image = MENU_PAUSE_DEAD
            self.image_rect.center = (
                half_screen_width, half_screen_height)
            self.screen.blit(
                self.image, self.image_rect)

            text = self.font.render(
                f" {game.player.life_person}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width - 178,
                                half_screen_height - 192)
            self.screen.blit(text, text_rect)

        pygame.display.flip()

        game.handle_events_on_menu()


'''
def show_menu_1(self, game):
        game.screen.fill((255, 255, 255))

        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        FONT_STYLE = "freesansbold.ttf"
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render("Press ENTER to start", True, (0, 0, 0))

        text_rect = text.get_rect()
        text_rect.center = (half_screen_width, half_screen_height)
        game.screen.blit(text, text_rect)

        if game.player.life_person > 0:
            text = font.render(
                "Press C to continue", True, (0, 0, 0))
            text_rect.center = (half_screen_width, half_screen_height + 100)
            game.screen.blit(text, text_rect)

        game.death_count = game.player.life_person
        text = font.render(
            f"Remaining Lives: {game.death_count}", True, (0, 0, 0))
        text_rect.center = (150, 100)
        game.screen.blit(text, text_rect)

        pygame.display.flip()

        game.handle_events_on_menu()
    '''
