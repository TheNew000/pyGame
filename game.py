import pygame #DUH
from hero_class import Hero #brings in the Hero Class
from settings_class import Settings
import game_functions as gf

# Set up the main core function
def run_game():
    pygame.init() #initialize game modules
    game_settings = Settings() #create an instance of settings Class
    screen = pygame.display.set_mode(game_settings.screen_size) #Set the screen size with set_mode
    pygame.display.set_caption("Monster Attack") #Set the messag e on the status bar
    hero = Hero(screen)  #set a variable equal to the class and pass it the screen

    while 1: #run this loop forever
        gf.check_events(hero) #call gf and get the check events method
        hero.update() #update hero booleans
        gf.update_screen(game_settings, screen, hero) #call the update_screen method

run_game() #Start the game!
