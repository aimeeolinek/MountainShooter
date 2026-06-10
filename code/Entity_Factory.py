import pygame
from .Player import Player
from .Enemy import Enemy
from .Background import Background


class EntityFactory:
    def get_entity(self, entity_type):
        if entity_type == "player":
            surf = pygame.Surface((50, 50))
            surf.fill((0, 255, 0))
            return Player("Player", surf, surf.get_rect())
        elif entity_type == "enemy":
            surf = pygame.Surface((50, 50))
            surf.fill((255, 0, 0))
            return Enemy("Enemy", surf, surf.get_rect())
        elif entity_type == "background":
            surf = pygame.Surface((800, 600))
            surf.fill((0, 0, 255))
            return Background("Background", surf, surf.get_rect())
        else:
            return None