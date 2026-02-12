#!/usr/bin/env python3

def king_kong(rows):
    for r, row in enumerate(rows):
        c = row.find('K')
        if c != -1:
            return r, c
    return -1, -1

def checkmate(board):
    # 1. เช็คว่ามีข้อมูลหรือไม่
    if not board:
        print("Fail")
        return

    rows = board.splitlines()

    # --- ส่วนที่เพิ่ม: เช็คว่าเป็นสี่เหลี่ยมจัตุรัสหรือไม่ ---
    if not rows:
        print("Fail")
        return

    height = len(rows)          # ความสูง (จำนวนบรรทัด)
    width = len(rows[0])        # ความกว้าง (ของบรรทัดแรก)

    # กฎข้อ 1: ความกว้างต้องเท่ากับความสูง (Square)
    if width != height:
        print("Fail")
        return

    # กฎข้อ 2: ทุกบรรทัดต้องยาวเท่ากัน
    for row in rows:
        if len(row) != width:
            print("Fail")
            return
    # ------------------------------------------------

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

            # เช็คขอบเขต (ใช้ width และ height ที่หาไว้แล้วได้เลย)
            if not (0 <= nr < height and 0 <= nc < width):
                break

            piece = rows[nr][nc]

            if piece == '.':
                dist += 1
                continue

            # --- เช็คศัตรู ---
            
            # Rook (R) - แนวตรง
            if piece == 'R' and (dr == 0 or dc == 0):
                print("Success")
                return

            # Bishop (B) - แนวทแยง
            if piece == 'B' and (dr != 0 and dc != 0):
                print("Success")
                return

            # Queen (Q) - ทุกทิศ
            if piece == 'Q':
                print("Success")
                return

            # Pawn (P)
            # เงื่อนไข: ทแยง (dr, dc ไม่ใช่ 0), ระยะ 1 ช่อง (dist == 1), 
            # และต้องอยู่ "ล่าง" King (dr == 1) เพราะ Pawn ตีขึ้นบน
            if piece == 'P' and dist == 1 and dr == 1 and (dc == -1 or dc == 1):
                print("Success")
                return

            # ถ้าเจอตัวอะไรก็ตามที่ไม่ใช่เงื่อนไขข้างบน แสดงว่าทางตัน (โดนบล็อก)
            break 

    # ถ้าวนครบทุกทิศแล้วไม่เจออะไรเลย
    print("Fail")