#!/usr/bin/env python

import sys
import os.path


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
