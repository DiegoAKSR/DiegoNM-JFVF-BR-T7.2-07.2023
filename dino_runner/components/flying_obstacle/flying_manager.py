

from dino_runner.components.flying_obstacle.mosquito import Mosquito_per


class Flying_manager:
    def __init__(self):
        self.mosquito = Mosquito_per()
        self.list_mosquito = []

    def update(self, game):
        if len(self.list_mosquito) < 5:
            self.list_mosquito.append(self.mosquito)

        for mosq in self.list_mosquito:
            mosq.update(game)

    def draw(self, screen):
        for mosq in self.list_mosquito:
            mosq.draw(screen)
