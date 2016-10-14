#A place for settings
class Settings(object):
    def __init__(self):
        self.screen_size = 1000,800 #Put the numbers in a variable because set_mode can only take one argument
        self.bg_color = (60,80,20) #army green color
        self.bullet_speed = 15
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 0,0,0
        self.enemy_speed = 5
        self.game_active = False #init the game as not active
        self.score = 0

