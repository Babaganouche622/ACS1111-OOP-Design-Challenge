'''
Defines a projectile class
'''

from .game_object import GameObject

class Projectile(GameObject):
    def __init__(self, speed, damage, x, y, image, default_image_size=(25,25)):
        super().__init__(x, y, image, default_image_size)
        self.__speed = speed # private -> only used within the class
        self.damage = damage # public -> will need to be read by the game loop on collision
        # self.render(screen)

    # @classmethod
    def move(self):
        '''
        Override the inherited move method; projectiles only move in a straight
        line along the y-axis. Public method as will be called by game loop.
        '''
        self._y += self.__speed
        
