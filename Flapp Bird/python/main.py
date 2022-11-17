# ========================================= Modules ============================================
# --------------------------------------- External modules --------------------------------------
import pygame

# ------------------------------------ Game modules --------------------------------------------
from settings import Settings
import game_functions as gf
from floor import Floor
from bird import Bird
# from state import States
from score_board import Scoreboard
from pipes import Pipes


# ===================================== Main function ===========================================
def run_game():
    """ A function to run the game"""

    # --------------------------- Objects ---------------------------------
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    floor = Floor(ai_settings, screen)
    bird = Bird(ai_settings, screen)
    clock = pygame.time.Clock()
    # state = States()
    sb = Scoreboard(ai_settings, screen)
    pipes = Pipes(ai_settings, screen)
    pygame.time.set_timer(ai_settings.create_flap, 90)

    # --------------------------- Main loop -------------------------------
    while True:
        # Make and frame rate per second
        clock.tick(ai_settings.fps)

        # Check for events
        gf.check_events(ai_settings, bird, pipes)

        # Start
        if not ai_settings.game_active:
            screen.blit(ai_settings.bg_img, (ai_settings.bg_img_x, 0))
            floor.blit_floor1()
            sb.show_states()

        if ai_settings.game_active:
            gf.bg_movement(ai_settings, screen)
            gf.bird_movement_f(ai_settings, bird)
            ai_settings.pipe_list = gf.move_pipes(ai_settings)
            pipes.display_pipes(ai_settings.pipe_list)
            gf.floor_movement(floor)
            gf.update_scores(ai_settings, sb)

        sb.show_score()

        # Update to most recently screen
        gf.update_screen(ai_settings, bird)


# ------------------------------------- call function ----------------------------------------
run_game()
