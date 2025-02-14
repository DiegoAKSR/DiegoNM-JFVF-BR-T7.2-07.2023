import os

import pygame

# Global Constants
TITLE = "Winifred the Running"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 40
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Constants for obstacle
OBSTACLE_Y_POS = 465

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

ATTACKING = [
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Attack/Attack_past_1/Attack_invok_1.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Attack/Attack_past_1/Attack_invok_2.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Attack/Attack_past_1/Attack_invok_3.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Attack/Attack_past_1/Attack_invok_4.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Attack/Attack_past_1/Attack_invok_5.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Attack/Attack_past_1/Attack_invok_6.png")),
]

ATTACKING_2 = [
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Attack/Attack_past_2/Attack_speed_1.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Attack/Attack_past_2/Attack_speed_2.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Attack/Attack_past_2/Attack_speed_3.png")),

]


RUNNING_LEFT = [
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Runner/Runner_Left/RunF_1.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Runner/Runner_Left/RunF_2.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Runner/Runner_Left/RunF_3.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Runner/Runner_Left/RunF_4.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Runner/Runner_Left/RunF_5.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Runner/Runner_Left/RunF_6.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Runner/Runner_Left/RunF_7.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Runner/Runner_Left/RunF_8.png")),

]
RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Runner/Run_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Runner/Run_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Runner/Run_3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Runner/Run_4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Runner/Run_5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Runner/Run_6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Runner/Run_7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Runner/Run_8.png")),

]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Runner/Run_1.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Runner/Run_2.png")),
]

JUMPING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Jumper/Jump_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Jumper/Jump_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Jumper/Jump_3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Jumper/Jump_4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Jumper/Jump_5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Jumper/Jump_6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Jumper/Jump_7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Jumper/Jump_8.png")),
]

JUMPING_LEFT = [
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Jumper/Jumper_left/JumpF_1.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Jumper/Jumper_left/JumpF_2.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Jumper/Jumper_left/JumpF_3.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Jumper/Jumper_left/JumpF_4.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Jumper/Jumper_left/JumpF_5.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Jumper/Jumper_left/JumpF_6.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Jumper/Jumper_left/JumpF_7.png")),
    pygame.image.load(os.path.join(
        IMG_DIR, "Dino/Jumper/Jumper_left/JumpF_8.png")),
]


DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Ducking/Duck.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Ducking/Duck.png")),
]


# CLOUDS
CLOUD_1 = pygame.image.load(os.path.join(
    IMG_DIR, 'Other/Clouds/NuvemP2Azul.png'))

CLOUD_2 = pygame.image.load(os.path.join(
    IMG_DIR, 'Other/Clouds/NuvemGrande.png'))

CLOUD_3 = [
    pygame.image.load(os.path.join(
        IMG_DIR, 'Other/Clouds/NuvemP2Azul.png')),
    pygame.image.load(os.path.join(
        IMG_DIR, 'Other/Clouds/NuvemGrande.png')),
    pygame.image.load(os.path.join(
        IMG_DIR, 'Other/Clouds/NuvemP2Azul.png')),
]

# OBSTACLES

STUMP = [pygame.image.load(os.path.join(
    IMG_DIR, 'Other/Obstacles/middle_lane_tree9.png')),
    pygame.image.load(os.path.join(
        IMG_DIR, 'Other/Obstacles/stumps_two.png')),
    pygame.image.load(os.path.join(
        IMG_DIR, 'Other/Obstacles/middle_lane_tree9.png')),
]

STUMP_LARGE = [pygame.image.load(os.path.join(
    IMG_DIR, 'Other/Obstacles/stump_large.png'))]


MOSQUITO = [
    pygame.image.load(os.path.join(IMG_DIR, 'mosquito/mosquito_11.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'mosquito/mosquito_22.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'mosquito/mosquito_33.png')),
]

# ICONS SWORDS
ICON_SWORD_ACTIVE = [pygame.image.load(os.path.join(IMG_DIR, 'Other/sword/sword.png')),
                     pygame.image.load(os.path.join(
                         IMG_DIR, 'Other/sword/sword_active.png')),
                     ]

ICON_SWORD_INATIVE = [pygame.image.load(os.path.join(IMG_DIR, 'Other/sword/sword_inative.png')),
                      pygame.image.load(os.path.join(
                          IMG_DIR, 'Other/sword/sword_inative_2.png')),
                      ]

ICON_SWORD_TWO_ACTIVE = [pygame.image.load(os.path.join(IMG_DIR, 'Other/sword/sword2.png')),
                         pygame.image.load(os.path.join(
                             IMG_DIR, 'Other/sword/sword2_active.png')),
                         ]

ICON_SWORD_TWO_INATIVE = [pygame.image.load(os.path.join(IMG_DIR, 'Other/sword/sword2_inative.png')),
                          pygame.image.load(os.path.join(
                              IMG_DIR, 'Other/sword/sword2_inative_2.png')),
                          ]


# SHIELD

SHIELD = pygame.image.load(os.path.join(
    IMG_DIR, 'Other/power_up_img/Icon7.png'))

ICON_SHIELD = [pygame.image.load(os.path.join(
    IMG_DIR, 'Other/power_up_img/shield.png')),
    pygame.image.load(os.path.join(
        IMG_DIR, 'Other/power_up_img/shield.png')),
]

ICON_LIFE_UP = pygame.image.load(os.path.join(
    IMG_DIR, 'Other/power_up_img/Icon1.png'))

HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

########### BACKGROUND###############################
BG_2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/mapa3.png'))
BG_TER = pygame.image.load(os.path.join(IMG_DIR, 'Other/mapa3_ter.png'))
BG_CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud_2.png'))
#####################################################################


HEART_LIFE = [pygame.image.load(os.path.join(IMG_DIR, 'life/life_3.png')),
              pygame.image.load(os.path.join(IMG_DIR, 'life/life_2.png')),
              pygame.image.load(os.path.join(IMG_DIR, 'life/life_1.png')),
              pygame.image.load(os.path.join(IMG_DIR, 'life/life_0.png')),
              pygame.image.load(os.path.join(IMG_DIR, 'life/life_01.png')),
              ]

DEAD_PERSON = [pygame.image.load(os.path.join(IMG_DIR, 'Dino/Dead/dead_1.png')),
               pygame.image.load(os.path.join(
                   IMG_DIR, 'Dino/Dead/dead_2.png')),
               pygame.image.load(os.path.join(
                   IMG_DIR, 'Dino/Dead/dead_3.png')),
               pygame.image.load(os.path.join(
                   IMG_DIR, 'Dino/Dead/dead_4.png')),
               pygame.image.load(os.path.join(
                   IMG_DIR, 'Dino/Dead/dead_5.png')),
               pygame.image.load(os.path.join(
                   IMG_DIR, 'Dino/Dead/dead_5.png')),


               ]

MENU_INICIO = pygame.image.load(os.path.join(
    IMG_DIR, 'Other/menu/2.png'))

MENU_PAUSE = pygame.image.load(os.path.join(
    IMG_DIR, 'Other/menu/menu_pause_1.png'))


MENU_PAUSE_DEAD = pygame.image.load(os.path.join(
    IMG_DIR, 'Other/menu/menu_dead.png'))

MENU_PAUSE_DEAD_0 = pygame.image.load(os.path.join(
    IMG_DIR, 'Other/menu/menu_dead_0.png'))

DEFAULT_TYPE = "default"
LIFE_TYPE = "life"
