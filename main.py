#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''

#Note - all comments within the following program will be below the code that they are commenting on

import pygame
#imports pygame module

class Character(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0
    
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

#creates Character class for following characters

pygame.init()

pygame.display.set_caption("The Math Maze")

background = pygame.image.load("BotwEntry.jpg")
background = pygame.transform.scale(background, (800, 600))

gameWindowWidth = background.get_width()
gameWindowHeight = background.get_height()
gameWindow = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))

# The game window within python is set with an image, as pygame is initialized

font = pygame.font.SysFont("comicsansms", 36)
text = font.render("Choose a room!", True, (0, 0, 0))
background.blit(text, (287, 50))

#Adds text to the Home Screen of the game

door_color = (0, 0, 255)  # blue
door_width = 100
door_height = 200
door_x = (screen_width - door_width) // 2
door_y = (screen_height - door_height) // 2

#creates color, size, and position of the door

door_rect = pygame.Rect(door_x, door_y, door_width, door_height)
pygame.draw.rect(screen, door_color, door_rect)
knob_color = (255, 255, 255)  # white
knob_width = 10
knob_height = 10
knob_x = door_x + door_width // 2 - knob_width // 2
knob_y = door_y + door_height // 2 - knob_height // 2
knob_rect = pygame.Rect(knob_x, knob_y, knob_width, knob_height)
pygame.draw.ellipse(screen, knob_color, knob_rect)

#Both components of the door are created and placed into
#our pygame window

Char1 = Character("DragoniteMC1.png")
Char1.rect.x = 400
Char1.rect.y = 300
all_sprites = pygame.sprite.Group()
all_sprites.add(Char1)

clock = pygame.time.Clock()

# The character that will be controlled by the user is given an initial position, 
# and added to the game as a sprite. The game clock is also set.

functioning = True
while functioning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            functioning = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Char1.vel_x = -3
    elif keys[pygame.K_RIGHT]:
        Char1.vel_x = 3
    else:
        Char1.vel_x = 0
    if keys[pygame.K_UP]:
        Char1.vel_y = -3
    elif keys[pygame.K_DOWN]:
        Char1.vel_y = 3
    else:
        Char1.vel_y = 0

# A loop is set to run pygame and close it when X is pressed.
#In addition to this, we have now given our character movement through 
#the arrow keys
    
    all_sprites.update()
    gameWindow.blit(background, (0, 0))
    all_sprites.draw(gameWindow)
    pygame.display.update()
    clock.tick(60)
    
#Sprites are drawn and set into the game window
#within pygame. Time is also measured

pygame.quit()

#Ends the game that we are running.






