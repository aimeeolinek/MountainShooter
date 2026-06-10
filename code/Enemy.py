import pygame
from .Entity import Entity

class Enemy(Entity):
    def move(self):
        self.rect.x -= 2  # movimento simples para esquerda