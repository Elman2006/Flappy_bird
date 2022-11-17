import random
import pygame.transform


class Pipes:
    """ A class to manage and create pipes"""

    def __init__(self, ai_settings, screen):
        """ Initialize attributes """
        self.ai_settings = ai_settings
        self.screen = screen

    def generate_pipe_rect(self):
        """ return the pipe rect to a dictionary"""
        random_pipes = random.randrange(250, 350)
        pipe_rect_bottom = self.ai_settings.pipe_img.get_rect(midtop=(700, random_pipes))
        pipe_rect_top = self.ai_settings.pipe_img.get_rect(midbottom=(700, random_pipes - 150))
        return pipe_rect_top, pipe_rect_bottom

    def display_pipes(self, pipes):
        """ Blit the pipes to the screen"""
        for pipe in pipes:
            if pipe.bottom >= self.ai_settings.pipe_range:
                self.screen.blit(self.ai_settings.pipe_img, pipe)
            else:
                reversed_pipes = pygame.transform.flip(self.ai_settings.pipe_img, False, True)
                self.screen.blit(reversed_pipes, pipe)
