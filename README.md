# Overview
The following sudoku.py solves any 9x9 standard sudoku puzzle while board.py contains methods used to solve the board.

## HOW TO USE
1. open and run sudoku.py
2. take any sudoku puzzle, and input in the puzzle as a string of just numbers (using 0s for empty boxes) in order from left to right,  moving down a row once you've reached the end of a row
3. press enter and the sudoku solver should output a new string of numbers showing a solution of the sudoku puzzle

## FEATURES
* Custom tile and grouping classes
* Uses depth first search
* Utilizes a backtracking recursive method when hitting a deadend
* Ends program when no solution is possible
