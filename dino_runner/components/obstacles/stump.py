from dino_runner.components.obstacles.obstacle import Obstacle


class Stump(Obstacle):
    def __init__(self, image):
        super().__init__(image)


class Stump_large(Obstacle):
    def __init__(self, image):
        super().__init__(image)
        self.rect.y = 475
