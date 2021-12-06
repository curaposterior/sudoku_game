#converting main.py to object oriented program

class Sudoku:
    def __init__(self, grid):
        '''zainicjowanie argumentow'''
        self.grid = grid
    
    def print_grid(self, grid):
        for i in range(len(grid)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(grid[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(grid[i][j])
                else:
                    print(str(grid[i][j]) + " ", end="")
    
    def findEmptyCell(self, i=0, j=0):
        '''Znajduje nastepna wolna komórke'''
        for num in range(81):
            row = num // 9
            col = num % 9
            print(row,col)
            if self.grid[row][col] == 0:
                return row,col
        return True

    def checkRowColumnSquare(grid, row, col, num):
        '''Sprawdza czy liczba znajduje sie w rzedzie,
        kolumnie i kwadracie. Jesli nie to zwracana 
        jest prawda'''
        #funkcja na razie nie dziala
        for i in range(9):
            if grid[row][i] == num:
                return False
            if grid[i][col] == num:
                return False
        
        sRow = row - row % 3
        sCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + sRow][j + sCol] == num:
                    return False
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
    
