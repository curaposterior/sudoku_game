#converting main.py to object oriented program


class Sudoku:
    def __init__(self, grid):
        self.grid = grid
    
    def print_grid(self):
        for i in range(9):
            for j in range(9):
                print(self.grid[i][j], end=" ")
            print()
    
    def findEmptyCell(self, i=0, j=0):
        for num in range(81):
            row = num // 9
            col = num % 9
            print(row,col)
            if self.grid[row][col] == 0:
                return row,col
        return True

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
    sudoku = Sudoku(test_grid)
    sudoku.print_grid()
