[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10769082&assignment_repo_type=AssignmentRepo)

# The Math Maze

CIT 128 Student Directed Project

## Student Info

* Daniel Grilli
* 37902
* Spring 2023

## Program Description

My program will involve a character that can go into multiple math themed rooms. Each room will have a dedicated challenger in it, and each challenger will have a different subsection of math questions in a given topic. Each challenger will have their own challenge questions, and the goal is to be able to answer questions with score properly incrementing and corresponding output

The overarching goals for this program are as follows: 
- User can move their character around with arrow keys
- Each opponent has a different sprite and exists in a different room [with different backgrounds]
- Each opponent has their own dialogue
- The user can answer math questions (questions are randomized), and the score is properly incremented when the user answers properly.
- Corresponding output messages are displayed correspondingly with the user's answer [checks if answer is correct]

### Video Demonstration

Add a Link to your video demonstration

[Posted to youtube but view by link only]

### Install Instructions

For use in VS Code:

You must make sure that pip, python, and pygame are all up to date in order for this program to properly be run.
Here is how you can do so.

In your VS Code terminal (click "new terminal" from terminal in upper left hand corner), type:

* python -m pip install --upgrade pip (should be version 23.1.2)
* pip install --upgrade python (should be version 3.11.3 - if not, download from python website)
* python -m pip install pygame ( should be version 2.3.0)

Since the game itself imports pygame, this should be everything required for the player of said game. 

{Add any install instructions, if needed. This includes how to install included modules or libraries as well as configurations. You may remove this section if no special instructions are required.}

## Software Engineering

Designing and developing this program, I used object-oriented programming techniques to follow the given rubric while also fostering clarity within my code. 
I created three classes (character, button, and door) as I drew multiple characters, buttons, and doors within my program. This allowed me to avoid code redundancy and foster legibility within my code. I also gave each one of my major game events their own function, so that I could just call these functions in the main game loop for ease of use. This includes the: game mechanic, background/opponent changes upon the user entering a door, character movement (for the user), opponents being drawn on the screen, and for corresponding text to be shown when a certain opponent/background is displayed. Below these functions and classes, I have similar code grouped near each other. This subsequent code involves the use of dictionaries to link questions and their answers, and then these questions and their answers are correspondingly linked to the button that displays them upon click.

{Describe the software engineering techniques used for the design and development of this program.}

## Testing Script

My testing script will be described and broken up by the major game elements that I struggled the hardest with while buildng this game.

* Triggering Questions: 
  Initially, I was going to trigger the math questions displayed on the screen by colliding the user's character with the opponents. Initially, I tried to trigger an event when the user's character "char1" touched the x and y coordinates of each other character. This did not work for hours, and it drove me crazy. I then tried using the built-in colliderect method with the variables of the characters themselves. For example, if "char1 collided with char2, display char2questions". Unfortunately, despite the code logically making sense, I still could not figure how to work this out. All I wanted was for the user to see the questions associated with the opponent upon opponent collision. I then had an epiphany and realized that I could display these questions upon clicking a button. Therefore, I then gave each opponent their own button and was finally able to display the questions. Once I had implemented this, I was able to finally trigger the events required.  
* Moving Character within scope of game:
  When curating my program initially, I was unsure how I would be able to move my character around. I was not sure if I would be able to use the arrow keys or the mousepad to move my character. I settled on the arrow keys, and I was able to move the character using these. However, I had soon realized that I was caught in an infinite issue in which my character could move forever in any direction. I then had to add conditionals into my function that moves my character to bound the character to the pygame window itself, in order to properly keep my character bounded.
* Button Clickability & triggering:
  Once I had realized that I was going to use buttons to trigger the event that displayed the various questions on the screen, I used my button class and made 4 different buttons with different text that led to 4 different sets of questions. However, they all had the same x and y coordinates, so even though these buttons were only visible in their corresponding rooms, all buttons led to the same set of questions (the first initialized button's questions). Once I had realized this, I gave each button unique x and y coordinates so that each button would not conflict with one another.
* Displaying other sprites:
  Upon program start, I was unsure on how I would get my characters and opponents to be displayed on the screen, as most google images had built in backgrounds. I was first going to use a graphics software to make all of these images have a transparent background so that they could be easily manipulated and imported in my game. However, once I had tried using some software, I had realized that this was way out of my league and tried figuring out another way to do this. I then downloaded sprite JPGs from a popular video game series, as these are easily manipulatible and have transparent backgrounds. This allowed me to import unique opponents and my character as unique without having to get bogged down with additional graphics software.
* Incrementing the score:
  In my game, I created a game mechanic function that is used in tandem with the a score function. This GameMechanic function randomizes the questions, checks if the answer is correct, displays the home button, and links other functions. This function has another function nested into it, which displays the score variable on the screen and increments/decrements the score accordingly. This score function provided me trouble as I was not sure exactly how to take the score variable into account in the function, and I had to figure out where to increment/decrement this function. I tried doing this in the called score function itself, and this led to an infinite loop. I took a step back from this issue and looked at it a few days later. I realized that I could increment/decrement my score variable in the GameMechanic function in the line before the function was called where score is passed as the parameter. This now makes the score mechanic function propelerly. 




{Describe the testing process using paragraphs and numbered bullet lists how to manually test the software here.}

## Directions and Grading Rubric

To review the project directions or update the grading rubric review the [DIRECTIONS.md](DIRECTIONS.md) file.

All rights reserved to The Pokemon Company for their character sprites, and to Nintendo for their background images. No profit will be made off of this project, and this was solely made for educational purposes. 
