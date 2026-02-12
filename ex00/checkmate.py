#!/usr/bin/env python3

def king_kong(rows):
    for r, row in enumerate(rows):
        c = row.find('K')
        if c != -1:
            return r, c
    return -1, -1

def checkmate(board):
    if not board:
        print("Fail")
        return

    rows = board.splitlines()

    if not rows:
        print("Fail")
        return

    height = len(rows)
    width = len(rows[0])

    if width != height:
        print("Fail")
        return

    for row in rows:
        if len(row) != width:
            print("Fail")
            return

    k_r, k_c = king_kong(rows)

    if k_r == -1:
        print("Fail")
        return

    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    for dr, dc in directions:
        dist = 1
        
        while True:
            nr, nc = k_r + (dr * dist), k_c + (dc * dist)

            if not (0 <= nr < height and 0 <= nc < width):
                break

            piece = rows[nr][nc]

            if piece == '.':
                dist += 1
                continue

            if piece == 'R' and (dr == 0 or dc == 0):
                print("Success")
                return

            if piece == 'B' and (dr != 0 and dc != 0):
                print("Success")
                return

            if piece == 'Q':
                print("Success")
                return

            if piece == 'P' and dist == 1 and dr == 1 and (dc == -1 or dc == 1):
                print("Success")
                return

            break 

    print("Fail")