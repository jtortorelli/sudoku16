#!/usr/bin/env python

import sys
import os.path


def main(argv):
    if len(argv) < 2 or len(argv) > 2:
        sys.exit('Requires exactly one argument (filename)')
    if not argv[1].endswith('.txt'):
        sys.exit('Must supply plain text file (using .txt extension)')
    if not os.path.isfile(argv[1]):
        sys.exit('File not found: ' + argv[1])
    # validate file contains valid puzzle
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
