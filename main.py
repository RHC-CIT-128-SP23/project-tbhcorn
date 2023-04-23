#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()

pygame.init()

background = pygame.image.load("Viridian_Forest_PE.jpg")

gameWindowWidth = background.get_width()
gameWindowHeight = background.get_height()
gameWindow = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))

Red = Character("Red.png")
all_sprites = pygame.sprite.Group()
all_sprites.add(Red)

clock = pygame.time.Clock()

functioning = True
while functioning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            functioning = False
    
    all_sprites.update()

    gameWindow.blit(background, (0, 0))
    all_sprites.draw(gameWindow)


    pygame.display.update()

    clock.tick(60)

pygame.quit()






