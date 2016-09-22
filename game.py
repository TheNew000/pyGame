import sys #we will need sys so the user can quit
import pygame #DUH
from hero_class import Hero #brings in the Hero Class


# Set up the main core function
def run_game():
    pygame.init() #initialize game modules
    screen_size = 1000,800 #Pt the numbers in a variable because set_mode can only take one argument
    screen = pygame.display.set_mode(screen_size) #Set the screem size with set_mode
    pygame.display.set_caption("Monster Attack") #Set the messag eon the status bar

    bg_color = (60,80,20) #army green color
    hero = Hero(screen)  #set a variable equal to the class and pass it the screen

    while 1: #run this loop forever
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        hero.draw_me()
        pygame.display.flip()

run_game() #Start the game!
