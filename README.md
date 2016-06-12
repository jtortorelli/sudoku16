# Sudoku 16

## Requirements
This is a reimplementation of an AI agent written for my master's circa 2012-2013. The requirements for the final project were as follows:

- Design and implement two AI agents to solve a 16 x 16 Sudoku puzzle
- The puzzle will meet the following format requirements:
    - The puzzle must be loaded from a plain text file
    - The text file contains 16 lines of 16 characters each, mimicking the format of a traditional Sudoku puzzle
    - Any 16 unique symbols may be used, as long as all 16 symbols appeared in the puzzle's starting state at least once
        - In fact, the final program must be able to solve a Sudoku puzzle irrespective of the symbols used (do not code for a specific character set)
    - Blank spaces in the Sudoku puzzle are represented with a hyphen '-'
- The first agent will attempt to solve the puzzle using a brute force algorithm that assigns values to each empty space as it traverses the puzzle sequentially
- The second agent will solve the puzzle using the minimum remaining values (MRV) approach to solve the puzzle
- Submit a paper describing the differences in performance between the two agents

## Discussion
This is the second of the two agents, implementing the MRV approach. First it constructs the puzzle in memory using a matrix data structure. Then it creates a series of sets to represent

1. The master symbol set (the 16 unique symbols used in the puzzle)
2. A set for each row in the puzzle
3. A set for each column in the puzzle
4. A set for each 4 x 4 square in the puzzle

Finally it creates a list of Space objects to represent the empty spaces of the puzzle. Each space is aware of its **constraints**, i.e., the *list of symbols that could possibly occupy that space*, taken from the difference between the master set and sets for the row, column or square that space occupies.

Using the MRV technique, the program first sorts all the empty spaces by the number of constraints, from least to greatest. The first space after sorting is considered and an assignment is made. The function calls itself recursively to continue making assignments, sorting the empty spaces by constraints each time. Any time the program reaches a dead end - when a space is encountered for which no assignment is possible - the recursion back tracks to attempt another assignment and continues. This continues until the goal state is reached (all rows, columns and squares completed correctly), or if it can be determined that no solution exists for the given puzzle.

Performance is measured as a function of time (taken in seconds) and in the total number of assignments made during the solution. For comparison's sake, the MRV agent made 141 assignments before arriving at a solution for a hard puzzle (time: < 1 second), whereas the brute force agent made 34.5 million assignments to arrive at the same solution (time: > 5 minutes).

## Usage
`python sudoku16_solver.py <path_to_file>.txt`