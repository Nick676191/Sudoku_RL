from sudoku_creator import Sudoku
import numpy as np

"""Assuming that I will start at the top left of the grid, or the first unfilled point of the grid in the top-left, to start filling out the grid
1. Fill out each value in each grid point according to the values in the respective column, row, and 3x3 grid that each value is in
2. Move onto next value and perform step 1
3. Keep doing this process until I run into a cell where the process above is infeasible. Move back to one of the previous values to change
one of those previous values to make the other grid cell work.
"""

# generating an easy puzzle with 30 values to start
easy_puzzle = Sudoku(30)
easy_puzzle.gridCreator()
starting_easy_puzzle = easy_puzzle.gridFiller()
print(starting_easy_puzzle)

def gridFinder(index):
    if index < 3:
        return 0
    elif 3 <= index < 6:
        return 1
    else:
        return 2

# look at the values in a column, row, and 3x3 grid of a specific cell in the grid. Find the numbers that could be input into the blank cell
def numRefiner(puzzle, row_index, col_index):
    row_nums = puzzle[row_index][np.where(puzzle[row_index] < 10)]
    col_nums = puzzle[:, col_index][np.where(puzzle[:, col_index] < 10)]

    index_list = [slice(0, 3), slice(3, 6), slice(6, 9)]
    iRow = gridFinder(row_index)
    jCol = gridFinder(col_index)
    nine_group = puzzle[index_list[iRow], index_list[jCol]].flatten()
    grid_nums = nine_group[np.where(nine_group < 10)]

    fullNumSet = set(np.array([i for i in range(10)]))
    refine = set(np.unique(np.concat([row_nums, col_nums, grid_nums])))

    return np.array(list(fullNumSet.difference(refine)))



test = numRefiner(starting_easy_puzzle, 1, 4)
print(test)
print(np.random.choice(test))