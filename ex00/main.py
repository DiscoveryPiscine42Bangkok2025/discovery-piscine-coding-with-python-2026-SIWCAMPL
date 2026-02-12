#!/usr/bin/env python3
from checkmate import *

def main():

    board_q = """\
Q...
....
..K.
...."""

   
    board_r = """\
....
.K.R
....
...."""

   
    board_p = """\
....
.K..
P...
...."""

    
    board_safe = """\
B...
.R..
..K.
...."""

    
    board_large = """\
........
........
...K....
........
........
...Q....
........
........"""

    print("Test Queen (Diagonal): ", end="")
    checkmate(board_q) 
    
    print("Test Rook (Horizontal): ", end="")
    checkmate(board_r) 

    print("Test Pawn (Diagonal 1 step): ", end="")
    checkmate(board_p)

    print("Test Blocked (Should Fail): ", end="")
    checkmate(board_safe) 
    print("Test Large Board: ", end="")
    checkmate(board_large) 

if __name__ == "__main__":
    main()