
'''
Name: Alien Invasion - Settings Module
Author: Marvin Perez
Purpose: Stores all game settings.
Date: 04/19/2026
'''
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        #ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 25
        self.alien_scale = 2
        self.alien_spacing_x = 1.5 # horizontal spacing multiplier
        self.alien_spacing_y = 1.5  # vertical spacing multiplier

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1  
        

        #how quickly the game speeds up
        self.speedup_scale = 1.1

        #how quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 5
        self.bullet_speed = 10
        self.alien_speed = 4

        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #scoring settings
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)