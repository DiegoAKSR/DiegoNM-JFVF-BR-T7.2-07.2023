

from dino_runner.components.flying_obstacle.mosquito import Mosquito_per


class Flying_manager:
    def __init__(self):
        self.mosquito = Mosquito_per()
        self.list_mosquito = []

    def update(self, game):

        # self.temp_list = []

        if len(self.list_mosquito) < 5:
            self.list_mosquito.append(self.mosquito)

        for mosq in self.list_mosquito:
            mosq.update(game)
            ''' if game.player.person_rect.colliderect(mosq.mosquito_rect):
                if game.player.has_power_up or game.player.type == "default":
                    self.temp_list.remove(mosq)

            self.list_mosquito = self.temp_list'''

    def draw(self, screen):
        for mosq in self.list_mosquito:
            mosq.draw(screen)
