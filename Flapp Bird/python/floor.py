# ===================================== Modules =========================================
import pygame.image


# ================================== Floor class ============================================
class Floor:
    """ To make floor object """

    def __init__(
            self,
            ai_settings,
            screen
    ):
        """ Initialize the floor attributes """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Load the floor image and get it rects
        self.image = pygame.image.load("../assets/img/floor.png")
        self.rect = self.image.get_rect()

    def blit_floor1(self):
        """ Show the first floor image to screen"""
        self.screen.blit(
            self.image,
            (self.ai_settings.floor_x,
             self.ai_settings.floor_y)
        )

    def blit_floor2(self):
        """ Show the second floor to the screen """
        self.screen.blit(
            self.image,
            (self.ai_settings.floor_x + 336,
             self.ai_settings.floor_y)
        )

    def update_floor(self):
        """ Make a floor movement """
        self.ai_settings.floor_x -= self.ai_settings.floor_speed_factor

        # Reset the loop
        if self.ai_settings.floor_x <= -336:
            self.ai_settings.floor_x = 0
