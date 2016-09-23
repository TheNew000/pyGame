import pygame

class Play_Button(object):
    def __init__(self, screen, button_text):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        #set width of the button image
        self.width=250
        #set height of the button image
        self.height=100
        #set button color
        self.button_color=0,200,150
        #set text color
        self.text_color=255,255,255
        #set font info
        self.font=pygame.font.Font(None,52)
        #set the rect of the button
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        self.setup_message(button_text)


    def setup_message(self, button_text):
        # render the image inside of image_message
        self.image_message = self.font.render(button_text, True, self.text_color)
        self.image_message_rect = self.image_message.get_rect()
        self.image_message_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.image_message, self.image_message_rect)
