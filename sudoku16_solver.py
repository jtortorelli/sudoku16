#!/usr/bin/env python

import sys
import os.path


def get_square_membership(a, b):
    if 0 <= a <= 3:
        if 0 <= b <= 3:
            return 0
        elif 4 <= b <= 7:
            return 1
        elif 8 <= b <= 11:
            return 2
        elif 12 <= b <= 15:
            return 3
    elif 4 <= a <= 7:
        if 0 <= b <= 3:
            return 4
        elif 4 <= b <= 7:
            return 5
        elif 8 <= b <= 11:
            return 6
        elif 12 <= b <= 15:
            return 7
    elif 8 <= a <= 11:
        if 0 <= b <= 3:
            return 8
        elif 4 <= b <= 7:
            return 9
        elif 8 <= b <= 11:
            return 10
        elif 12 <= b <= 15:
            return 11
    elif 12 <= a <= 15:
        if 0 <= b <= 3:
            return 12
        elif 4 <= b <= 7:
            return 13
        elif 8 <= b <= 11:
            return 14
        elif 12 <= b <= 15:
            return 15


def main(argv):
    # check correct number of arguments
    if len(argv) < 2 or len(argv) > 2:
        sys.exit('Requires exactly one argument (filename)')

    # check that argument ends in '.txt'
    if not argv[1].endswith('.txt'):
        sys.exit('Must supply plain text file (using .txt extension)')

    # check that argument is reference to valid file
    if not os.path.isfile(argv[1]):
        sys.exit('File not found: ' + argv[1])

    # read in puzzle
    filename = argv[1]
    src = open(filename, 'r')
    lines = [line.rstrip() for line in src]
    src.close()

    # validate puzzle format
    if len(lines) != 16:
        sys.exit('File does not contain valid puzzle; expected 16 lines, found ' + str(len(lines)) + ' lines')
    for i, line in enumerate(lines):
        if len(line) != 16:
            sys.exit('File does not contain valid puzzle; expected 16 columns, found ' + str(len(line)) + ' columns on line ' + str(i + 1) + '')
    master_set = set()
    for line in lines:
        for n in line:
            if n != '-':
                master_set.add(n)
    if len(master_set) != 16:
        sys.exit("File does not contain valid puzzle; expected 16 unique symbols, found " + str(len(master_set)) + ": " + ', '.join(sorted(master_set)))

    # create matrix structure to hold puzzle information
    matrix = []
    for line in lines:
        row = []
        for n in line:
            row.append(n)
        matrix.append(row)

    # create row sets
    rows = []
    for i, n in enumerate(matrix):
        row = set()
        for m in n:
            if m != '-':
                if m in row:
                    sys.exit('File does not contain valid puzzle; found duplicate value ' + m + ' in row ' + str(i + 1))
                else:
                    row.add(m)
        rows.append(row)

    # create column sets
    cols = []
    for n in range(16):
        col = set()
        for m in range(16):
            if matrix[m][n] != '-':
                if matrix[m][n] in col:
                    sys.exit('File does not contain valid puzzle; found duplicate value ' + matrix[m][n] + ' in column ' + str(n + 1))
                else:
                    col.add(matrix[m][n])
        cols.append(col)

    # create square sets
    squares = []
    for n in range(16):
        squares.append(set())
    for a in range(16):
        for b in range(16):
            if matrix[a][b] != '-':
                square = get_square_membership(a, b)
                if matrix[a][b] in squares[square]:
                    sys.exit('File does not contain valid puzzle; found duplicate value ' + matrix[a][b] + ' in square ' + str(square))
                else:
                    squares[square].add(matrix[a][b])

    # import puzzle as matrix
    # print the puzzle start state
    # create master set
    # create sets for rows, cols, and squares
    # create list of empty spaces
    # start tracking time
    # start solving
    pass


if __name__ == "__main__":
    main(sys.argv)
