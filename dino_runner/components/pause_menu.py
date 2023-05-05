import pygame

from dino_runner.utils.constants import MENU_PAUSE, SCREEN_HEIGHT, SCREEN_WIDTH


class Pause:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.show_menu = False
        self.image = MENU_PAUSE
        self.image_rect = self.image.get_rect()
       # self.image_rect.x = 0
        # self.image_rect.y = 0

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

            self.image_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(
                self.image, self.image_rect)

            FONT_STYLE = "freesansbold.ttf"
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render(
                f" {game.death_count}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width - 178,
                                half_screen_height - 192)
            self.screen.blit(text, text_rect)

            game.death_count = game.player.life_person
            pygame.display.flip()
            game.handle_events_on_menu()
