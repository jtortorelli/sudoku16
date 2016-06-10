#!/usr/bin/env python

import sys
import os.path


def main(argv):
    if len(argv) < 1 or len(argv) > 1:
        print('Requires exactly one argument (filename)')
        return
    if not os.path.isfile(argv[0]):
        print('File not found: ' + argv[0])
        return
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
