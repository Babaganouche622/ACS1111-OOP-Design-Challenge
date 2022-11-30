'''
Character class; will be extended to create both Player and Enemy classes. Extends
The GameObject class.
'''
from .game_object import GameObject
from .projectile import Projectile

class Character(GameObject):
    '''Character class; parent class for Player and Enemy classes. Extends GameObject class.
    PROJECTILE_SPEED should be positive for instances of player, negative for instances of enemy.
    '''
    def __init__(self, health, move_speed, fire_rate, damage, projectile_speed, x, y, image):
        super().__init__(x, y, image)
        self._health = health # protected, only needs to be directly accessed within class and children
        self._move_speed = move_speed 
        self._fire_rate = fire_rate
        self._damage = damage
        self._projectile_speed = projectile_speed

    def shoot(self):
        '''
        Creates a new projectile object with projectile_speed and initial
        position at the same position as the character and returns it
        '''
        shot = Projectile(self._projectile_speed, self._damage, self.x, self.y, image='TODO:Projectile Image')
        return shot

    def set_move_speed(self, new_move_speed):
        '''
        Set a new move speed (could be needed if a powerup is obtained, or when reaching a higher level)
        '''
        self._move_speed = new_move_speed
    
    def is_dead(self):
        '''
        Determines if the character is dead
        '''
        if self._health <= 0:
            return True
        return False
