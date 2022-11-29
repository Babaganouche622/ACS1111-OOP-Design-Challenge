import pygame

class GameObject(pygame.sprite.Sprite):
    """
    Evey game object will pull from this class, we need to call these methods specifically to move game objects and loads them into the map.
    This is the basic game object we will be using to instantiate
    all rendered game objects with.
    """
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect()

    def render(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.surf, (self.x, self.y))

    def move(self, x, y):
        self.x = x
        self.y = y