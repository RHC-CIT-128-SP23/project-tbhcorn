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

python -m pip install --upgrade pip (should be version 23.1.2)
pip install --upgrade python (should be version 3.11.3 - if not, download from python website)
python -m pip install pygame ( should be version 2.3.0)

Since the game itself imports pygame, this should be everything required for the player of said game. 

{Add any install instructions, if needed. This includes how to install included modules or libraries as well as configurations. You may remove this section if no special instructions are required.}

## Software Engineering

Designing and developing this program, I used object-oriented programming techniques to follow the given rubric while also fostering clarity within my code. 
I created three classes (character, button, and door) as I drew multiple characters, buttons, and doors within my program. This allowed me to avoid code redundancy and foster legibility within my code. I also gave each one of my major game events their own function, so that I could just call these functions in the main game loop for ease of use. This includes the: game mechanic, background/opponent changes upon the user entering a door, character movement (for the user), characters being drawn on the screen, and for corresponding text to be shown when a certain opponent/background is displayed. Below these functions and classes, I have similar code grouped near each other. This subsequent code involves the use of dictionaries to link questions and their answers, and then these questions and their answers are correspondingly linked to the button that displays them upon click.

{Describe the software engineering techniques used for the design and development of this program.}

## Testing Script

My testing script will be described and broken up by the major game elements that I struggled the hardest with while buildng this game.




{Describe the testing process using paragraphs and numbered bullet lists how to manually test the software here.}

## Directions and Grading Rubric

To review the project directions or update the grading rubric review the [DIRECTIONS.md](DIRECTIONS.md) file.

All rights reserved to The Pokemon Company for their character sprites, and to Nintendo for their background images. No profit will be made off of this project, and this was solely made for educational purposes. 
