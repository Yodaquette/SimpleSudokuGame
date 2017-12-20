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
    
    ##################################
    # Generate the game board
    #
    # @param: difficultySetting
    # - difficultySetting is an integer value of the number of cells
    # that will appear on the game board
    ##################################
    def generateBoard(self,difficultySetting):
        from random import randint,sample
        self.board = [sample(range(1,self.gridSize + 1),self.gridSize) for i in range(self.gridSize)]
        while(difficultySetting > 0):
            y,x = randint(0,self.gridSize - 1),randint(0,self.gridSize - 1)
            if(self.board[y][x] != 0):
                self.board[y][x] = 0
                difficultySetting -= 1

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
    
    #########################################
    # Display the game board
    #
    #########################################
    def display(self,w,h):
        # Set X and Y position variables to 1% of the screen resolution pixels
        xpos,ypos = w*0.1,h*0.1
        # Set X and Y size variables to 1% of the screen resolution pixels
        xWidth,yHeight = w*0.1,h*0.1
        
        # Make text size fit inside rectangles
        textSize(xpos - 5)
        textAlign(CENTER,CENTER)
        rectMode(CENTER)
        
        # For each cell within each row, generate a new rectangle
        for row in self.board:
            for cell in row:
                fill(255)
                rect(xpos,ypos,xWidth,yHeight)
                
                #if(abs(mouseX - xpos) < )
                
                # Leave out the values of 0 
                if(cell > 0):
                    fill(0)
                    text(str(cell),xpos,ypos)
                    
                xpos += w*0.1
            # Reset xpos
            xpos = w*0.1
            # Increase ypos
            ypos += h*0.1
    
    # For testing - print the game board to the console
    def printBoard(self):
        print("Board Generated: " + str(self.board))