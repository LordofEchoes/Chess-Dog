# class Pawn, inherits from Pieces
from Piece import Pieces

class Pawn(Pieces):
    #arg[0] = x_coord
    #arg[1] = y_coord
    #arg[2] = isWhite
    def __init__(self, *args):
        super().__init__(args[0],args[1])
        self.isWhite = args[2]
        self.uptwo = True
        self.enpassant = False

    def __eq__(self, other):
        return 'P' == other

    def __str__(self):
        return "P"

    def validMoves(self, board, new_x, new_y):
        # are new coords inside the board?
        if new_x > 7 or new_x < 0 or new_y > 7 or new_y < 0:
            return False
        #is self white?
        if self.isWhite == True:
            #try capturing techniques
            #try enpassant capture:
            if (new_x == self.x+1) and new_y == self.y + 1:
                #try capture right
                if self.x+1 <= 7 and board[self.x+1][self.y] == 'P' and board[self.x+1][self.y].enpassant == True:
                    return True
            elif (new_x == self.x-1) and new_y == self.y + 1:
                #try capture left
                if self.x+1 >= 0 and board[self.x-1][self.y] == 'P' and board[self.x-1][self.y].enpassant == True:
                    return True
            #check normal capture
            if board[new_x][new_y] != ' ':
                #new square is black
                if board[new_x][new_y].isWhite == False:
                    #pawn capturing left and right
                    if (new_x ==  self.x+1 or new_x  == self.x-1) and new_y == self.y + 1:
                        return True
                #new square is white
                else:
                    return False
            #check if new board spot is empty
            if board[new_x][new_y] == " ":
            #check if new move is pure movement
                #check if move is uptwo
                if self.y + 2 == new_y:
                    if self.uptwo == True:
                        if board[self.x][self.y+1] != " ":
                            return False
                        self.uptwo = False
                        self.enpassant = True
                        return True
                    else:
                        return False
                #move is up one
                elif self.y+1 == new_y:
                    self.uptwo = False
                    return True
        # self is black, same code as before up upside down
        else:
            #try capturing techniques
            #try enpassant capture:
            if (new_x == self.x+1) and new_y == self.y - 1:
                #try capture right
                if self.x+1 <= 7 and board[self.x+1][self.y] == 'P' and board[self.x+1][self.y].enpassant == True:
                    return True
            elif (new_x == self.x-1) and new_y == self.y + 1:
                #try capture left
                if self.x+1 >= 0 and board[self.x-1][self.y] == 'P' and board[self.x-1][self.y].enpassant == True:
                    return True
            #check normal capture
            if board[new_x][new_y] != ' ':
                #new square is black
                if board[new_x][new_y].isWhite == False:
                    #pawn capturing left and right
                    if (new_x ==  self.x+1 or new_x  == self.x-1) and new_y == self.y - 1:
                        return True
                #new square is white
                else:
                    return False
            #check if new board spot is empty
            if board[new_x][new_y] == " ":
            #check if new move is pure movement
                #check if move is uptwo
                if self.y - 2 == new_y:
                    if self.uptwo == True:
                        if board[self.x][self.y-1] != " ":
                            return False
                        self.uptwo = False
                        self.enpassant = True
                        return True
                    else:
                        return False
                #move is up one
                elif self.y - 1 == new_y:
                    self.uptwo = False
                    return True
