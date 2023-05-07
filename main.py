#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
#Note - all comments within the following program will be 
#below the code that they are commenting on
import pygame
import random
pygame.init()
pygame.font.init()
all_sprites = pygame.sprite.Group()

#imports pygame, random, and pygame font modules and initializes them + all_sprites
    
backgrounds = {
    "BotwEntry": pygame.transform.scale(pygame.image.load("BotwEntry.jpg"), (800, 600)),
    "ArceusLocation": pygame.transform.scale(pygame.image.load("ArceusLocation.jpg"), (800, 600)),
    "GiratinaLocation": pygame.transform.scale(pygame.image.load("GiratinaLocation.jpg"), (800, 600)),
    "RayquazaLocation": pygame.transform.scale(pygame.image.load("RayquazaLocation.jpg"), (800, 600)),
    "DeoxysLocation": pygame.transform.scale(pygame.image.load("DeoxysLocation.jpg"), (800, 600))
}
#All rooms are initialized as backgrounds, and are scaled to fit the game window.
class Character(pygame.sprite.Sprite):
    def __init__(self, image_path,name):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0
        self.name = name
    
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
#creates Character class for following characters
#with position and velocity
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

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, text, text_color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        font = pygame.font.SysFont("comicsansms", 22)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        if self.rect.collidepoint(pos):
            return True
        return False
#Creates a button class for buttons that can be clicked
#to display questions 

DivButton = Button(320, 240, 210, 50, (255, 255, 255), "Division Questions!", (0, 0, 0))
MultButton = Button(320, 240, 258, 50, (255, 255, 255), "Multiplication Questions!", (0, 0, 0))
SubButton = Button(320, 240, 250, 50, (255, 255, 255), "Subtraction Questions!", (0, 0, 0))
AddButton = Button(320, 240, 210, 50, (255, 255, 255), "Addition Questions!", (0, 0, 0))

#Visuals for buttons are displayed

def WasButtonClicked(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Check which button was clicked
            if DivButton.is_clicked(mouse_pos):
                questions = Char2Questions
                DisplayQuestions(questions)
            elif MultButton.is_clicked(mouse_pos):
                questions = Char3Questions
                DisplayQuestions(questions)
            elif SubButton.is_clicked(mouse_pos):
                questions = Char4Questions
                DisplayQuestions(questions)
            elif AddButton.is_clicked(mouse_pos):
                questions = Char5Questions
                DisplayQuestions(questions)
                
def DisplayQuestions(questions):
    for question in questions:
        font = pygame.font.Font(None, 32)
        text = font.render(question, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (gameWindowWidth // 2, gameWindowHeight // 2)
        input_box = pygame.Rect(gameWindowWidth // 2 - 70, gameWindowHeight // 2, 140, 32)
        input_box.center = (gameWindowWidth // 2, gameWindowHeight // 2 + 50)
        pygame.draw.rect(gameWindow, (255, 255, 255), input_box, 2)
        pygame.display.flip()
        user_input = ''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if user_input == question[-1]:
                            print("Congratulations, you got it right!")
                        else:
                            print("Sorry, wrong answer. Please try again.")
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += chr(event.key)
            gameWindow.fill((128, 73, 8))
            pygame.draw.rect(gameWindow, (255, 255, 255), input_box, 2)
            font = pygame.font.Font(None, 32)
            text_surface = font.render(user_input, True, (255, 255, 255))
            gameWindow.blit(text, text_rect)
            gameWindow.blit(text_surface, input_box)
            pygame.display.flip()


def Door_Collisions():
    global background
    for door in doors:
        if Char1.rect.colliderect(door.rect):
            if door == door1:
                background = pygame.image.load("ArceusLocation.jpg")
                background = pygame.transform.scale(background, (800, 600))
                all_sprites.add(Char2)
                all_sprites.add(DivButton)
                all_sprites.remove(SubButton)
                all_sprites.remove(AddButton)
                all_sprites.remove(MultButton)
                draw_character_on_background("ArceusLocation", Char2, 400, 140)  
                all_sprites.remove(Char3)
                all_sprites.remove(Char4)
                all_sprites.remove(Char5)
            elif door == door2:
                background = pygame.image.load("GiratinaLocation.jpg")
                background = pygame.transform.scale(background, (800, 600))
                all_sprites.add(Char3)
                all_sprites.add(MultButton)
                all_sprites.remove(DivButton)
                all_sprites.remove(SubButton)
                all_sprites.remove(AddButton)
                draw_character_on_background("GiratinaLocation", Char3, 400, 140)
                all_sprites.remove(Char2)
                all_sprites.remove(Char4)
                all_sprites.remove(Char5)
            elif door == door3:
                background = pygame.image.load("RayquazaLocation.jpg")
                background = pygame.transform.scale(background, (800, 600))
                all_sprites.add(Char4)
                all_sprites.add(SubButton)
                all_sprites.remove(DivButton)
                all_sprites.remove(AddButton)
                all_sprites.remove(MultButton)
                draw_character_on_background("RayquazaLocation", Char4, 400, 140) 
                all_sprites.remove(Char2)
                all_sprites.remove(Char3)
                all_sprites.remove(Char5)
            elif door == door4:
                background = pygame.image.load("DeoxysLocation.jpg")
                background = pygame.transform.scale(background, (800, 600))
                all_sprites.add(Char5)
                all_sprites.add(AddButton)
                all_sprites.remove(DivButton)
                all_sprites.remove(SubButton)
                all_sprites.remove(MultButton)
                draw_character_on_background("DeoxysLocation", Char5, 400, 140)
                all_sprites.remove(Char2)
                all_sprites.remove(Char3)
                all_sprites.remove(Char4)
    all_sprites.draw(gameWindow)

#Function that changes background and displays buttons
#upon door collisions

def draw_character_on_background(background_name, character, x, y):
    global background
    background = backgrounds[background_name]
    character_image = character.image
    character_rect = character.rect
    character_rect.x = x
    character_rect.y = y
    gameWindow.blit(background, (0, 0))
    all_sprites.draw(gameWindow)  
#Character drawing function, which draws the character 
#on our background in the game window.    

pygame.display.set_caption("The Math Maze")
background = pygame.image.load("BotwEntry.jpg")
background = pygame.transform.scale(background, (800, 600))
gameWindowWidth = background.get_width()
gameWindowHeight = background.get_height()
gameWindow = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))
#Initial background is set with a caption
#Game Window is initialized with the same dimensions as the background.

font = pygame.font.SysFont("comicsansms", 36)
text = font.render("Choose a room!", True, (0, 0, 0))
background.blit(text, (287, 50))
Char1 = Character("DragoniteMC1.png", "Char1")
Char1.rect.x = 400
Char1.rect.y = 300
all_sprites = pygame.sprite.Group(Char1)
all_sprites.add(Char1)
#The user's character is initialized, and is placed in the center of the screen.
#The screem also has text on it.

Char2 = Character("ArceusC2.png", "Char2")
Char2Questions = {
    "What is 87,300/900?" : "97" ,
    "What is 2,456,789/7?" : "350,984" ,
    "What is 3,829,875/25?" : "153,195" ,
    "What is 9,876,543/81?" : "121,969" ,
    "What is 7,432,561/99?" : "75,065" 
}
#Our first opponent is initialized
#with associated questions.

Char3 = Character("GiratinaC3.png", "Char3")

Char3Questions = {
    "What is 79 * 96?" : "7,584" ,
    "What is 6,247 * 82?" : "512,654" ,
    "What is 15,729 * 81?" : " 1,275,849" ,
    "What is 8,712 * 56?" : "488,832" ,
    "What is 3,246 * 225?" : "730,250" 
}
#Our second opponent is initialized
#with associated questions.

Char4 = Character("RayquazaC4.png", "Char4")
Char4Questions = {
    "What is 1,000,000 - 123,456?" : "876,544" ,
    "What is 6,543,210 - 3,210,987?" : "3,332,223" ,
    "What is 89,654 - 34,567?" : "55,087" ,
    "What is 986,543 - 543,210?" : "443,333" ,
    "What is 127,896 - 89,654?" : "38,242" 
}
#Our third opponent is initialized
#with associated questions.

Char5 = Character("DeoxysC5.png", "Char5")
Char5Questions = {
    "What is 123,456 + 654,321?" : "777,777" ,
    "What is 23,456 + 98,765?" : "122,221" ,
    "What is 765,432 + 876,543?" : "1,642,975" ,
    "What is 987,654 + 345,678?" : "1,333,332" ,
    "What is 987,654 + 123,456?" : " 1,111,110" 
}
#Our fourth opponent is initialized
#with associated questions.

door1 = Door(50, 50, 100, 200, (0, 0, 255), (255, 255, 255))  
door2 = Door(gameWindowWidth - 150, 50, 100, 200, (255, 0, 0), (255, 255, 255))  
door3 = Door(50, gameWindowHeight - 250, 100, 200, (0, 255, 0), (255, 255, 255)) 
door4 = Door(gameWindowWidth - 150, gameWindowHeight - 250, 100, 200, (255, 255, 0), (255, 255, 255))  
doors = [door1, door2, door3, door4]
#Our doors are given a position and placed in a list.

all_sprites.add(door1)
all_sprites.add(door2)
all_sprites.add(door3)
all_sprites.add(door4)
#The doors that will lead the user to 4 different rooms are placed on our game board.
#These doors are at four different corners, respectively.

clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial',30)
#The game clock and font are also set.

functioning = True
while functioning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            functioning = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Char1.vel_x = -8
    elif keys[pygame.K_RIGHT]:
        Char1.vel_x = 8
    else:
        Char1.vel_x = 0
    if keys[pygame.K_UP]:
        Char1.vel_y = -8
    elif keys[pygame.K_DOWN]:
        Char1.vel_y = 8
    else:
        Char1.vel_y = 0
        
    WasButtonClicked(event)
    Door_Collisions()    
    all_sprites.update()
    pygame.display.update()
    gameWindow.blit(background, (0, 0))
    all_sprites.draw(gameWindow)
    pygame.display.update()
    clock.tick(60)
    
#Our game loop is set to run pygame and close it when X is pressed.
#In addition to this, we have now given our character movement through 
#the arrow keys. Sprites are drawn and set into the game window
#within pygame. Time is also measured.

pygame.quit()
#Ends the game that we are running.