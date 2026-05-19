from sudoku_creator import Sudoku
import numpy as np

"""Assuming that I will start at the top left of the grid, or the first unfilled point of the grid in the top-left, to start filling out the grid
1. Fill out each value in each grid point according to the values in the respective column, row, and 3x3 grid that each value is in
2. Move onto next value and perform step 1
3. Keep doing this process until I run into a cell where the process above is infeasible. Move back to one of the previous values to change
one of those previous values to make the other grid cell work.
"""

# generating an easy puzzle with 50 values to start
hard_puzzle = Sudoku(40)
hard_puzzle.gridFillerP2()
starting_hard_puzzle = hard_puzzle.gridReducer()
print(starting_hard_puzzle)

# def gridFinder(index):
#     if index < 3:
#         return 0
#     elif 3 <= index < 6:
#         return 1
#     else:
#         return 2

# # look at the values in a column, row, and 3x3 grid of a specific cell in the grid. Find the numbers that could be input into the blank cell
# def numRefiner(puzzle, row_index, col_index):
#     row_nums = puzzle[row_index][np.where(puzzle[row_index] < 10)]
#     col_nums = puzzle[:, col_index][np.where(puzzle[:, col_index] < 10)]

#     index_list = [slice(0, 3), slice(3, 6), slice(6, 9)]
#     iRow = gridFinder(row_index)
#     jCol = gridFinder(col_index)
#     nine_group = puzzle[index_list[iRow], index_list[jCol]].flatten()
#     grid_nums = nine_group[np.where(nine_group < 10)]

#     fullNumSet = set(np.array([i for i in range(1, 10)]))
#     refine = set(np.unique(np.concat([row_nums, col_nums, grid_nums])))

#     return np.array(list(fullNumSet.difference(refine)))

# def cellCounter(array, num):
#     count=0
#     for arr in array:
#         if num in arr:
#             count+=1
    
#     return count

# def cellSearcher(puzzle, row_index, col_index):
#     """Want to look at a specific cell that is blank to compare the potential numbers that it could fill in with the other cells
#     potential values in its own respective 3x3 grid, row, and column"""
    
#     print(f"cell searcher function has been called for the cell at ({row_index}, {col_index})")
    
#     index_list = [slice(0, 3), slice(3, 6), slice(6, 9)]
#     iRow = gridFinder(row_index)
#     jCol = gridFinder(col_index)
#     nine_group = puzzle[index_list[iRow], index_list[jCol]]
#     blank_grid_nums = np.where(nine_group == 100)
#     blank_grid_nums = np.array([blank_grid_nums[0], blank_grid_nums[1]])

#     if iRow == 1:
#         new_row_vals = np.add(blank_grid_nums[0], 3)
#         blank_grid_nums[0] = new_row_vals
#     elif iRow == 2:
#         new_row_vals = np.add(blank_grid_nums[0], 6)
#         blank_grid_nums[0] = new_row_vals
    
#     if jCol == 1:
#         new_col_vals = np.add(blank_grid_nums[1], 3)
#         blank_grid_nums[1] = new_col_vals
#     elif jCol == 2:
#         new_col_vals = np.add(blank_grid_nums[1], 6)
#         blank_grid_nums[1] = new_col_vals
        
#     blank_grid_indexes = np.stack((blank_grid_nums[0], blank_grid_nums[1]), axis=-1)
    
#     toggle = False
#     for blank_arr in blank_grid_indexes:
#         if np.all(np.array([row_index, col_index]) == blank_arr):
#             toggle = True
#             break
    
#     if toggle == False:
#         blank_grid_indexes = np.vstack((blank_grid_indexes, np.array([row_index, col_index])))

#     grid_possibilities = []
#     for brow, bcol in blank_grid_indexes:
#         print(brow, bcol)
#         print(row_index, col_index)
#         if (brow != row_index) or (bcol != col_index):
#             potential_nums = numRefiner(puzzle, brow, bcol)
#             grid_possibilities.append(potential_nums)
#         else:
#             specific_cell_nums = numRefiner(puzzle, brow, bcol)
#             print(f"The specific cell nums var is {specific_cell_nums}")
    
#     # have it choose the number for the specific cell that we are in that shows up the least in the potential cells for the grids we have chosen
#     num_occurences = [cellCounter(grid_possibilities, num) for num in specific_cell_nums]

#     num_to_choose = specific_cell_nums[np.argmin(num_occurences)]  

#     return num_to_choose, specific_cell_nums

# def oneOffFinder(puzzle, blank_indexes):
#     oneOffList = []
#     for index in blank_indexes:
#         nums = numRefiner(puzzle, index[0], index[1])
#         if len(nums) == 1:
#             oneOffList.append({(index[0], index[1]): nums[0]})
    
    # return oneOffList

# def oneOffFiller(puzzle, row_num, col_num, num):
#     print(f"filling the puzzle at position ({row_num, col_num}) with the only choice, {num}")
#     puzzle[row_num, col_num] = num
#     return puzzle

# # I need this recursive filler to go back to a previous index if the current index doesn't have any number to choose from, then after it has chosen a number for that specific index, I need it to go back to the index that is right ahead of it
# def recursive_filler(puzzle, indexes, index_pair_num):
#     row_num = indexes[index_pair_num][0]
#     col_num = indexes[index_pair_num][1]
#     nums = numRefiner(puzzle, row_num, col_num)
#     print(f"The available numbers at position ({row_num}, {col_num}) are {nums}")
#     if len(nums) != 0:
#         choice, num_choices = cellSearcher(puzzle, row_num, col_num)
#         print(f"filling the puzzle at position ({row_num, col_num}) with {choice}")
#         puzzle[row_num, col_num] = choice
#         return (puzzle, index_pair_num)
#     else:
#         print("Going back to the the previous unfilled position")
#         return recursive_filler(puzzle, indexes, index_pair_num-1)

# # if we have been bouncing between the same two indexes for more than 10 goes lets flag it
# def checkInfinite(index_pair_tracker):
#     if (len(set(index_pair_tracker[-15:])) < 3) and (len(index_pair_tracker) > 20):
#         return True
#     else:
#         return False


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

# index_list = np.where(starting_easy_puzzle > 10)
# empty_indexes = np.stack((index_list[0], index_list[1]), axis=-1)

puzzle_copy = starting_hard_puzzle.copy()
# for i in range(len(empty_indexes)):
#     puzzle_copy = recursive_filler(puzzle_copy, empty_indexes, i)

# unsolved = True
# index_num = 0
# index_tracker = []
# while unsolved:
#     index_tracker.append(index_num)
#     puzzle_copy, index_num = recursive_filler(puzzle_copy, empty_indexes, index_num)
#     index_num+=1
#     if checkInfinite(index_tracker):
#         # go back two paces
#         index_num = index_num - 3
#     if checkFinish(puzzle_copy):
#         unsolved = False
    
#     print(index_num)


# print(puzzle_copy)
# row_i = empty_indexes[0][0]
# col_i = empty_indexes[0][1]

# nc, scn = cellSearcher(starting_easy_puzzle, row_i, col_i)

# print(nc, scn)

# going to try to isolate the indexes where there is only one option
# easy_fill_list = []
# for index in empty_indexes:
#     row = index[0]
#     col = index[1]
#     nc, scn = cellSearcher(starting_easy_puzzle, row, col)
#     if len(scn) == 1:
#         easy_fill_list.append([np.array([row, col])])




# index_list = np.where(starting_easy_puzzle > 10)
# empty_indexes = np.stack((index_list[0], index_list[1]), axis=-1)
# easy_list = oneOffFinder(starting_easy_puzzle, empty_indexes)
# print(easy_list)

# for dict in easy_list:
#     key = list(dict.keys())[0]
#     starting_easy_puzzle = oneOffFiller(starting_easy_puzzle, key[0], key[1], dict[key])


# bool = checkFinish(starting_easy_puzzle)

# print(starting_easy_puzzle)
# print(bool)

"""Another possible way to programmatically fill out the sudoku puzzle would be to start at 1 and go to each 3x3 grid
that the number 1 isn't currently in. Then go to the number two and add that number into every 3x3 grid that it currently isn't apart of.
Then do the same thing for the rest of the numbers all the way up to 9."""
"""Psuedo-code for the problem above
1. Loop through every number that can be input into the suduko puzzle (1-9)
2. Find the grid(s) where the respective number currently isn't present. Start in the 3x3 grid where that respective number has the most free options to choose from
3. Create a list that holds all of the indexes of that respective number in the puzzle
4. Ensure that the number that is being pasted into the puzzle doesn't have any similarity to the index of other instances of that number that is already in the puzzle
    4a. Check each blank cell in the grid to see if that blank cell's index (row or col) matches up with any of the row or col vals of the existing instances of that number in the grid currently
    4b. If the index (row and col) does not match up with any of the existing indexes, then we could add the number into the grid and move onto the next grid without that respective number
    4c. If there isn't any cell available to paste the number into the respective 3x3 grid, then we need to undo the cells that we pasted a number into until we hit a 3x3 grid with multiple instances where we could have pasted a number and paste the number into a different spot to try a different route
    4d. Then we would continue the solver back from that point up to the current point using the steps above again
5. Add that number to the puzzle and note its index and add it to the list that holds all of the indexes for that respective number
6. Each time that we are adding in a new number we should check for compliance with the sudoku rules still. If there is no way to correctly paste number into a grid then we can backtrack to move a number to a different cell in a dofferent grid to try and open things up.
7. Once all 9 instances have been correctly pasted into the puzzle loop into the next number
8. continue this loop until all 81 values have been pasted into the grid"""

def flat2grid(digit):
    """Takes a digit and returns the 2d-array index of that digit for a 3x3 grid"""
    if digit < 3:
        return np.array([0, digit])
    elif 3 <= digit < 6:
        return np.array([1, digit - 3])
    else:
        return np.array([2, digit - 6])

def grid2flat(array):
    """Takes a 2d-array index of a 3x3 grid and assigns it its corresponding digit value between 0-8"""
    if array[0] == 0:
        return array[0] + array[1]
    elif array[0] == 1:
        return 3 + array[1]
    else:
        return 6 + array[1]
    
def sGrid2LGrid(row, col, index):
    """Converts a 2-d index for a 3x3 grid into a 2-d index for a 9x9 sudoku grid"""
    if row == 1:
        index[0] = np.add(index[0], 3)
    elif row == 2:
        index[0] = np.add(index[0], 6)
    
    if col == 1:
        index[1] = np.add(index[1], 3)
    elif col == 2:
        index[1] = np.add(index[1], 6)
    
    return index

def indexStacker(positionIndexes):
    indexes = np.stack((positionIndexes[0], positionIndexes[1]), axis=-1)
    return indexes

def ogNumFinder(startingPuzzle):
    startingPositions = {}
    for num in range(1, 10):
        numPositions = np.where(startingPuzzle == num)
        startingPositions[num] = indexStacker(numPositions)
    
    return startingPositions

def gridChecker(puzzle, number):
    """checks each 3x3 grid to see if it contains the number that we are searching for. This 
    function will output the digit of each grid that contains the number specified as keys, and 
    the 2-d array index of that respective number as the values in a dictionary"""
    present_grids = []
    cell_indexes = []
    index_list = [slice(0, 3), slice(3, 6), slice(6, 9)]
    for i in range(len(index_list)):
        for j in range(len(index_list)):
            nine_group = puzzle[index_list[i], index_list[j]].flatten()
            num_check = np.where(nine_group == number)
            if len(num_check[0]) > 0:
                present_grids.append(grid2flat(np.array([i, j])))
                arr_index = flat2grid(num_check[0][0])
                cell_indexes.append(sGrid2LGrid(i, j, arr_index))
    
    return dict(zip(present_grids, cell_indexes))

def rowColChecker(dictionary, gridNum):
    """returns a list of 2-d 3x3 grid arrays that contain a certain number that have the same row or col index as the current 3x3 grid"""
    gridList = []
    keys = dictionary.keys()
    gridNum2d = flat2grid(gridNum)
    keys2d = [flat2grid(key) for key in keys]

    if len(keys2d) > 0:
        for key in keys2d:
            if (key[0] == gridNum2d[0]) or (key[1] == gridNum2d[1]):
                gridList.append(key)
        return gridList
    else:
        return

def blankCellFinder(puzzle, gridNum):
    """Finds the blank cells in a 3x3 grid"""
    index_list = [slice(0, 3), slice(3, 6), slice(6, 9)]
    gridNum2d = flat2grid(gridNum)
    rows = gridNum2d[0]
    cols = gridNum2d[1]
    nine_group = puzzle[index_list[rows], index_list[cols]].flatten()
    blank_indexes = np.where(nine_group == 100)

    return blank_indexes[0]

def listFillableCells(puzzle, gridNum):
    """Finding the cells in a grid that can be filled with a number. Outputs a list that will be appended to the dictionary that is created in 
    the puzzle overview function"""
    blank_cell_tracker = []
    blanks = blankCellFinder(puzzle, gridNum)
    blanks = np.array(blanks, dtype=object)
    blanks2d = np.vectorize(flat2grid, otypes=[np.ndarray])
    blanks = blanks2d(blanks)
    
    for i in range(len(blanks)):
        gridNum2d = flat2grid(gridNum)
        row, col, index = gridNum2d[0], gridNum2d[1], blanks[i]
        blanks[i] = sGrid2LGrid(row, col, index)
        blank_cell_tracker.append(blanks[i])
    
    return blank_cell_tracker

def puzzleOverview(puzzle, numPresentDict):
    """Given a dictionary that lists out which 3x3 grids contain the number we are searching for this function will output a dictionary
    that helps us deconflict the other positions of the specific number in other 3x3 grids in the puzzle currently."""
    gridNumDict = {}
    for gridNum in range(9):
        num_in_adjacent_grid = rowColChecker(numPresentDict, gridNum)
        if num_in_adjacent_grid:
            gridNumDict[gridNum] = ("present", num_in_adjacent_grid)
        else:
            blank_cell_tracker = listFillableCells(puzzle, gridNum)
            gridNumDict[gridNum] = ("fill", blank_cell_tracker)
    
    return gridNumDict

def arrayList2ListList(arrayList):
    """Turns a list full of arrays into a list of lists"""
    listList = []
    for index in arrayList:
        row = index[0]
        col = index[1]
        lister = [row, col]
        listList.append(lister)
    
    return listList


def indexDeconflictor(puzzle, indexesList, gridDigit):
    """Given the list of indexes that show the indexes of a number in a 9x9 grid. Find the index in a 3x3 grid of the 9x9 grid that 
    does not conflict with any of the indexes in the list"""
    blankGridCells = listFillableCells(puzzle, gridDigit)
    blankGridCellsList = arrayList2ListList(blankGridCells)
    row_indexes = [index[0] for index in indexesList]
    col_indexes = [index[1] for index in indexesList]

    for blankCellIndex in blankGridCellsList.copy():
        if (blankCellIndex[0] in row_indexes) or (blankCellIndex[1] in col_indexes):
            blankGridCellsList.remove(blankCellIndex)
    
    return blankGridCellsList


def choicesCreator(puzzle, presentDict, gridDict, key):
    if gridDict[key][0] == "fill":
        choices = gridDict[key][1]
        return choices
        
    else:
        numberIndexes = []
        for gridArr in gridDict[key][1]:
            gridNumber = grid2flat(gridArr)
            numberIndexes.append(presentDict[gridNumber])
        
        choices = indexDeconflictor(puzzle, numberIndexes, key)
        return choices

def puzFill(puzzle, presentDict, choices, key, num):
    print(key, choices)
    i_list = [i for i in range(len(choices))]
    i_choice = np.random.choice(i_list)
    choice = choices[i_choice]
    puzzle[choice[0], choice[1]] = num
    presentDict[np.int64(key)] = np.array([choice[0], choice[1]])

    return puzzle, presentDict


def puzzleReset(puzzle, presentDict, startPositions):
    print("\nUSING PUZZLE RESETTER\n")
    for num in presentDict.copy():
        index = presentDict[num]
        if [index[0], index[1]] in startPositions:
            continue
        else:
            row = index[0]
            col = index[1]
            puzzle[row, col] = 100
            presentDict.pop(num)
    
    gridDict = puzzleOverview(puzzle, presentDict)

    return puzzle, presentDict, gridDict



def numGridChecker(presentDict):
    if len(presentDict) != 9:
        return False
    
    rowChecker = [presentDict[key][0] for key in presentDict]
    colChecker = [presentDict[key][1] for key in presentDict]
    if (len(set(rowChecker)) != 9) or (len(set(colChecker)) != 9):
        return False
    
    return True

def finalPuzzleChecker(totalPresDict):
    for num in totalPresDict:
        if numGridChecker(totalPresDict[num]) == False:
            return False
    
    if len(totalPresDict) != 9:
        return False
    
    return True

def choicesCheck(choicesDict):
    return all(len(val) <= 1 for val in choicesDict.values())

def iterativeGridFiller(puzzle, presentDict, gridDict, numToFill, startPositions, infinite_loop):
    """Checking each 3x3 grid in the puzzle, filling each one, and updating the dictionary that holds all of the present indexes
    of the respective number in the sudoku puzzle currently"""
    numPresentGridDigits = list(presentDict.keys())
    puzResetterTick = 0
    
    while True:
        decreaseNum = False
        choices_dictionary = {}
        for key in range(9):
            if key in numPresentGridDigits:
                continue
            else:
                choices = choicesCreator(puzzle, presentDict, gridDict, key)
                choices_dictionary[key] = choices
                if (len(choices) == 0) and (choicesCheck(choices_dictionary)):
                    print("WE GOT TO GO BACK TO ANOTHER NUMBER TO OPEN UP THE CURRENT NUMBER")
                    decreaseNum = True
                    puzzle, presentDict, gridDict = puzzleReset(puzzle, presentDict, startPositions)
                    break
                elif len(choices) == 0: 
                    puzzle, presentDict, gridDict = puzzleReset(puzzle, presentDict, startPositions)
                    puzResetterTick += 1
                    break
                elif puzResetterTick > 15:
                    infinite_loop = True
                    break
                else:
                    puzzle, presentDict = puzFill(puzzle, presentDict, choices, key, numToFill)
                
            gridDict = puzzleOverview(puzzle, presentDict)
        if numGridChecker(presentDict) or decreaseNum or infinite_loop:
            break
    
    return puzzle, gridDict, presentDict, decreaseNum, infinite_loop

startPosDict = ogNumFinder(starting_hard_puzzle.copy())
totalPresentDict = {}
puzzle_unfinished = True
while puzzle_unfinished:
    for num in range(1, 10):
        infinite_loop = False
        og_num = num
        dec_num = 0
        while True:
            startPos = startPosDict[num]
            print(f"The starting positions for this number, {num}, are:\n{startPos}\n")

            dictNumPresent = gridChecker(starting_hard_puzzle, num)
            print(f"The presentDict object for this number at the start is:\n{dictNumPresent}\n")
            
            gridDictForNum = puzzleOverview(starting_hard_puzzle, dictNumPresent)
            print(f"The gridDict object for this number at the start is:\n{gridDictForNum}\n")
            
            starting_hard_puzzle, numGridDict, numPresentDict, decreaseTracker, infinite_loop = iterativeGridFiller(starting_hard_puzzle, dictNumPresent, gridDictForNum, num, startPos, infinite_loop)
            
            if decreaseTracker:
                totalPresentDict[num] = {}
                num -= 1
                dec_num += 1
                starting_hard_puzzle, numPresentDict, numGridDict = puzzleReset(starting_hard_puzzle, totalPresentDict[num], startPosDict[num])
            else:
                totalPresentDict[num] = numPresentDict
            
            if (dec_num > 0) and (numGridChecker(numPresentDict)):
                num += 1
            
            if dec_num > 10:
                infinite_loop = True
                break
            
            if numGridChecker(totalPresentDict[og_num]) or infinite_loop:
                break
            
        if infinite_loop:
            for num in totalPresentDict:
                starting_hard_puzzle, numPresentDict, numGridDict = puzzleReset(starting_hard_puzzle, totalPresentDict[num], startPosDict[num])
            break

    if finalPuzzleChecker(totalPresentDict):
        print(f"Result after pasting the specified numbers into the grid\n{starting_hard_puzzle}\n")
        # print(f"Dictionary object that holds all of the index values for each respective number in the grid\n{totalPresentDict}")
        break