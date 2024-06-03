# Hangman

In this game, I recreated the classic Hangman game, also known as Jogo da Forca. My version features 4 difficulty levels: normal, tormento, inferno, and nightmare.

## Features

- **4 Difficulty Levels:** Choose from the difficulty levels: normal, tormento, inferno, and nightmare.
- **Progress Visualization:** As the player makes mistakes, parts of the hangman's body are drawn on the screen.
- **Game Over:** The game ends when the player guesses the correct word or when the hangman is fully drawn.
- **Restart Game:** After the game ends, you can restart it to play again.

## What appears at each error for the respective difficulties:

- **Normal:** Head, torso, left arm, right arm, left leg, right leg, GAME OVER
- **Tormento:** Head, torso, both arms, both legs, GAME OVER
- **Inferno:** Head, rest of the body, GAME OVER
- **Nightmare:** Everything appears, GAME OVER

## Installation Requirements

- Python 3.x
- tkinter
- tqdm
- easygui

## Required Libraries

- `random.choice`: Module for random word selection.
- `tkinter`: Graphical module for the game's interface.
- `tqdm`: Module for displaying progress bars.
- `time`: Module for time manipulation.
- `easygui`: Module for creating menus.
- `os` and `sys`: Modules for restarting the program from scratch.

## How to Play

1. Ensure that Python and the necessary libraries are installed on your system.
2. Clone or download the repository of this game.
3. Run the main game file.
4. Choose the desired difficulty level from the menu.
5. Try to guess the correct word by typing letters.
6. As you make mistakes, parts of the hangman's body are drawn on the screen.
7. Try to guess the word before the hangman is fully drawn.
8. The game ends when you guess the word or when the hangman is complete.

## How to Contribute

If you wish to contribute to the development of this game, follow these steps:

1. Fork the repository.
2. Make your modifications and improvements to the code.
3. Test your changes to ensure they work correctly.
4. Submit a pull request describing the changes you made and the reasons for them.

## Author

This game was recreated by Ageu Felipe Nunes Moraes as part of an academic project inspired by the classic Hangman game. For questions or suggestions, contact [ageumoraes67@gmail.com](mailto:ageumoraes67@gmail.com).

## Disclaimer

This is a software project developed by an individual and is not affiliated with the original Hangman game or its creators.
