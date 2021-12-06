##
# 최초 1회로 헥사도쿠 (16*16) 테이블을 만들어준다.
##

from hexadoku import CreateTable
import hashlib
import numpy as np

M = 16


def puzzle(a):
    doku = []

    for i in range(M):
        row = []
        for j in range(M):
            row.append(hex(a[i][j]))
        doku.append(row)

    return doku


# 2차원 -> 1차원
def solve(grid, row, col, num):
    for x in range(16):
        if grid[row][x] == num:
            return False

    for x in range(16):
        if grid[x][col] == num:
            return False

    startRow = row - row % 4
    startCol = col - col % 4
    for i in range(4):
        for j in range(4):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def hexadoku(grid, row, col):  # 만든거 채움
    if row == M - 1 and col == M:
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > -1:
        return hexadoku(grid, row, col + 1)
    for num in range(0, M, 1):

        if solve(grid, row, col, num):

            grid[row][col] = num
            if hexadoku(grid, row, col + 1):
                return True
        grid[row][col] = -1
    return False
