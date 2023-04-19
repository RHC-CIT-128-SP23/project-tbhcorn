#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
import pygame

pygame.init()

background = pygame.image.load("Viridian_Forest_PE.jpg")

gameWindowWidth = background.get_width()
gameWindowHeight = background.get_height()
gameWindow = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))

clock = pygame.time.Clock()

functioning = True
while functioning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            functioning = False

    gameWindow.blit(background, (0, 0))

    pygame.display.update()

    clock.tick(60)

pygame.quit()






