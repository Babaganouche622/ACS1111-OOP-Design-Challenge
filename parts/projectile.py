'''
Defines a projectile class
'''

from .game_object import GameObject

class Projectile(GameObject):
    def __init__(self, speed, damage, x, y, image):
        super().__init__(x, y, image)
        self.__speed = speed # private -> only used within the class
        self.damage = damage # public -> will need to be read by the game loop on collision

    def move(self):
        '''
        Override the inherited move method; projectiles only move in a straight
        line along the y-axis. Public method as will be called by game loop.
        '''
        self.y += self.__speed
