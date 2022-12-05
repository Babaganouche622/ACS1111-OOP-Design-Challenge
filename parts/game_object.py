import pygame

class GameObject(pygame.sprite.Sprite):
    """
    Evey game object will pull from this class, we need to call these methods specifically to move game objects and loads them into the map.
    This is the basic game object we will be using to instantiate
    all rendered game objects with.
    """
    def __init__(self, x, y, image, default_image_size):
        super(GameObject, self).__init__()
        self._x = x
        self._y = y
        self.__default_image_size = default_image_size
        self._surf = pygame.transform.scale((pygame.image.load(image)), self.__default_image_size)
        self._rect = self._surf.get_rect()
        

    def render(self, screen):
        self._rect.x = self._x
        self._rect.y = self._y
        screen.blit(self._surf, (self._x, self._y))

    def move(self, x, y):
        self._x = x
        self._y = y