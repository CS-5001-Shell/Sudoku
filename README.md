# Sudoku Helper

This project requires the following concepts:

- Recursion
- Functions
- Complex Logic

## Project Setup

The repository for this assignment includes the following:

1. sudoku.py - This Python file includes documentation for all of the functions that you will implement for this program.
2. test/sudoku_test.py - These are the test cases that your solution must pass in order to earn full credit. Do not change this file.
3. boards.py - This includes several example boards that are used by sudoku_test.py. Do not change this file.
4. boards/ - This directory includes several text files that represent sudoku boards.  
5. sample_output.txt - This text file shows an example of the output your program may produce.

## Overview

For this assignment, you will write a Python program that can check a sudoku board for correctness and solve the sudoku puzzle if a solution exists.

It is recommended that you play a few games to familiarize yourself with Sudoku before you begin on this assignment: [https://sudoku.com/](https://sudoku.com/)

Your program will not implement a complete sudoku game where the user can fill in squares. It will only implement several "helper" functions.

The main logic of this program will open a board, determine whether the rows, columns, and subsquares are valid, and solve the board if the user so wishes.

In your program, a sudoku board will be represented as a two-dimensional list. The outer list will have nine rows. Each row is represented by an inner list that includes nine integers.

The text files in the board/ directory of the project3 repository are text representations of the board.

A subsquare is a 3x3 square. There are nine subsquares, and their upper-left corners are at (0, 0); (0, 3); (0, 6); (3, 0); (3, 3); (3, 6); (6, 0); (6, 3); (6, 6). 

## Requirements and Assumptions

1. You are required to implement the six functions specified in sudoku.py. You may not modify the parameter list or return value of any of the required functions. You may implement additional functions as well as a main function that will implement the user interface logic.
2. `read_board` will read a text file from the boards/ directory and convert it into a two-dimensional list representing a board.
3. `check_rows` will take a two-dimensional list as a parameter and will return True if all rows are complete and correct. Each row must contain all numbers 1 - 9 without any repeating numbers.
4. `check_columns` will take a two-dimensional list as a parameter and will return True if all columns are complete and correct. Each column must contain all numbers 1 - 9 without any repeating numbers.
5. `check_squares` will take a two-dimensional list as a parameter and will return True if all subsquares are complete and correct. Each subsquares must contain all numbers 1 - 9 without any repeating numbers.
6. `candidate_values` is a required function that will be used by `solve`. It will return all possible values that can go in a given square. A number can go in a square if it does not already appear in the row, column, or subsquare where the square is located.
7. `solve` will generate a solution if one exists. Note that if no solution exists the board passed as a parameter to solve must be in its original state after the function completes. 
8. The logic of your main function will produce output similar to that in sample_output.txt. The general logic is as follows:
   1. Print a welcome message
   2. Prompt the user for a filename
   3. If the board is complete and correct, report that to the user.
   4. Otherwise, report whether the rows, columns, and subsquares are correct and ask the user if they want to solve the puzzle. 
       1. If the user wants to solve report the solution or that the board was unsolvable.
   5. Ask the user whether they want to go again.

## Hints
`solve` will be a recursive function. It will use the `check_*` functions and the `candidate_values` function. The general logic of the function is as follows (many pieces are missing, like the base case!):
  1. Find the next empty square.
  2. For each possible value for that square
     1. Assign that value
     2. Recursively try to solve the puzzle.
     3. If there is a solution, return True. Otherwise, try the next value.
  3. If all possible values for the square have been tried and no solution is found, return False.

You are welcome to implement any additional functions that would be helpful for
the logic or debugging. My solution uses six other functions in addition to
main.

## Assignment Submission

To earn credit for this assignment you must commit all of your changes to your GitHub repository prior to the deadline. It is strongly recommended that you commit your changes regularly. Do not wait until you complete all four parts of the assignment to upload your (partial) solution.

Step 1 - *Stage Changes*: Select the Source Control icon in the VSCode left menu. In the Changes section, click the + to *Stage All Changes*.

Step 2 - Commit Message: In the text box that says Message enter a meaningful message that describes the change you just completed.

Step 3 - *Commit & Push*: Select the down arrow in the blue box that says Commit. Choose *Commit & Push*.

Step 4 - Verify: Visit the repository on GitHub to confirm that your changes were uploaded successfully