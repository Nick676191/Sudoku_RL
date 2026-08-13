# Sudoku_RL

## Description
Sudoku_RL is a Python-based project that uses search-based algorithms and other greedy heuristics to create and solve Sudoku puzzles. It provides a framework for generating valid Sudoku grids, allowing users to specify the number of starting values in the puzzle, which dictates the difficulty level.

## Key Features
- Random grid generation to create various Sudoku puzzles.
- Flexible configuration of starting values to adjust puzzle difficulty.
- Validation checks to ensure Sudoku rules are adhered to.
- Supports both grid creation and solution-filling methods.

## Installation Instructions
To install the required packages for Sudoku_RL, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Sudoku_RL.git
   ```
   
2. Navigate into the cloned directory:
   ```bash
   cd Sudoku_RL
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Examples
After installation, you can run the module directly by executing `main.py`, which contains example usage of Sudoku grid creation and validation.

```python
from sudoku_creator import Sudoku

# Create a Sudoku puzzle with 18 starting values
sudoku_puzzle = Sudoku(18)
puzzle_grid = sudoku_puzzle.gridFillerP2()
print("Generated Puzzle:\n", puzzle_grid)

# Check if generated puzzle follows Sudoku rules
is_valid = sudoku_puzzle.checker()
print("Is the puzzle valid? ", is_valid)

finished_puzzle = sudoku_puzzle.gridReducer()
print("Finished Puzzle:\n", finished_puzzle)
is_finished_valid = sudoku_puzzle.checker()
print("Is the finished puzzle valid? ", is_finished_valid)
```

## File/Project Overview
- **sudoku_creator.py**: Contains the `Sudoku` class, which handles the grid creation, filling, validation, and reduction logic.
  
- **main.py**: The entry point of the application that demonstrates the creation and validation of a Sudoku puzzle.

- **requirements.txt**: Lists the dependencies required for the project, ensuring that the correct versions are installed for functionality.

### Class Overview (Sudoku)
- `__init__(self, numStartVals)`: Initializes a Sudoku object with a specified number of starting values.
  
- `gridCreator()`: Constructs an empty Sudoku grid.
  
- `checker()`: Validates the current state of the grid against Sudoku rules.
  
- `gridFiller()`: Randomly fills the Sudoku grid based on the provided starting values and rules.
  
- `gridFillerP2()`: Alternative algorithm for filling the grid in a more strategic manner.
  
- `gridReducer()`: Removes digits from the filled Sudoku grid to convert it into a puzzle format.

Through this project, users can experience generating and validating Sudoku puzzles while gaining insights into algorithmic approaches for puzzle-solving.

Feel free to customize further as needed!