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
        self.sudokuGrid = np.ones(arrLength).reshape((9, 9)) * 100

        return self.sudokuGrid
    
    def checker(self):
        for row_num in range(self.rows):
            row_check = self.sudokuGrid[row_num][np.where(self.sudokuGrid[row_num] < 10)]
            if len(np.unique(row_check)) != len(row_check):
                return False
        
        for col_num in range(self.columns):
            col_check = self.sudokuGrid[:, col_num][np.where(self.sudokuGrid[:, col_num] < 10)]
            if len(np.unique(col_check)) != len(col_check):
                return False
        
        index_list = [slice(0, 3), slice(3, 6), slice(6, 9)]
        for i in index_list:
            for j in index_list:
                nine_group = self.sudokuGrid[i, j].flatten()
                nine_check = nine_group[np.where(nine_group < 10)]
                if len(np.unique(nine_check)) != len(nine_check):
                    return False
        
        return True

    def gridFiller(self):
        for _ in range(self.numStartVals):
           ticker = True
           while ticker:
                randGridX = np.random.randint(self.rows)
                randGridY = np.random.randint(self.columns)
                randDigit = np.random.randint(10)
                self.sudokuGrid[randGridX, randGridY] = randDigit

                if self.checker():
                   ticker = False
                else:
                    self.sudokuGrid[randGridX, randGridY] = 100
        
        return self.sudokuGrid

if __name__ == "__main__":
    hard_puzzle = Sudoku(21)
    hard_puzzle.gridCreator()
    starting_hard_puzzle = hard_puzzle.gridFiller()
    print(starting_hard_puzzle)