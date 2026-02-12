#!/usr/bin/env python3
from checkmate import *

def main():
    # เคสที่ 1: โดน Queen รุกจากระยะไกล (แนวทแยง)
    board_q = """\
Q..................
....
..K.
...."""

    # เคสที่ 2: โดน Rook รุก (แนวตรง)
    board_r = """\
....
.K.R
....
...."""

    # [span_8](start_span)เคสที่ 3: โดน Pawn รุก (เฉียง 1 ช่อง)[span_8](end_span)
    board_p = """\
....
.K..
P...
...."""

    # [span_9](start_span)เคสที่ 4: ปลอดภัย (มีหมากตัวอื่นบล็อกทางไว้)[span_9](end_span)
    board_safe = """\
B...
.R..
..K.
...."""

    # [span_10](start_span)เคสที่ 5: กระดานขนาดใหญ่ขึ้น (สี่เหลี่ยมจัตุรัส)[span_10](end_span)
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
    checkmate(board_q) # คาดหวัง: Success
    
    print("Test Rook (Horizontal): ", end="")
    checkmate(board_r) # คาดหวัง: Success

    print("Test Pawn (Diagonal 1 step): ", end="")
    checkmate(board_p) # คาดหวัง: Success

    print("Test Blocked (Should Fail): ", end="")
    checkmate(board_safe) # คาดหวัง: Fail (เพราะ Bishop บล็อกทาง Rook ไว้)

    print("Test Large Board: ", end="")
    checkmate(board_large) # คาดหวัง: Success

if __name__ == "__main__":
    main()