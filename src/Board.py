# Board Class
from Pawn import Pawn
from Knight import Knight
from Rook import Rook
from Bishop import Bishop
from King import King
from Queen import Queen

class ChessBoard:

    def __init__(self):
        self.board = [[" " for x in range(0,8)] for y in range(0,8)]
        self.white = list()
        self.black = list()

    def __eq__(self, other):
        return self.board == other.board

    def __str__(self):
        #print the board
        string = "Chess Board:\n  a|b|c|d|e|f|g|h| \n"
        string += "  - - - - - - - - \n"
        for x in range(0,8):
            string += str(x + 1) + "|"
            for y in range(0,8):
                string += str(self.board[x][y]) + "|"
            string += "\n  - - - - - - - -\n"

        return string

    def setUpBoard(self):
        #set up white
        self.white = [
        Pawn(1,0,True),
        Pawn(1,1,True),
        Pawn(1,2,True),
        Pawn(1,3,True),
        Pawn(1,4,True),
        Pawn(1,5,True),
        Pawn(1,6,True),
        Pawn(1,7,True),
        Knight(0,1,True),
        Knight(0,6,True),
        Bishop(0,2,True),
        Bishop(0,5,True),
        Rook(0,0,True),
        Rook(0,7,True),
        King(0,3,True),
        Queen(0,4,True)]

        #set up Black
        self.black = [
        Pawn(6,0,False),
        Pawn(6,1,False),
        Pawn(6,2,False),
        Pawn(6,3,False),
        Pawn(6,4,False),
        Pawn(6,5,False),
        Pawn(6,6,False),
        Pawn(6,7,False),
        Knight(7,1,False),
        Knight(7,6,False),
        Bishop(7,2,False),
        Bishop(7,5,False),
        Rook(7,0,False),
        Rook(7,7,False),
        King(7,3,False),
        Queen(7,4,False)]

        #set up board
        for obj in self.white:
            # print(obj.x, obj.y)
            self.board[obj.x][obj.y] = obj
        for obj in self.black:
            self.board[obj.x][obj.y] = obj

    #check if any Kings are in mate
    def checkKing(self):
        pass
