"""
    Andrew Goodman
    March 30, 2016
    
    Sudoku game that features rules-based programming
"""
from Sudoku import Sudoku

s = Sudoku()

def setupGame():
    """Prepare game"""
    s.generateGame(10)

def gameController():
    """Control the logic in the game"""
    #s.printBoard()
    s.display(width,height)

def setup():
    size(500,500)
    #background(255,255,255)
    background(150)
    setupGame()
    s.printBoard()
        
def draw():
    gameController()