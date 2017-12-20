"""
    Andrew Goodman
    April 1, 2016

    Generate a randomized, valid Sudoku board
"""
import random


class SudokuBoard:
    def __init__(self,boardLength):
        """Initialize instance variables"""
        self.sudoku = []
        self.sudokuLength = boardLength
    
    #########################################
    # Generate the game board
    #########################################
    def generateBoard(self,difficultySetting):
        for i in range(self.sudokuLength):
            self.sudoku.append(None) # populate board with nulls
        self.populateCell(0)    
        
        while(difficultySetting > 0):
            cell = random.randint(0,self.sudokuLength - 1)
            # print(cell)
            if(self.sudoku[cell] != 0):
                self.sudoku[cell] = 0
                difficultySetting -= 1
        
        # self.printSudoku()
        return self.sudoku
    
    #########################################
    # Populate the board
    # This function executes recursively until
    # all cells on the board are populated
    #
    # @param: grid
    # - 
    #########################################
    def populateCell(self,grid):
        if(grid == self.sudokuLength):
            return True
        oneToNine = [i for i in range(1,10)]
        for i in range(9):
            self.sudoku[grid] = random.choice(oneToNine)
            oneToNine.remove(self.sudoku[grid])
            if(self.gridIsValid(self.sudoku[grid], grid)):
                if(self.populateCell(grid+1)):
                    return True
        self.sudoku[grid] = None
        return False
   
    #########################################
    # Checks that the board is valid
    #
    # @param: grid
    # - 
    #########################################
    def gridIsValid(self,num, grid):
        #print(num)
        if(self.checkVertical(num, grid) and self.checkHorizontal(num, grid) and self.check3x3(num, grid)):
            return True
        else:
            return False
    #########################################
    # Checks for a valid 3x3 square
    #
    # @param: grid
    # - 
    #########################################
    def check3x3(self,num, grid):
        temp = grid
        row = 0
        while temp >= 9:
            temp -= 9
            row += 1
        if(row % 3 == 0):
            return True
        else:
            temp = grid
            offset = grid % 3
            # range(1 or 2)
            for i in range(row % 3):
                temp -= 9
                for j in range(3):
                        if(num == self.sudoku[temp - offset + j]):
                            return False
        return True
    
    #########################################
    # Checks for a valid horizontal line
    #
    # @param: grid
    # - 
    #########################################
    def checkHorizontal(self,num, grid):
        offset = grid % 9
        for i in range(1, offset + 1):
            if(num == self.sudoku[grid - i]):
                return False
        return True
    
    #########################################
    # Checks for a valid vertical line
    #
    # @param: grid
    # - 
    #########################################
    def checkVertical(self,num, grid):
        grid -= 9
        while grid >= 0:
            if(num == self.sudoku[grid]):
                return False
            grid -= 9
        return True
    
    def printSudoku(self):
        """
        Print board
        """
        temp = []
        for i in range(9):
            temp.append([])
        gridCtr = 0
        rowCtr = 0
        while gridCtr < 81:
            for i in range(9):
                temp[rowCtr].append(self.sudoku[gridCtr])
                gridCtr += 1
            rowCtr += 1
        for row in temp:
            print(row)