#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
#Note - all comments within the following program will be 
#below the code that they are commenting on
import pygame
import pygame.time
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

DivButton = Button(320, 172, 210, 50, (255, 255, 255), "Division Questions!", (0, 0, 0))
MultButton = Button(320, 190, 258, 50, (255, 255, 255), "Multiplication Questions!", (0, 0, 0))
SubButton = Button(320, 260, 250, 50, (255, 255, 255), "Subtraction Questions!", (0, 0, 0))
AddButton = Button(320, 330, 210, 50, (255, 255, 255), "Addition Questions!", (0, 0, 0))


#Visuals for buttons are displayed
#and buttons are grouped together.

def WasButtonClicked(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()

        # Check which button was clicked
        for button, questions in ButtonQuestionLink.items():
            if button.is_clicked(mouse_pos):
                DisplayQuestions(questions)
                break

                
def DisplayQuestions(questions):
    escape_button = Button(10, 10, 100, 50, (255, 0, 0), "Home", (255, 255, 255))
    escape_button_group = pygame.sprite.GroupSingle(escape_button)
    question_keys = list(questions.keys())
    random.shuffle(question_keys)
    score = 0  
    for question in question_keys:
        answer = questions[question]
        question_displayed = False
        while not question_displayed:
            gameWindow.fill((128, 73, 8))
            escape_button_group.draw(gameWindow)
            font = pygame.font.Font(None, 32)
            text = font.render(question, True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (gameWindowWidth // 2, gameWindowHeight // 2 - 50)
            gameWindow.blit(text, text_rect)
            input_box = pygame.Rect(gameWindowWidth // 2 - 70, gameWindowHeight // 2, 140, 32)
            input_box.center = (gameWindowWidth // 2, gameWindowHeight // 2 + 50)
            pygame.draw.rect(gameWindow, (255, 255, 255), input_box, 2)
            pygame.display.flip()
            user_input = ''
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if escape_button.is_clicked(event.pos):
                            return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if user_input.strip().lower() == str(answer).lower():
                                font = pygame.font.Font(None, 32)
                                text = font.render("Congratulations, you got it right!", True, (255, 255, 255))
                                text_rect = text.get_rect()
                                text_rect.center = (gameWindowWidth // 2, gameWindowHeight // 2 + 100)
                                gameWindow.blit(text, text_rect)
                                pygame.display.flip()
                                pygame.time.delay(1450)
                                question_displayed = True
                                score += 1 
                                score_font = pygame.font.Font("comicsansms", 24)
                                score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
                                score_rect = (790,10)
                                gameWindow.blit(score_text, score_rect)
                                break
                            else:
                                font = pygame.font.Font(None, 32)
                                text = font.render("Sorry, wrong answer. Please try again.", True, (255, 255, 255))
                                score += 0
                                text_rect = text.get_rect()
                                text_rect.center = (gameWindowWidth // 2, gameWindowHeight // 2 + 100)
                                gameWindow.blit(text, text_rect)
                                pygame.display.flip()



#Game Mechanic function


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
                draw_character_on_background("ArceusLocation", Char2, 400, 80)  
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
                draw_character_on_background("GiratinaLocation", Char3, 400, 100)
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

def BackgroundHeaders():
    BackgroundFont = pygame.font.SysFont("comicsansms", 20)
    BackgroundX = 272
    BackgroundY = 0
    if background == backgrounds["ArceusLocation"]:
        BackgroundDisplay = BackgroundFont.render("Welcome to Arceus' Division Room!", True, (0, 0, 0))
        background.blit(BackgroundDisplay, (BackgroundX, BackgroundY))
        pygame.display.update()
    elif background == backgrounds["GiratinaLocation"]:
        BackgroundDisplay = BackgroundFont.render("Welcome to Giratina's Multiplication Room!", True, (0, 0, 0))
        background.blit(BackgroundDisplay, (BackgroundX, BackgroundY))
        pygame.display.update()
    elif background == backgrounds["RayquazaLocation"]:
        BackgroundDisplay = BackgroundFont.render("Welcome to Rayquaza's Subtraction Room!", True, (0, 0, 0))
        background.blit(BackgroundDisplay, (BackgroundX, BackgroundY))
        pygame.display.update()
    elif background == backgrounds["DeoxysLocation"]:
        BackgroundDisplay = BackgroundFont.render("Welcome to Deoxys' Addition Room!", True, (0, 0, 0))
        background.blit(BackgroundDisplay, (BackgroundX, BackgroundY))
        pygame.display.update()
        
#Function that displays the headers for each background


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

def Char1Movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and Char1.rect.x > 0:
        Char1.vel_x = -9
    elif keys[pygame.K_RIGHT] and Char1.rect.x + Char1.rect.width < 800:
        Char1.vel_x = 9
    else:
        Char1.vel_x = 0
    if keys[pygame.K_UP] and Char1.rect.y > 0:
        Char1.vel_y = -9
    elif keys[pygame.K_DOWN] and Char1.rect.y + Char1.rect.height < 600:
        Char1.vel_y = 9
    else:
        Char1.vel_y = 0

        
#Allows the character to move, 
#bounded to the gameWindow

pygame.display.set_caption("The Math Maze")
background = pygame.image.load("BotwEntry.jpg")
background = pygame.transform.scale(background, (800, 600))
gameWindowWidth = background.get_width()
gameWindowHeight = background.get_height()
gameWindow = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))
#Initial background is set with a caption
#Game Window is initialized with the same dimensions as the background.

font1 = pygame.font.SysFont("comicsansms", 26)
text = font1.render("Welcome to the Math Maze!", True, (0, 0, 0))
background.blit(text, (287, 50))
font2 = pygame.font.SysFont("comicsansms", 18)
WelcomeMessage = font2.render("Using the arrow keys, travel to a room!.", True, (0,0,0))
background.blit(WelcomeMessage, (301, 253))
#Text initialized on the welcome screen.


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
    "What is 7,432,561/99?" : "75,065", 
    "What is 7,654,321/1234?" : "6,201",
    "What is 56,789/123?" : "461",
    "What is 9,876,543/321?" : "30,687",
    "What is 4,321,098/98?" : "44,016",
    "What is 123,456/789?" : "156"
}
#Our first opponent is initialized
#with associated questions.

Char3 = Character("GiratinaC3.png", "Char3")

Char3Questions = {
    "What is 79 * 96?" : "7,584" ,
    "What is 6,247 * 82?" : "512,654" ,
    "What is 15,729 * 81?" : " 1,275,849" ,
    "What is 8,712 * 56?" : "488,832" ,
    "What is 3,246 * 225?" : "730,250", 
    "What is 222 * 333?" : "73,926",
    "What is 789 * 456? " : "359,724",
    "What is 888 * 222? " : "197,136",
    "What is 345 * 678?" : "234,210",
    "What is 987 * 654? " : "644,298"
}
#Our second opponent is initialized
#with associated questions.

Char4 = Character("RayquazaC4.png", "Char4")
Char4Questions = {
    "What is 1,000,000 - 123,456?" : "876,544" ,
    "What is 6,543,210 - 3,210,987?" : "3,332,223" ,
    "What is 89,654 - 34,567?" : "55,087" ,
    "What is 986,543 - 543,210?" : "443,333" ,
    "What is 127,896 - 89,654?" : "38,242", 
    "What is 876,543 - 123,456?" : "753,087",
    "What is 987,654 - 345,678?" : "641,976",
    "What is 987,654 - 123,456?" : "864,198",
    "What is 876,543 - 432,109?" : "444,434",
    "What is 987,654 - 456,789?" : "530,865"
}
#Our third opponent is initialized
#with associated questions.

Char5 = Character("DeoxysC5.png", "Char5")
Char5Questions = {
    "What is 123,456 + 654,321?" : "777,777" ,
    "What is 23,456 + 98,765?" : "122,221" ,
    "What is 765,432 + 876,543?" : "1,642,975" ,
    "What is 987,654 + 345,678?" : "1,333,332" ,
    "What is 987,654 + 123,456?" : " 1,111,110", 
    "What is 123,456 + 987,654?" : "1,111,110",
    "What is 456,789 + 543,210?" : "1,000,999",
    "What is 789,012 + 123,456?" : "912,468",
    "What is 321,654 + 987,654?" : "1,309,308",
    "What is 876,543 + 321,098?" : "1,197,641"
}
#Our fourth opponent is initialized
#with associated questions.

AllQuestions = [Char2Questions, Char3Questions, Char4Questions, Char5Questions]

#Questions placed in a list for accessibililty.

ButtonQuestionLink = {
    DivButton: Char2Questions,
    MultButton: Char3Questions,
    SubButton: Char4Questions,
    AddButton: Char5Questions
}

door1 = Door(50, 50, 100, 200, (0, 0, 255), (255, 255, 255))  

DivDoorFont = pygame.font.SysFont("comicsansms", 20)
DivDoorDisplay = DivDoorFont.render("Division", True, (0, 0, 0))
DivDoorX = 14
DivDoorY = 50
door1.image.blit(DivDoorDisplay, (DivDoorX, DivDoorY))

#Door 1 is given a position and text is blitted onto it.

door2 = Door(650, 50, 100, 200, (225, 0, 0), (255, 255, 255))

MultDoorFont = pygame.font.SysFont("comicsansms", 15)
MultDoorDisplay = MultDoorFont.render("Multiplication", True, (0, 0, 0))
MultDoorX = 3
MultDoorY = 60
door2.image.blit(MultDoorDisplay, (MultDoorX, MultDoorY))

#Door 2 is given a position and text is blitted onto it.
  
door3 = Door(50, 350, 100, 200, (0, 255, 0), (255, 255, 255)) 

SubDoorFont = pygame.font.SysFont("comicsansms", 16)
SubDoorDisplay = SubDoorFont.render("Subtraction", True, (0, 0, 0))
SubDoorX = 6
SubDoorY = 46
door3.image.blit(SubDoorDisplay, (SubDoorX, SubDoorY))

#Door 3 is given a position and text is blitted onto it.

door4 = Door(650, 350, 100, 200, (255, 255, 0), (255, 255, 255))  

AddDoorFont = pygame.font.SysFont("comicsansms", 17)
AddDoorDisplay = AddDoorFont.render("Addition", True, (0, 0, 0))
AddDoorX = 14
AddDoorY = 48
door4.image.blit(AddDoorDisplay, (AddDoorX, AddDoorY))

#Door 4 is given a position and text is blitted onto it.

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
    
    
    Char1Movement()   
    WasButtonClicked(event)
    BackgroundHeaders()
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