import pygame  # DUH
from hero_class import Hero  # brings in the Hero Class
from settings_class import Settings
import game_functions as gf
from pygame.sprite import Group
from enemy_class import Enemy
from start_button import Play_Button


# Set up the main core function
def run_game():
    pygame.init()  # initialize game modules
    game_settings = Settings()  # create an instance of settings Class
    screen = pygame.display.set_mode(game_settings.screen_size)  # Set the screen size with set_mode
    pygame.display.set_caption("Monster Attack")  # Set the messag e on the status bar
    play_button = Play_Button(screen, 'PLAY ME!!')

    hero = Hero(screen)  # set a variable equal to the class and pass it the screen
    enemies = Group()
    bullets = Group()  # set the bullets to group
    enemies.add(Enemy(screen))

    tick = 0

    while 1:  # run this loop forever

        gf.check_events(hero, bullets, game_settings, screen, play_button)  # call gf and get the check events method
        gf.update_screen(game_settings, screen, hero, enemies, bullets, play_button)  # call the update_screen method

        if game_settings.game_active:
            hero.update()  # update hero booleans
            enemies.update(hero, game_settings.enemy_speed)
            bullets.update()
            tick += 1

            if tick % 150 == 0:
                enemies.add(Enemy(screen))
            # get rid of  bullets that are off the screen
            for enemy in enemies:
                for bullet in bullets:
                    if bullet.rect.right <= 0:
                        bullets.remove(bullet)
                    if enemy.rect.colliderect(bullet.rect):
                        enemies.remove(enemy)
                        bullets.remove(bullet)
                if enemy.rect.colliderect(hero.rect):
                    print "You DIED!"
                    exit(0)


run_game()  # Start the game!
