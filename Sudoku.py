"""
    Andrew Goodman
    March 30, 2016
    
    Sudoku game that features rules-based programming
"""



class Sudoku():
    def __init__(self,gs = 9,bs = 3):
        """Initialize the Sudoku instance variables"""
        self.gridSize = gs
        self.boardSize = bs
        self.board = []
        # self.board = [None for i in range(9)]
        self.boardCells = []
    
    #########################################
    # Check the game board for the win state
    #
    # @param: grid
    # - grid is the current game board
    #########################################
    def checkBoard(grid):
        numbers = set(range(1, len(grid) + 1))
        if (any(set(row) != numbers for row in grid) or any(set(col) != numbers for col in zip(*grid))):
            return False
        return True
    
    ##################################
    # Generate the game board
    #
    # @param: difficultySetting
    # - difficultySetting is an integer value of the number of cells
    # that will appear on the game board
    ##################################
    def generateGame(self,cellsToBlank):
        from SudokuBoard import SudokuBoard
        sb = SudokuBoard(9*9)
        # from random import randint,sample
        # self.board = [sample(range(1,self.gridSize + 1),self.gridSize) for i in range(self.gridSize)]
        # while(difficultySetting > 0):
        #     y,x = randint(0,self.gridSize - 1),randint(0,self.gridSize - 1)
        #     if(self.board[y][x] != 0):
        #         self.board[y][x] = 0
        #         difficultySetting -= 1
        # self.board = sb.generateBoard(cellsToBlank)
        [self.board.append(i) for i in sb.generateBoard(cellsToBlank) for j in range(9)]
        for i in len(sb.)
        # print(self.board)
    
    #########################################
    # Display the game board
    #
    # @param: w
    # - The width of the game window
    # @param: h
    # - The height of the game window
    #########################################
    def display(self,w,h):
        # Set X and Y position variables to 10% of the screen resolution pixels
        xpos,ypos = w*0.1,h*0.1
        # Set X and Y size variables to 10% of the screen resolution pixels
        xWidth,yHeight = w*0.1,h*0.1
        
        # Make text size fit inside rectangles
        textSize(xpos - 5)
        textAlign(CENTER,CENTER)
        rectMode(CENTER)
        
        # For each cell within each row, generate a new rectangle
        for row in self.board:
            #for cell in row:
            fill(255)
            rect(xpos,ypos,xWidth,yHeight)
            #self.boardCells.append(xpos,ypos,xWidth,yHeight)
            
            # Populate every cell except the cells with value 0 
            if(row > 0):
                fill(0)
                text(str(row),xpos,ypos)
                
        # Darken cell background during mouse hover
        # if(abs(mouseX - xpos) < textWidth(str(cell)) and abs(mouseY - ypos)
        #         < (textAscent() + textDescent())):
        #     fill(225)
                
            xpos += w*0.1
        # Reset xpos
        xpos = w*0.1
        # Increase ypos
        ypos += h*0.1
    
    # For testing - print the game board to the console
    def printBoard(self):
        print("Board Generated: " + str(self.board))
        print("Board Cell Locations: " + str(self.boardCells))