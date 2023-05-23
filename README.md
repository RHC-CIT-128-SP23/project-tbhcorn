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

[Add a Link to your video demonstration] 
https://youtu.be/JFYFD-PJuCE - viewable by link only


### Install Instructions

For use in VS Code:

You must make sure that pip, python, and pygame are all up to date in order for this program to properly be run.

[Pygame MUST be up to date for this game to run.]

Here is how you can do so.

In your VS Code terminal (click "new terminal" from terminal in upper left hand corner), type:

* python -m pip install --upgrade pip (should be version 23.1.2)
* pip install --upgrade python (should be version 3.11.3 - if not, download from python website)
* python -m pip install pygame ( should be version 2.3.0)

Since the game itself imports pygame, this should be everything required for the player of said game. 

The user will then access this github repository, and open the project in VS Code. Then, the user will access the main.py file, and click "Run - Start Debugging". The game will initialize for a moment, and then the user will be able to play it!

{Add any install instructions, if needed. This includes how to install included modules or libraries as well as configurations. You may remove this section if no special instructions are required.}

## Software Engineering

Designing and developing this program, I used object-oriented programming techniques to follow the given rubric while also fostering clarity within my code. 
I created three classes (character, button, and door) as I drew multiple characters, buttons, and doors within my program. This allowed me to avoid code redundancy and foster legibility within my code. I also gave each one of my major game events their own function, so that I could just call these functions in the main game loop for ease of use. This includes the: game mechanic, background/opponent changes upon the user entering a door, character movement (for the user), opponents being drawn on the screen, and for corresponding text to be shown when a certain opponent/background is displayed. Below these functions and classes, I have similar code grouped near each other. This subsequent code involves the use of dictionaries to link questions and their answers, and then these questions and their answers are correspondingly linked to the button that displays them upon click.

{Describe the software engineering techniques used for the design and development of this program.}

## Testing Script

For my testing script, the core mechanics of my game will be discussed with the expected output upon given action for an interaction.
* Character Movement: 
1) The user's character moves around our game using the arrow keys, bounded by the game window.
2) When the user presses the up arrow key, the character will move upwards.
3) When the user presses the down arrow key, the character will move downwards.
4) When the user presses the right arrow key, the character will move to the right.
5) When the user presses the left arrow key, the character will move to the right.
6) If the character did not move upon pressing any of these keys, that would be an issue. Luckily, this is not the case.
* Score Validation:
1) For any of the math rooms, the user enters their answer.
2) Using a for loop and a dictionary, the game verifies the user's answer.
3) If the user's answer is correct, the game shuffles 1 of 5 possible congratulatory output messages and outputs it, in addition to incrementing the score.
4) If the user's answer is incorrect, the game shuffles 1 of possible encouraging output messages and outputs it, in addition to decrementing the score. 
5) If this function did not work properly, the game would neither decrement nor increment properly upon user input. It also would not shuffle through the output messages.
6) The user can type in any sort of input values from the keyboard to test this feature, and the score validation will still occur in the same method. To my knowledge, there is no set of values that explicitly trigger errors.
* Buttons:
7) In this game, there is a button in each of the character's rooms as well as on the game screen. By clicking each of these buttons, the game properly sends the user to the right place. 
8) When the multiplication button is clicked, the game screen with multiplication questions is shown. 
9) When the division button is clicked, the game screen with division questions is shown. 
10) When the addition button is clicked, the game screen with addition questions is shown. 
11) When the subtraction button is clicked, the game screen with subtraction questions is shown. 
12) When the home button is clicked on the game screen (for any set of questions), the user returns to the room that they originated from.  
13) If the game did not use the button directory correctly, the user would not see the corresponding questions or return to their home room.
* Doors:
14) This game has 4 doors that correspond to the subdivision of math which they are testing.
15) When the user's character collides with the addition door, they travel to the addition room.
16) When the user's character collides with the subtraction door, they travel to the subtraction room.
17) When the user's character collides with the division door, they travel to the division room. 
18) When the user's character collides with the multiplication door, they travel to the multiplication room.
19) If the collision detection function did not work properly, the user's character would not travel upon collision and would stay in the welcome room. 

{Describe the testing process using paragraphs and numbered bullet lists how to manually test the software here.}

## Directions and Grading Rubric

To review the project directions or update the grading rubric review the [DIRECTIONS.md](DIRECTIONS.md) file.

All rights reserved to The Pokemon Company for their character sprites, and to Nintendo for their background images. No profit will be made off of this project, and this was solely made for educational purposes. 
