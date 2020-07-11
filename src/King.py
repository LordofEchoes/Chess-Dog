#King Piece class
from Piece import Pieces

class King(Pieces):
    #arg[0] = x_coord
    #arg[1] = y_coord
    #arg[2] = isWhite
    def __init__(self, *args):
        super().__init__(args[0],args[1])
        self.isWhite = args[2]
        self.canCastle = True

    def __eq__(self, other):
        return 'K' == other

    def __str__(self):
        return "K"

    def validMoves(self, board, new_x, new_y, isCastle):
        isCastle = False
        #are the new moves in the board?
        if new_x > 7 or new_x < 0 or new_y > 7 or new_y < 0:
            return False
        #is the new move a castling move?
        if self.canCastle:
            #are all the blocks out of the way to castle?
            self_check = True
            for space in range(self.x, new_x):
                #don't check self for empty
                if self_check == True:
                    self_check = False
                    continue
                #board is empty till newspace
                if board[space][self.y] != " ":
                    return False
            if self.isWhite:
                #King is attempting to castle Queenside
                if new_x == 2 and new_y == 0:
                    if board[0][0] == "R" and board[0][0].canCastle:
                        #The King can castle
                        isCastle = True
                        return True
                #King is attempting to castle Kingside
                if new_x == 6 and new_y == 0:
                    if board[7][0] == "R" and board[7][0].canCastle:
                        #The King can castle
                        isCastle = True
                        return True
            else:
                #King is attempting to castle Queenside
                if new_x == 2 and new_y == 7:
                    if board[0][7] == "R" and board[0][7].canCastle:
                        #The King can castle
                        isCastle = True
                        return True
                #King is attempting to castle Kingside
                if new_x == 6 and new_y == 7:
                    if board[7][7] == "R" and board[7][7].canCastle:
                        #The King can castle
                        isCastle = True
                        return True

        #are all the moves one away?
        if (new_x-self.x != 1 and new_x-self.x != 1) or (new_y-self.y != 1 and new_y-self.y != -1):
            return False
        #moves are one away, is the move empty?
        if board[new_x][new_y] == " ":
            self.canCastle = False
            return True
        #the new space is not empty
        #what color are you?
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
