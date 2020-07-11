#Rook Piece class
from Piece import Pieces

class Rook(Pieces):
    #arg[0] = x_coord
    #arg[1] = y_coord
    #arg[2] = isWhite
    def __init__(self, *args):
        super().__init__(args[0], args[1])
        self.isWhite = args[2]
        #used for King castling
        self.canCastle = True

    def __eq__(self, other):
        return 'R' == other

    def __str__(self):
        return "R"

    #return True or False
    def validMoves(self, board, new_x, new_y):
        #are the new moves in the board?
        if new_x > 7 or new_x < 0 or new_y > 7 or new_y < 0:
            return False
        #check if piece can move to i
        #movement in x, y must be constant
        if new_x - self.x != 0 and new_y - self.y == 0:
            self_check = True
            for space in range(self.x, new_x):
                #don't check self for empty
                if self_check == True:
                    self_check = False
                    continue
                #board is empty till newspace
                if board[space][self.y] != " ":
                    return False
        #movement in y, x must be constant
        elif new_x - self.x == 0 and new_y - self.y != 0:
            self_check = True
            for space in range(self.y, new_y):
                #don't check self for empty
                if self_check == True:
                    self_check = False
                    continue
                #board is empty till newspace
                if board[self.x][space] != " ":
                    return False
        else:
            #can't move to the spot
            return False
        #check if new move is empty.
        if board[new_x][new_y] == " ":
            self.canCastle = False
            return True
        #new move is a piece/capture
        #this piece is white
        if self.isWhite:
            #new move is same color
            if board[new_x][new_y].isWhite == True:
                return False
            #new move is different color
            self.canCastle = False
            return True
        #piece is black
        else:
            #new move is same color
            if board[new_x][new_y].isWhite == False:
                return False
            #new move is different color
            self.canCastle = False
            return True
