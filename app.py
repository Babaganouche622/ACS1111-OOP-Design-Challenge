"""
Pygame, import all things pygame, build the screen

class1 = GameObject => Character => Player
                                 => Enemy
                    => Items

methods, just print statements

-Spaceship
    health, lives, deaths, score, powerups
-enemies
    health, lives, deaths,
-powerups

-score counter, death counter, lives counter, music, sound effects, bullet classes, shooting mechanics



TODO we will start by building out the basic game board functionality
"""
"""Import all the dependancies"""
import pygame
from pygame.locals import *
from pygame import mixer
# from sprites.character import *

"""Initialize Pygame"""

pygame.init()
mixer.init()

"""All our pygame specific dependencies we need before runtime are here."""
fake_screen = pygame.display.set_mode([1920, 1080], HWSURFACE | DOUBLEBUF | RESIZABLE)
screen = fake_screen.copy()
# TODO Load background image here
background = pygame.image.load("spacey_images/space-background-with-stars-vector-illustration_97886-319.webp")

clock = pygame.time.Clock()


# TODO Here we load all the enemie's, player's, item's disigns into their classes.

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


    """This is where we will load our game music"""
    if music:
        music = play_music("spacey_sounds/mixkit-retro-video-game-bubble-laser-277.wav")

    """
    TODO Here down we will have the logic of the game actually being played
    TODO The enemies will try to kill the player, the player will shoot the enemies.
    TODO The player will score points.
    TODO The player will lose lives.
    TODO The game will end.
    """






    """This loops our game 60 times a second, emulating 60fps, kind of."""
    pygame.display.flip()
    clock.tick(60)
