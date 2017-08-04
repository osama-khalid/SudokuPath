# SudokuPath
Finds the Longest Monotonically increasing path in sudoku puzzles
An generalization of the longest path in binary tree algorithm to grids of arbitrary sizes.
see example(https://raw.githubusercontent.com/osama-khalid/SudokuPath/master/Sudoku.jpg). The red line illustrates the longest path

An implementation of the Sudoku-sub-problem that I solve everyday after finishing the DailyIowan Sudoku Puzzle.
Some definitions:
A directed edge exists between two neighbors if one neighbor is exactly 1 higher than the other. 
  see example(https://raw.githubusercontent.com/osama-khalid/SudokuPath/master/ValidPaths.png)
A neighbor is defined as a grid in any grid that touches the current grid (left/right/up/down/diagonally across)
  see example(https://raw.githubusercontent.com/osama-khalid/SudokuPath/master/Neighbors.png)
