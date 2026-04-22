import numpy as np
"""The rules of Sudoku are:
1. Every row should have the numbers 0-9 in it only once
2. Every column shold have the numbers 0-9 in it only once
3. Every 3x3 grid within the 9x9 matrix should have the numbers 0-9 in it only once

I want to set up the class so that it fills the grid with a certain amount of random integers strategically placed to create a
sudoku grid object that can be used by the RL algorithm to learn how to solve sudoku puzzles. This will allow me to rapidly choose
starting sudoku configurations.

Pseudocode
1. Create the 9x9 sudoku grid where numbers can be input into the matrix.
2. Fill the grid with a specific amount of numbers that the user can specify. To give more context to the user specification; if the 
user wants to train the algorithm on hard puzzles they can specify less spots (17 at a minimum) to be filled in for the puzzle
3. Ensure the filled in puzzle follows the rules listed above. Start filling in the puzzle at a random point in the grid and use a
random integer 0-9 to fill in that point.
3a. While filling in the puzzle check that each row, column, and 3x3 grid only has a unique 0-9 value. If the new random point with
a random 0-9 integer satisfies these rules, then add it to the matrix. 
3b. Continue this process until the user specified amount of numbers is added to the puzzle and meets all criteria."""

class Sudoku:
    def __init__(self, numStartVals):
        self.rows = 9
        self.columns = 9
        self.numStartVals = numStartVals
    
    def gridCreator(self):
        arrLength = self.rows * self.columns
        self.sudokuGrid = np.ones(arrLength).reshape((9, 9)) * 10

        
        return self.sudokuGrid
    
    def checker(self):
        for row_num in range(self.rows + 1):
            for col_num in range(self.columns + 1):

    
    def gridFiller(self):
        for _ in range(self.numStartVals):
           randGridX = np.random.randint(self.rows + 1)
           randGridY = np.random.randint(self.columns + 1)

           randDigit = np.random.randint(10)

if __name__ == "__main__":
    hard_puzzle = Sudoku(18)
    print(hard_puzzle.gridCreator())