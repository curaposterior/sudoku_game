#/usr/bin/python3

def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
def generuj_sudoku():
    pass

test_grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
            [0, 1, 0, 0, 0, 4, 0, 0, 0],
            [4, 0, 7, 0, 0, 0, 2, 0, 8],
            [0, 0, 5, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 9, 8, 1, 0, 0],
            [0, 4, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 3, 6, 0, 0, 7, 2],
            [0, 7, 0, 0, 0, 0, 0, 0, 3],
            [9, 0, 3, 0, 0, 0, 6, 0, 4]]
class Sudoku():
    def __init__(self, grid):
        self.grid = grid

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

    def checkColumnAndRow(grid, elem, row, col):
        for i in range(9):
            if grid[i][col] == elem or grid[row][i] == elem:
                return False
        return True

    def checkSquare(grid, elem, row, col):
        '''
        test_grid:
        [2, 5, 0, 0, 3, 0, 9, 0, 1]
        [0, 1, 0, 0, 0, 4, 0, 0, 0]
        [4, 0, 7, 0, 0, 0, 2, 0, 8]
        [0, 0, 5, 2, 0, 0, 0, 0, 0]
        [0, 0, 0, 0, 9, 8, 1, 0, 0]
        [0, 4, 0, 0, 0, 3, 0, 0, 0]
        [0, 0, 0, 3, 6, 0, 0, 7, 2]
        [0, 7, 0, 0, 0, 0, 0, 0, 3]
        [9, 0, 3, 0, 0, 0, 6, 0, 4]
        2 5 0   0 3 0   9 0 1
        0 1 0   0 0 4   0 0 0
        4 0 7   0 0 0   2 0 8


        indeksy:
        00 01 02
        10 11 12
        20 21 22
        '''
        
        for i in range(3):
            square1 = grid[i][:3]
            if elem in square1:
                return False
        return True

    # def checkElem(grid, x, y):
    #     elem = grid[x][y]
    #     if x < 3 and y < 3:
    #         #check all posiblities
    #         pass
    # def generuj_sudoku():
    #     pass

    def solveSudoku(self, grid):
        if findEmptyCell(grid):
            return True
        else:
            i, j = findEmptyCell(grid)
            for elem in range(1,10):
                print('test')
        


if __name__ == '__main__':
    test_grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
                [0, 1, 0, 0, 0, 4, 0, 0, 0],
                [4, 0, 7, 0, 0, 0, 2, 0, 8],
                [0, 0, 5, 2, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 9, 8, 1, 0, 0],
                [0, 4, 0, 0, 0, 3, 0, 0, 0],
                [0, 0, 0, 3, 6, 0, 0, 7, 2],
                [0, 7, 0, 0, 0, 0, 0, 0, 3],
                [9, 0, 3, 0, 0, 0, 6, 0, 4]]
    elem = 4
    #print(checkColumn(test_grid, 4, 0, 2))
    print(Sudoku.checkSquare(test_grid, 5, 0, 2))