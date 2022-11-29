'''
File contains a class representing an enemy ship.
'''
from random import randint
from .character import Character


class Enemy(Character):
    '''
    Class representing an enemy ship.
    '''
    def shoot(self):
        '''
        Randomy determines if a shot should be fired, with higher fire rate increasing
        the likelihood. If a shot should be fired, calls super().shoot(). Idea is
        to call this method on each enemy ship every time step, and then some random
        subset of the enemies would fire on each time step.
        '''
        random_number = randint(0, 100)
        if random_number < self._fire_rate:
            super().shoot()