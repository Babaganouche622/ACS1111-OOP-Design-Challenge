'''
Character class; will be extended to create both Player and Enemy classes. Extends
The GameObject class.
'''
from game_object import GameObject

class Character(GameObject):
    '''Character class; parent class for Player and Enemy classes. Extends GameObject class.'''
    def __init__(self, health, move_speed, fire_rate, projectile_speed):
        super().__init__()
        self.health = health
        self.move_speed = move_speed
        self.fire_rate = fire_rate
        self.projectile_speed = projectile_speed

    def shoot(self):
        '''
        TODO: Create a new projectile object with projectile_speed and initial
        position at the same position as the character
        '''
        print('Pew Pew')

    def heal(self, amount):
        '''
        Heal the character for the specified amount
        '''
        self.health += amount

    def set_move_speed(self, new_move_speed):
        '''
        Set a new move speed (could be needed if a powerup is obtained, or when reaching a higher level)
        '''
        self.move_speed = new_move_speed

    

    
