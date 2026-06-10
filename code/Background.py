import pygame
from code.Entity import Entity

class Background(Entity):
    def move(self):
        # Exemplo: scroll horizontal
        self.rect.x -= 1
