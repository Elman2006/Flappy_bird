# ===================================== Modules ==========================================
import pygame


# ====================================== Settings class ===================================
class Settings:
    """ To sort and manage all settings in game"""

    def __init__(self):
        # ------------------ Files -----------------------
        # Bird
        self.bg_img = pygame.transform.scale(
            pygame.image.load("../assets/img/bg2.png"),
            (310, 551)
        )
        self.bird_img_up = pygame.image.load("../assets/img/red_bird_up_flap.png")
        self.bird_img_mid = pygame.image.load("../assets/img/red_bird_mid_flap.png")
        self.bird_img_down = pygame.image.load("../assets/img/red_bird_down_flap.png")

        # Pipe
        self.pipe_img = pygame.image.load("../assets/img/pipe_red.png")
        self.pipe_speed_factor = 5
        self.pipe_range = 250

        # Sounds & font
        self.fly_sound = pygame.mixer.Sound("../assets/sound/wing.wav")
        self.die_sound = pygame.mixer.Sound("../assets/sound/die.wav")
        self.smb_stomp = pygame.mixer.Sound("../assets/sound/smb_stomp.wav")
        self.point_sound = pygame.mixer.Sound("../assets/sound/point.wav")
        self.flappy_font = pygame.font.Font("../assets/font/Flappy.TTF", 38)

        # Colors
        self.lynx_white = (245, 246, 250)

        # Screen
        self.screen_width = 310
        self.screen_height = 512
        self.screen_caption = "Flappy bird"
        self.fps = 60
        self.bg_img_x = 0
        self.increase_factor = 0.25

        # Floor & pipe
        self.floor_speed_factor = 1
        self.floor_x = 0
        self.floor_y = 440
        self.pipe_list = []

        # Bird
        self.bird_fly = -4
        self.bird_movement = 0
        self.gravity = 0.25
        self.bird_list = [
            self.bird_img_up,
            self.bird_img_mid,
            self.bird_img_down
        ]
        self.bird_list_index = 0
        self.bird_img = self.bird_list[self.bird_list_index]

        # States
        self.game_active = False
        self.score = 0
        self.high_score = 0

        # User events
        self.create_flap = pygame.USEREVENT
        self.create_pipe = pygame.USEREVENT + 1
        self.increase_game = pygame.USEREVENT + 2
        pygame.time.set_timer(self.create_flap, 400)
        pygame.time.set_timer(self.create_pipe, 1200)
        pygame.time.set_timer(self.increase_game, 15000)

    def initialize_dynamic_settings(self):
        self.score = 0
        self.pipe_range = 250
