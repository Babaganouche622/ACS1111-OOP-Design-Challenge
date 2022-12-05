'''
Defines the Player class, which represents the player's ship.
'''
import pygame
from .character import Character

class Player(Character):
    '''
    Represents the player's ship. Inherits GameObject -> Character -> Player
    '''
    def __init__(self, health, move_speed, fire_rate, damage, projectile_speed, lives, x, y, image, default_image_size=(100,100)):
        super().__init__(health, move_speed, fire_rate, damage, projectile_speed, x, y, image, default_image_size)
        self.lives = lives

    def move(self, pressed_keys):
        '''
        Moves the player left or right; takes in an array of the currently pressed keys
        (can be obtained by calling pygame.key.get_pressed())
        '''
        if pressed_keys[pygame.K_LEFT]:
            self._x -= self._move_speed
        if pressed_keys[pygame.K_RIGHT]:
            self._x += self._move_speed

    def heal(self, amount):
        '''
        Heal the character for the specified amount
        '''
        self._health += amount

    def shoot(self, pressed_keys):
        '''
        Shoots when the spacebar is pressed.
        '''
        if pressed_keys[pygame.K_SPACE]:
            return super().shoot("spacey_images/player_bullet.png")
