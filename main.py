#/usr/bin/python3

def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()

def findEmptyCell(grid, i=0,j=0):
    for num in range(81):
        row = num // 9
        col = num % 9
        print(row,col)
        if grid[row][col] == 0:
            return row,col
    return True

def checkElem(grid, x, y):
    elem = grid[x][y]
    if i < 3 and j < 3:
        #check all posiblities
        pass

def solveSudoku(grid):
    if findEmptyCell(grid):
        return True
    else:
        i, j = findEmptyCell(grid)
        for elem in range(1,10):
            print('test')

test_grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
            [0, 1, 0, 0, 0, 4, 0, 0, 0],
            [4, 0, 7, 0, 0, 0, 2, 0, 8],
            [0, 0, 5, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 9, 8, 1, 0, 0],
            [0, 4, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 3, 6, 0, 0, 7, 2],
            [0, 7, 0, 0, 0, 0, 0, 0, 3],
            [9, 0, 3, 0, 0, 0, 6, 0, 4]]    

