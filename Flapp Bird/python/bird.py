class Bird:
    """ A class to manage and control bird"""

    def __init__(
            self,
            ai_settings,
            screen
    ):
        """ Initialize bird attributes"""

        # Objects
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Load the bird image and get its rect
        self.image = ai_settings.bird_img
        self.rect = self.image.get_rect()

        # Set the position of bird
        self.rect.top = 8 * self.rect.height
        self.rect.left = self.rect.width

    def replace_bird(self):
        self.rect.top = 8 * self.rect.height
        self.rect.left = self.rect.width
        self.ai_settings.bird_movement = 0

    def blit_bird(self):
        """ Show the bird to screen"""
        self.screen.blit(
            self.image,
            self.rect
        )
