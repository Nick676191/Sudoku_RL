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
        # initialize the sudoku grid characteristics
        self.rows = 9
        self.columns = 9
        self.numStartVals = numStartVals
    
    def gridCreator(self):
        # creating the sudoku grid object
        arrLength = self.rows * self.columns
        self.sudokuGrid = np.ones(arrLength).reshape((9, 9)) * 100

        return self.sudokuGrid
    
    def checker(self):
        # check that each row only contains one value of the digits 0-9
        for row_num in range(self.rows):
            row_check = self.sudokuGrid[row_num][np.where(self.sudokuGrid[row_num] < 10)]
            if len(np.unique(row_check)) != len(row_check):
                return False
        
        # check that each column only contains one value of the digits 0-9
        for col_num in range(self.columns):
            col_check = self.sudokuGrid[:, col_num][np.where(self.sudokuGrid[:, col_num] < 10)]
            if len(np.unique(col_check)) != len(col_check):
                return False
        
        # check that each 3x3 grid within the sudoku grid only contains one value of the digits 0-9
        index_list = [slice(0, 3), slice(3, 6), slice(6, 9)]
        for i in index_list:
            for j in index_list:
                nine_group = self.sudokuGrid[i, j].flatten()
                nine_check = nine_group[np.where(nine_group < 10)]
                if len(np.unique(nine_check)) != len(nine_check):
                    return False
        
        # assuming that the grid follows the suduko rules if none of the checks above return a false value
        return True

    def gridFiller(self):
        # looping through the range of the number of start values to fill the sudoku grid with all of those values
        for _ in range(self.numStartVals):
           ticker = True
           while ticker:
                # initialize boolean that indicates if a number is going to be filled into a slot within the grid that has already been filled
                same = False
                randGridX = np.random.randint(self.rows)
                randGridY = np.random.randint(self.columns)
                randDigit = np.random.randint(1, 10)
                # if grid spot isn't already filled, fill it with randomly generated digit 1-9
                if self.sudokuGrid[randGridX, randGridY] == 100:
                    self.sudokuGrid[randGridX, randGridY] = randDigit
                else:
                    # toggle variable to true if sudoku grid already has a digit 0-9 in the spot that has been genrated
                    same = True

                # if the digit space is already filled, restart the while loop to generate a new space and number
                if same:
                    continue
                # if grid follows rules with new value, exit out of the while loop and move onto generating the next input value to the grid
                elif self.checker():
                   ticker = False
                # change input grid value back to 100 if it breaks one of the three sudoku rules above
                else:
                    self.sudokuGrid[randGridX, randGridY] = 100
        
        return self.sudokuGrid

if __name__ == "__main__":
    hard_puzzle = Sudoku(18)
    hard_puzzle.gridCreator()
    starting_hard_puzzle = hard_puzzle.gridFiller()
    print(starting_hard_puzzle)