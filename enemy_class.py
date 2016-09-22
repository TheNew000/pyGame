import math
import pygame #duh
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, screen):
        super(Enemy, self).__init__()
        self.screen = screen #Give the Enemy the ability to control the screen
        #Load the hero image, get it's rect and put i
        self.image = pygame.image.load("images/monster1.png")
        self.rect = self.image.get_rect() #pygame gives us get_rect on any obect
        self.screen_rect = screen.get_rect() #assign a car so the hero class knows how big it is
        self.rect.centery = self.screen_rect.centery #this will put the middle of the hero at the middle of the screen
        self.rect.right = self.screen_rect.right  #this will put our hero "bottom" at the bottom of the screen

    def update(self, hero, speed=5):
        
        # find normalized direction vector (dx, dy) between enemy and hero
        dx, dy = self.rect.x - hero.rect.x, self.rect.y - hero.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist
        # move along this normalized vector towards the hero at current speed
        self.rect.x -= dx * speed
        self.rect.y -= dy * speed

    def draw_me(self):
        self.screen.blit(self.image, self.rect) #draw the surface (the image the where)

    def __exit__(self, *err):
        self.remove(self)
