"""Import all the dependancies"""
import pygame
from pygame.locals import *
from pygame import mixer
from parts.player import Player
from parts.enemy import Enemy
import random
from parts.projectile import Projectile
# from sprites.character import *

"""Initialize Pygame"""

pygame.init()
mixer.init()

"""All our pygame specific dependencies we need before runtime are here."""
fake_screen = pygame.display.set_mode([1920, 1080], HWSURFACE | DOUBLEBUF | RESIZABLE)
screen = fake_screen.copy()
# TODO Load background image here
background_image_size = (1920, 1080)
background = pygame.transform.scale((pygame.image.load("spacey_images/milky-way-2695569__480.jpeg")), background_image_size)

clock = pygame.time.Clock()

"""This is the method run to change the song during runtime"""
def play_music(song):
    mixer.music.stop()
    mixer.music.unload()
    mixer.music.load(song)
    mixer.music.play(-1)
    return False

"""All runtime specific variables to maintain operational flow."""

running = True 
new_battle = True
boss = False
music = True
player_score = 0
player_powerup = False

player2 = Player(x=50, y=650, image="spacey_images/x_wing.png", health=500, move_speed=10, fire_rate=1, damage=1, projectile_speed=-10, lives=3)

enemies = []
projectiles = []

while running:
    """This is where we check for exiting the game."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, HWSURFACE | DOUBLEBUF | RESIZABLE)
            # screen.blit(pygame.transform.scale(background, event.dict['size']), (0, 0))            
            pygame.display.update()

    """Here we set the background image."""
    screen.fill((0, 0, 0))
    screen.blit(background, [0, 0])
    fake_screen.blit(pygame.transform.scale(fake_screen, screen.get_rect().size), (0, 0))
    if new_battle:
        # music = play_music("Battle-Game-Music/Fight.mp3")
        number_enemies = random.randint(1, 20)
        while number_enemies > 0:
            enemies.append(Enemy(x=50, y=50, image="spacey_images/tie_fighter.png", health=10, move_speed=10, fire_rate=2, damage=1, projectile_speed=10))
            number_enemies -= 1
        x = 50
        for enemy in enemies:
            enemy.move(x, 50)
            x += 100
        new_battle = False
        music = True

    """This is where we will load our game music"""
    if music:
       play_music("spacey_sounds/03 In-Game Ambience.mp3")
       music = False

    """
    TODO Here down we will have the logic of the game actually being played
    TODO The enemies will try to kill the player, the player will shoot the enemies.
    TODO The player will score points.
    TODO The player will lose lives.
    TODO The game will end.
    """
    for entity in enemies:
        entity.render(screen)
    player2.render(screen)
    keys = pygame.key.get_pressed()
    player2.move(keys)

    player_shot = player2.shoot(keys)
    if isinstance(player_shot, Projectile):
        projectiles.append(player_shot)
    
    for enemy in enemies:
        shot = enemy.shoot()
        if isinstance(shot, Projectile):
            projectiles.append(shot)
    
    for projectile in projectiles:
        projectile.render(screen)
        projectile.move()
    # Projectile.move()



    """This loops our game 60 times a second, emulating 60fps, kind of."""
    pygame.display.flip()
    clock.tick(60)
