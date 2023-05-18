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

def WasButtonClicked(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()

        # Check which button was clicked
        for button, questions in ButtonQuestionLink.items():
            if button.is_clicked(mouse_pos):
                GameMechanic(questions)
                break

def update_score(score):
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (gameWindowWidth // 2, 50)
    gameWindow.blit(score_text, score_text_rect)
    return score


def GameMechanic(questions):
    score = 0
    escape_button = Button(10, 10, 100, 50, (255, 0, 0), "Home", (255, 255, 255))
    escape_button_group = pygame.sprite.GroupSingle(escape_button)
    question_keys = list(questions.keys())
    random.shuffle(question_keys)
    for question in question_keys:
        answer = questions[question]
        question_displayed = False
        while not question_displayed:
            gameWindow.fill((128, 73, 8))
            escape_button_group.draw(gameWindow)
            font = pygame.font.SysFont("comicsansms", 22)
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
                                pygame.time.delay(880)
                                question_displayed = True
                                score += 1
                                score = update_score(score)
                                break
                            else:
                                font = pygame.font.Font(None, 32)
                                text = font.render("Sorry, wrong answer. Please try again.", True, (255, 255, 255))
                                text_rect = text.get_rect()
                                text_rect.center = (gameWindowWidth // 2, gameWindowHeight // 2 + 100)
                                gameWindow.blit(text, text_rect)
                                pygame.display.flip()
                                pygame.time.delay(880)
                                question_displayed = True
                                score -= 1
                                score = update_score(score)
                                break
                        elif event.key == pygame.K_BACKSPACE:
                            user_input = user_input[:-1]
                        else:
                            user_input += event.unicode
                if question_displayed:
                    break
                gameWindow.fill((231, 239, 192))
                escape_button_group.draw(gameWindow)
                score = update_score(score)
                font = pygame.font.Font(None, 32)
                text_surface = font.render(user_input, True, (255, 255, 255))
                gameWindow.blit(text, text_rect)
                gameWindow.blit(text_surface, input_box)
                pygame.draw.rect(gameWindow, (255, 255, 255), input_box, 2)
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
                draw_character_on_background("ArceusLocation", Char2, 500, 62)  
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

def RoomText():
    BackgroundFont = pygame.font.SysFont("comicsansms", 20)
    BackgroundX = 211
    BackgroundY = 0
    if background == backgrounds["ArceusLocation"]:
        BackgroundHeader = BackgroundFont.render("Welcome to Arceus' Division Room!", True, (0, 0, 0))
        BackgroundWarning = BackgroundFont.render("Time to divide and conquer.", True, (0, 0, 0))
        BackgroundDisclaimer = BackgroundFont.render("Note: use commas when your answer has 4 digits! Ex: 1,234", True, (0, 0, 0))
        BackgroundInstructions = BackgroundFont.render("Click the button to begin your division journey.", True, (0, 0, 0))
        background.blit(BackgroundHeader, (BackgroundX, BackgroundY))
        background.blit(BackgroundWarning, (BackgroundX, BackgroundY + 25))
        background.blit(BackgroundDisclaimer, (234, 300))
        background.blit(BackgroundInstructions, (BackgroundX, BackgroundY + 50))
        pygame.display.update()
    elif background == backgrounds["GiratinaLocation"]:
        BackgroundHeader = BackgroundFont.render("Welcome to Giratina's Multiplication Room!", True, (0, 0, 0))
        BackgroundWarning = BackgroundFont.render("Let the time fly by while you multiply.", True, (0, 0, 0))
        BackgroundDisclaimer = BackgroundFont.render("Note: use commas when your answer has 4 digits! Ex: 1,234", True, (255,255,255))
        BackgroundInstructions = BackgroundFont.render("Click the button to multiply as high as the sky.", True, (0, 0, 0))
        background.blit(BackgroundHeader, (BackgroundX, BackgroundY))
        background.blit(BackgroundWarning, (BackgroundX, BackgroundY + 25))
        background.blit(BackgroundDisclaimer, (234, 300))
        background.blit(BackgroundInstructions, (BackgroundX, BackgroundY + 50))
        pygame.display.update()
    elif background == backgrounds["RayquazaLocation"]:
        BackgroundHeader = BackgroundFont.render("Welcome to Rayquaza's Subtraction Room!", True, (0, 0, 0))
        BackgroundWarning = BackgroundFont.render("Don't forget how to act when it's time to subtract.", True, (0, 0, 0))
        BackgroundDisclaimer = BackgroundFont.render("Note: use commas when your answer has 4 digits! Ex: 1,234", True, (255,255,255))
        BackgroundInstructions = BackgroundFont.render("Click the button to subtract and be exact.", True, (0, 0, 0))
        background.blit(BackgroundHeader, (BackgroundX, BackgroundY))
        background.blit(BackgroundWarning, (BackgroundX, BackgroundY + 25))
        background.blit(BackgroundDisclaimer, (234, 300))
        background.blit(BackgroundInstructions, (BackgroundX, BackgroundY + 50))
        pygame.display.update()
    elif background == backgrounds["DeoxysLocation"]:
        BackgroundHeader = BackgroundFont.render("Welcome to Deoxys' Addition Room!", True, (0, 0, 0))
        BackgroundWarning = BackgroundFont.render("It is now your mission to master addition.", True, (0, 0, 0))
        BackgroundDisclaimer = BackgroundFont.render("Note: use commas when your answer has 4 digits! Ex: 1,234", True, (0, 0, 0))
        BackgroundInstructions = BackgroundFont.render("Click the button to add and don't be sad!", True, (0, 0, 0))
        background.blit(BackgroundHeader, (BackgroundX, BackgroundY))
        background.blit(BackgroundWarning, (BackgroundX, BackgroundY + 25))
        background.blit(BackgroundDisclaimer, (234, 300))
        background.blit(BackgroundInstructions, (BackgroundX, BackgroundY + 50))
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
WelcomeMessage = font2.render("Using the arrow keys, travel to a room!", True, (0,0,0))
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
    "What is 628/4?" : "157" ,
    "What is 9,184/28?" : "328" ,
    "What is 9,876/3?" : "3,292" ,
    "What is 7,432/4?" : "1,858" , 
    "What is 8,568/6?" : "1,428",
    "What is 5,525/65?" : "85",
    "What is 7,631/587?" : "13",
    "What is 4,214/43?" : "98",
    "What is 1,392/16?" : "87"
}
#Our first opponent is initialized
#with 10 division questions.

Char3 = Character("GiratinaC3.png", "Char3")

Char3Questions = {
    "What is 87 * 54?" : "4,698" ,
    "What is 21 * 64??" : "1,344" ,
    "What is 17 * 84?" : " 1,428" ,
    "What is 14 * 56?" : "784" ,
    "What is 12 * 71?" : "852", 
    "What is 13 * 45?" : "585",
    "What is 74 * 21? " : "1,554",
    "What is 88 * 22? " : "1,936",
    "What is 81 * 14?" : "1,134",
    "What is 97 * 34? " : "3,298"
}
#Our second opponent is initialized
#with 10 multiplication questions.

Char4 = Character("RayquazaC4.png", "Char4")
Char4Questions = {
    "What is 8,797 - 675?" : "8,122" ,
    "What is 9,654 - 4,652?" : "5,002" ,
    "What is 8,572 - 785?" : "7,787" ,
    "What is 987 - 233?" : "754" ,
    "What is 852 - 741?" : "111", 
    "What is 456 - 123?" : "333",
    "What is 5,964 - 2,134?" : "3,830",
    "What is 1,714 - 1,472?" : "242",
    "What is 7,845 - 4,523?" : "3,322",
    "What is 4,152 - 3,245?" : "907"
}
#Our third opponent is initialized
#with 10 subtraction questions.

Char5 = Character("DeoxysC5.png", "Char5")
Char5Questions = {
    "What is 859 + 753?" : "1,612" ,
    "What is 345 + 629?" : "974" ,
    "What is 741 + 962?" : "1,703" ,
    "What is 867 + 341?" : "1,208" ,
    "What is 7,412 + 2,479?" : "9,891", 
    "What is 934 + 6,712?" : "7,646",
    "What is 618 + 2,415?" : "3,033",
    "What is 876 + 954?" : "1,830",
    "What is 643 + 892?" : "1,535",
    "What is 496 + 758?" : "1,254"
}
#Our fourth opponent is initialized
#with 10 addition questions.

DivButton = Button(270, 142, 210, 50, (255, 255, 255), "Division Questions!", (0, 0, 0))
MultButton = Button(320, 190, 258, 50, (255, 255, 255), "Multiplication Questions!", (0, 0, 0))
SubButton = Button(320, 260, 250, 50, (255, 255, 255), "Subtraction Questions!", (0, 0, 0))
AddButton = Button(320, 330, 210, 50, (255, 255, 255), "Addition Questions!", (0, 0, 0))


#Visuals for buttons are displayed
#and buttons are grouped together.


ButtonQuestionLink = {
    DivButton: Char2Questions,
    MultButton: Char3Questions,
    SubButton: Char4Questions,
    AddButton: Char5Questions
}
#A dictionary is created to link the buttons to the questions.

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
    RoomText()
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