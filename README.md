# Tic Tac Toe Game with GUI

This is a simple implementation of the Tic Tac Toe game with a graphical user interface (GUI) using the Tkinter library in Python. The game allows two players to take turns placing their marks (X and O) on a 3x3 grid. The first player to get three of their marks in a horizontal, vertical, or diagonal row wins the game.

## Prerequisites

To run this game on your local machine, you need to have Python installed. The code is written in Python 3, so make sure you have a compatible version installed.

## Getting Started

To get started with the game, follow these steps:

1. Clone the repository or download the source code files.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command to install the required dependencies:
4. Once the dependencies are installed, run the following command to start the game:

## How to Play

1. The game starts with an empty 3x3 grid displayed on the GUI.
2. Two players take turns clicking on the cells of the grid to place their marks.
3. Player 1's mark is "X" and Player 2's mark is "O".
4. The first player to get three of their marks in a row (horizontal, vertical, or diagonal) wins the game.
5. If all the cells are filled and no player has won, the game ends in a tie.

## GUI Controls

The game GUI consists of buttons representing the cells on the grid. To place a mark, click on an empty cell. The current player's mark will appear in the clicked cell.

## Class Structure

The code is structured into a single class called `TicTacToe`. Here is a brief overview of the class and its methods:

- `__init__()`: Initializes the game by setting up the current player and the game board.
- `create_board()`: Creates the game board GUI using Tkinter buttons.
- `on_button_click(row, col)`: Handles the button click event and updates the game state accordingly.
- `update_button_text(row, col)`: Updates the text of a button to display the current player's mark.
- `is_board_full()`: Checks if the game board is full.
- `check_win(player)`: Checks if the given player has won the game.
- `reset_board()`: Resets the game board and GUI to their initial state.
- `show_message_box(message)`: Displays a message box with the specified message.
- `run()`: Runs the game by starting the Tkinter main event loop.

## Libraries Used

The following libraries are used in this project:
- `tkinter`: The standard Python library for creating GUI applications.
- `messagebox` from `tkinter`: A module within tkinter that provides a simple way to display message boxes.

## What You Can Learn

By studying this Tic Tac Toe game implementation, you can learn the following:

- Building a GUI application using Tkinter.
- Handling button click events and updating the GUI accordingly.
- Managing game state and logic.
- Implementing win conditions and tie conditions.
- Resetting the game and GUI to their initial state.

Feel free to modify and improve the game as you see fit. Have fun playing Tic Tac Toe!

## Acknowledgments

- This game was created as a simple educational project.
- The GUI is built using the Tkinter library in Python.

Created by Ahmed Rifai.
