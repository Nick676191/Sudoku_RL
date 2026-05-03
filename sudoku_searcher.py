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

    fullNumSet = set(np.array([i for i in range(1, 10)]))
    refine = set(np.unique(np.concat([row_nums, col_nums, grid_nums])))

    return np.array(list(fullNumSet.difference(refine)))

# I need this recursive filler to go back to a previous index if the current index doesn't have any number to choose from, then after it has chosen a number for that specific index, I need it to go back to the index that is right ahead of it
def recursive_filler(puzzle, indexes, index_pair_num):
    row_num = indexes[index_pair_num][0]
    col_num = indexes[index_pair_num][1]
    nums = numRefiner(puzzle, row_num, col_num)
    print(f"The available numbers at position ({row_num}, {col_num}) are {nums}")
    if len(nums) != 0:
        choice = np.random.choice(nums)
        print(f"filling the puzzle at position ({row_num, col_num}) with {choice}")
        puzzle[row_num, col_num] = choice
        return (puzzle, index_pair_num)
    else:
        print("Going back to the the previous unfilled position")
        return recursive_filler(puzzle, indexes, index_pair_num-1)

# if we have been bouncing between the same two indexes for more than 10 goes lets flag it
def checkInfinite(index_pair_tracker):
    if (len(set(index_pair_tracker[-10:])) < 3) and (len(index_pair_tracker) > 20):
        return True
    else:
        return False


def checkFinish(puzzle):
    # check that each row only contains one value of the digits 0-9
        for row_num in range(9):
            row_check = puzzle[row_num][np.where(puzzle[row_num] < 10)]
            if len(np.unique(row_check)) != len(row_check):
                return False
        
        # check that each column only contains one value of the digits 0-9
        for col_num in range(9):
            col_check = puzzle[:, col_num][np.where(puzzle[:, col_num] < 10)]
            if len(np.unique(col_check)) != len(col_check):
                return False
        
        # check that each 3x3 grid within the sudoku grid only contains one value of the digits 0-9
        index_list = [slice(0, 3), slice(3, 6), slice(6, 9)]
        for i in index_list:
            for j in index_list:
                nine_group = puzzle[i, j].flatten()
                nine_check = nine_group[np.where(nine_group < 10)]
                if len(np.unique(nine_check)) != len(nine_check):
                    return False
        
        # checking that the puzzle has been completed
        puzzle_sum = np.sum(puzzle)
        blank_spaces = np.stack((np.where(puzzle == 100)[0], np.where(puzzle == 100)[1]), axis=-1)
        if (puzzle_sum != 405) or (len(blank_spaces) > 0):
            return False
        
        # assuming that the grid follows the suduko rules if none of the checks above return a false value
        return True

index_list = np.where(starting_easy_puzzle > 10)
empty_indexes = np.stack((index_list[0], index_list[1]), axis=-1)

puzzle_copy = starting_easy_puzzle.copy()
# for i in range(len(empty_indexes)):
#     puzzle_copy = recursive_filler(puzzle_copy, empty_indexes, i)

unsolved = True
index_num = 0
index_tracker = []
while unsolved:
    index_tracker.append(index_num)
    puzzle_copy, index_num = recursive_filler(puzzle_copy, empty_indexes, index_num)
    index_num+=1
    if checkInfinite(index_tracker):
        # go back two paces
        index_num = index_num - 3
    if checkFinish(puzzle_copy):
        unsolved = False
    
    print(index_num)


print(puzzle_copy)
