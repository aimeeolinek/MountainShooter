import pygame
from code.Entity import Entity

class Enemy(Entity):
    def move(self):
        self.rect.x -= 2  # movimento simples para esquerda