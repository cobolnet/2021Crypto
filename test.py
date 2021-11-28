#2021 정보보안
#4조
#20163081 정금종

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


    return doku#np.reshape(doku,(16,16))

#2차원 -> 1차원

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
 
def hexadoku(grid, row, col):   #만든거 채움
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > -1:
        return hexadoku(grid, row, col + 1)
    for num in range(0, M , 1):
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if hexadoku(grid, row, col + 1):
                return True
        grid[row][col] = -1
    return False
 
'''-1 means the cells where no value is assigned'''



#grid = CreateTable()    #이것도 에러뜸
#print(grid)
'''
grid = [
    [0,1,2,3,           -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [4,5,6,7,           -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [8,9,0xa,0xb,       -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [0xc,0xd,0xe,0xf,   -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    ]
'''



'''
def CompleteTable(eTable) :
    if (hexadoku(eTable, 0, 0)):  # 헥사도쿠 알고리즘
        puzzle(eTable)  # 완성된 테이블 가져오기 (16진수)
'''


'''
#디버깅 용
if (hexadoku(grid, 0, 0)):  #헥사도쿠 알고리즘
    print(puzzle(grid))     #완성된 테이블 가져오기 (16진수)
else:
    print("Solution does not exist:(")
    
'''
