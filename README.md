# SolverCSP
Solver of a Sudoku game as CSP. 

* To run the program is needed python 3.4 or later, most of the function inside csp.py have been taken from AIMA's code 
(https://github.com/aimacode/aima-python) as a base solver for general csp (some is slightly modified, I explained
the changes in the comments).

* The class sudokuCSP creates the objects needed for the general csp solver like neighbor, variables, domain for a sudoku 
game as a constraint satisfaction problem.

* The file Test.py contains code to execute tests for each inference algorithm on a sudoku board (it is possible 
to choose which board).

A pdf explaining the work (how to model the sudoku problem and tests) have been added.
