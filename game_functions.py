#Here we will put all main game functions here
import sys #we will need sys so the user can quit
import pygame

def check_events(hero):
    for event in pygame.event.get(): #run through all pygame events
        if event.type == pygame.QUIT: #if the event is the quit event....quit!
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: #"The user pressed "right"
                hero.moving_right = True
            elif event.key == pygame.K_LEFT:
                hero.moving_left = True
            elif event.key == pygame.K_UP:
                hero.moving_up = True
            elif event.key == pygame.K_DOWN:
                hero.moving_down = True
        elif event.type == pygame.KEYUP:
            hero.moving_right = False
            hero.moving_left = False
            hero.moving_up = False
            hero.moving_down = False

def update_screen(settings, screen, hero):
    screen.fill(settings.bg_color)
    hero.draw_me()
    pygame.display.flip()
