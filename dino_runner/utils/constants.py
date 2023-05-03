import os

import pygame

# Global Constants
TITLE = "Chrome Dino Runner"
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

JUMPING_SHIELD = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Ducking/Duck.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Ducking/Duck.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
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
    pygame.image.load(os.path.join(IMG_DIR, 'mosquito/mosquito_1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'mosquito/mosquito_2.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'mosquito/mosquito_3.png')),
]

####################

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

# BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
# BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Mapa1.png'))
BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/mapa2.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
