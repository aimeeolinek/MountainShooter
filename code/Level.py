#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list = []
        self.factory = EntityFactory()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for entity in self.entity_list:
                entity.move()
                self.window.blit(entity.surf, entity.rect)

            pygame.display.flip()
