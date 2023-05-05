from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import (DEFAULT_TYPE, ICON_LIFE_UP, LIFE_TYPE,
                                         SHIELD)


class Shield(PowerUp):
    def __init__(self):
        super().__init__(SHIELD, DEFAULT_TYPE)


class Life_uper(PowerUp):
    def __init__(self):
        super().__init__(ICON_LIFE_UP, LIFE_TYPE)
