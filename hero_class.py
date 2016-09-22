import pygame #duh

class Hero(object):
    def __init__(self, screen):
        self.screen = screen #Give the hero the ability to control the screen
        #Load the hero image, get it's rect and put i
        self.image = pygame.image.load("images/hero.png")
        self.rect = self.image.get_rect() #pygame gives us get_rect on any obect
        self.screen_rect = screen.get_rect() #assign a car so the hero class knows how big it is
        self.rect.centerx = self.screen_rect.centerx #this will put the middle of the hero at the middle of the screen
        self.rect.bottom = self.screen_rect.bottom  #this will put our hero "bottom" at the bottom of the screen
        #not self.rect.centery because we want the bottom pointing towards the bottom
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #Add's updates to the hero class to keep all the hero updates in the hero class
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 15
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 15
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.bottom -= 15
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += 15

    def draw_me(self):
        self.screen.blit(self.image, self.rect) #draw the surface (the image the where)
