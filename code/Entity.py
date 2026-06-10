import pygame

class Entity:
    def _init_(self, name, surf, rect):
        self.name = name
        self.surf = surf
        self.rect = rect

    def move(self):
        pass