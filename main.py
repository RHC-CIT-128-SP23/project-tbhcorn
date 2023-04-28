#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
#Note - all comments within the following program will be below the code that they are commenting on
import pygame
pygame.init()
#imports pygame module and initializes it

backgrounds = {
    "BotwEntry": pygame.transform.scale(pygame.image.load("BotwEntry.jpg"), (800, 600)),
    "ArceusLocation": pygame.transform.scale(pygame.image.load("ArceusLocation.jpg"), (800, 600)),
    "GiratinaLocation": pygame.transform.scale(pygame.image.load("GiratinaLocation.jpg"), (800, 600)),
    "RayquazaLocation": pygame.transform.scale(pygame.image.load("RayquazaLocation.jpg"), (800, 600)),
    "DeoxysLocation": pygame.transform.scale(pygame.image.load("DeoxysLocation.jpg"), (800, 600))
}
#All rooms "backgrounds"

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
class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, knob_color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        knob_width = 10
        knob_height = 10
        knob_x = width - knob_width
        knob_y = height // 2 - knob_height // 2
        pygame.draw.ellipse(self.image, knob_color, [knob_x, knob_y, knob_width, knob_height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#Creates door class for doors to be used later

def detect_collisions():
    global background
    for door in doors:
        if Char1.rect.colliderect(door.rect):
            if door == door1:
                background = pygame.image.load("ArceusLocation.jpg")
                background = pygame.transform.scale(background, (800, 600))
                all_sprites.add(Char2)
                draw_character_on_background("ArceusLocation", Char2, 500, 400)  
                all_sprites.remove(Char3)
                all_sprites.remove(Char4)
                all_sprites.remove(Char5)
            elif door == door2:
                background = pygame.image.load("GiratinaLocation.jpg")
                background = pygame.transform.scale(background, (800, 600))
                all_sprites.add(Char3)
                draw_character_on_background("GiratinaLocation", Char3, 300, 200)
                all_sprites.remove(Char2)
                all_sprites.remove(Char4)
                all_sprites.remove(Char5)
            elif door == door3:
                background = pygame.image.load("RayquazaLocation.jpg")
                background = pygame.transform.scale(background, (800, 600))
                all_sprites.add(Char4)
                draw_character_on_background("RayquazaLocation", Char4, 200, 100) 
                all_sprites.remove(Char2)
                all_sprites.remove(Char3)
                all_sprites.remove(Char5)
            elif door == door4:
                background = pygame.image.load("DeoxysLocation.jpg")
                background = pygame.transform.scale(background, (800, 600))
                all_sprites.add(Char5)
                draw_character_on_background("DeoxysLocation", Char5, 390, 280)
                all_sprites.remove(Char2)
                all_sprites.remove(Char3)
                all_sprites.remove(Char4)

#Collision Detection function, to change rooms.

# Define a function to draw a character on a background
def draw_character_on_background(background_name, character, x, y):
    global background
    background = backgrounds[background_name]
    character_image = character.image
    character_rect = character.rect
    character_rect.x = x
    character_rect.y = y
    gameWindow.blit(background, (0, 0))
    all_sprites.draw(gameWindow)  # draw all sprites, including the character
#draw character

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
Char1 = Character("DragoniteMC1.png")
Char1.rect.x = 400
Char1.rect.y = 300
all_sprites = pygame.sprite.Group(Char1)
all_sprites.add(Char1)

# The character that will be controlled by the user is given an initial position, 

Char2 = Character("ArceusC2.png")
Char2.rect.x = 500
Char2.rect.y = 400

Char3 = Character("GiratinaC3.png")
Char3.rect.x = 300
Char3.rect.y = 200

Char4 = Character("RayquazaC4.png")
Char4.rect.x = 200
Char4.rect.y = 100

Char5 = Character("DeoxysC5.png")
Char5.rect.x = 150
Char5.rect.y = 250

#All character opponents are initialized as sprites.

door1 = Door(50, 50, 100, 200, (0, 0, 255), (255, 255, 255))  
door2 = Door(gameWindowWidth - 150, 50, 100, 200, (255, 0, 0), (255, 255, 255))  
door3 = Door(50, gameWindowHeight - 250, 100, 200, (0, 255, 0), (255, 255, 255)) 
door4 = Door(gameWindowWidth - 150, gameWindowHeight - 250, 100, 200, (255, 255, 0), (255, 255, 255))  
doors = [door1, door2, door3, door4]
#doors placed in a list for collision detection

all_sprites.add(door1)
all_sprites.add(door2)
all_sprites.add(door3)
all_sprites.add(door4)
clock = pygame.time.Clock()
#The doors that will lead the user to 4 different rooms are placed on our game board.
#These doors are at different corners, respectively.
#The game clock is also set.

#Adds text to the Home Screen of the game
functioning = True
while functioning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            functioning = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Char1.vel_x = -5
    elif keys[pygame.K_RIGHT]:
        Char1.vel_x = 5
    else:
        Char1.vel_x = 0
    if keys[pygame.K_UP]:
        Char1.vel_y = -5
    elif keys[pygame.K_DOWN]:
        Char1.vel_y = 5
    else:
        Char1.vel_y = 0
        
    detect_collisions()
    
    all_sprites.update()
# A loop is set to run pygame and close it when X is pressed.
#In addition to this, we have now given our character movement through 
#the arrow keys
    # Update the display
    pygame.display.update()
    
    gameWindow.blit(background, (0, 0))
    all_sprites.draw(gameWindow)
    pygame.display.update()
    clock.tick(60)
    
#Sprites are drawn and set into the game window
#within pygame. Time is also measured

pygame.quit()
#Ends the game that we are running.