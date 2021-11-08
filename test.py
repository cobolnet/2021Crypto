from hexadoku import createTable

M = 16
def puzzle(a):
    doku = []
    for i in range(M):
        row = []
        for j in range(M):      
            row.append(hex(a[i][j]))
        doku.append(row)
    return doku

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
 
def hexadoku(grid, row, col):
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > -1:
        return hexadoku(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if hexadoku(grid, row, col + 1):
                return True
        grid[row][col] = -1
    return False
 
'''-1 means the cells where no value is assigned'''
grid = createTable()
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

if (hexadoku(grid, 0, 0)):
    print(puzzle(grid))
else:
    print("Solution does not exist:(")