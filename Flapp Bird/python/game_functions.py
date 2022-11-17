import pygame
from sys import exit
from time import sleep


# ====================================== Events function =========================================
def check_keydown(
        ai_settings,
        bird,
        event
):
    """ To check what keys that gamer pressed """

    # Quit the game
    if event.key == pygame.K_ESCAPE:
        exit()

    # Fly with pressing key
    if (event.key == pygame.K_RCTRL or event.key == pygame.K_SPACE) and ai_settings.game_active:
        ai_settings.fly_sound.play()
        ai_settings.bird_movement = 0
        ai_settings.bird_movement += ai_settings.bird_fly

    # Start game
    elif event.key == pygame.K_p and not ai_settings.game_active:
        ai_settings.initialize_dynamic_settings()
        bird.replace_bird()
        ai_settings.game_active = True


def check_events(
        ai_settings,
        bird,
        pipes
):
    """ To check all events in the game"""
    for event in pygame.event.get():

        # Quit form the game
        if event.type == pygame.QUIT:
            exit()

        # keydown events
        elif event.type == pygame.KEYDOWN:
            check_keydown(
                ai_settings,
                bird,
                event
            )

        # Creat flap
        elif event.type == ai_settings.create_flap and ai_settings.game_active:

            if ai_settings.bird_list_index < 2:
                ai_settings.bird_list_index += 1
            elif ai_settings.bird_list_index == 2:
                ai_settings.bird_list_index = 0

            bird.image = bird_animation(ai_settings)

        # Creat pipe
        elif event.type == ai_settings.create_pipe and ai_settings.game_active:
            ai_settings.pipe_list.extend(pipes.generate_pipe_rect())

        # Increase game
        # TODO: Not finished
        # elif event.type == ai_settings.increase_game and ai_settings.game_active:
        #     if ai_settings.pipe_range <= 300:
        #         ai_settings.pipe_range += 2


# ========================================= Collision =========================================
def game_over(
    ai_settings
):
    """ To show what will happen in when the game ends """
    ai_settings.die_sound.play()
    sleep(1.2)
    ai_settings.floor_x = 0
    ai_settings.pipe_list.clear()
    ai_settings.game_active = False


def check_edge(
        ai_settings,
        bird
):
    """ To check that is bird out of screen or collide with floor """
    for pipe in ai_settings.pipe_list:
        if bird.rect.colliderect(pipe) and ai_settings.game_active:
            game_over(ai_settings)

    if bird.rect.bottom >= ai_settings.floor_y + 10 and ai_settings.game_active:
        game_over(ai_settings)

    elif bird.rect.top <= -3 and ai_settings.game_active:
        game_over(ai_settings)


# ==================================== Movements ================================================
def bg_movement(
        ai_settings,
        screen,
):
    """ Make a background that can move and set the settings """

    # Blit the backgrounds
    screen.blit(ai_settings.bg_img, (ai_settings.bg_img_x, 0))
    screen.blit(ai_settings.bg_img, (ai_settings.bg_img_x + 288, 0))

    # Move the backgrounds to left
    ai_settings.bg_img_x -= ai_settings.floor_speed_factor

    # Reset the movement
    if ai_settings.bg_img_x <= -288:
        ai_settings.bg_img_x = 0


def bird_movement_f(
        ai_settings,
        bird
):
    # Show the bird
    bird.blit_bird()
    bird.rect.centery += ai_settings.bird_movement
    ai_settings.bird_movement += ai_settings.gravity


def bird_animation(ai_settings):
    ai_settings.bird_img = ai_settings.bird_list[ai_settings.bird_list_index]
    return ai_settings.bird_img


def floor_movement(
        floor
):

    # Make floor and floor movement
    floor.blit_floor1()
    floor.blit_floor2()
    floor.update_floor()


# ======================================== Pipes ===============================================
def move_pipes(ai_settings):
    """ Moving the pipes """
    for pipe in ai_settings.pipe_list:
        pipe.centerx -= ai_settings.pipe_speed_factor
    inside_pipes = [pipe for pipe in ai_settings.pipe_list if pipe.right > -50]
    return inside_pipes


# ======================================= Score =======================================
def update_scores(
        ai_settings,
        sb
):
    for pipe in ai_settings.pipe_list:
        if pipe.right == 31:
            # TODO Increase the game
            ai_settings.score += 0.5
            ai_settings.smb_stomp.play()

        elif ai_settings.score >= ai_settings.high_score:
            ai_settings.high_score = ai_settings.score

    sb.prep_high_score()
    sb.prep_score()


# ===================================== Screen functions ============================================
def update_screen(
        ai_settings,
        bird
):
    """ Make to most recently screen"""

    # Set the caption and icon
    pygame.display.set_caption(ai_settings.screen_caption)
    pygame.display.set_icon(ai_settings.bird_img_up)

    check_edge(ai_settings, bird)
    # update to most recently screen
    pygame.display.flip()
