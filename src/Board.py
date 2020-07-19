# Board Class
from Pawn import Pawn
from Knight import Knight
from Rook import Rook
from Bishop import Bishop
from King import King
from Queen import Queen

class ChessBoard:

    def __init__(self):
        self.board = [[" " for y in range(0,8)] for x in range(0,8)]
        self.white = list()
        self.black = list()
        self.graveyard = list()
        self.move = 0
        self.enpassant = False
        self.EPlocation = tuple()

    def __eq__(self, other):
        return self.board == other.board

    def __str__(self):
        #print the board
        string = "Chess Board:\n  a|b|c|d|e|f|g|h|\n"
        string += "  - - - - - - - - \n"
        for y in range(7,-1,-1):
            string += str(y+1) + "|"
            for x in range(0,8):
                string += str(self.board[x][y]) + "|"
            string += "\n  - - - - - - - -\n"
        return string

    def setUpBoard(self):
        #set up white
        self.white = [
        Pawn(0,1,True),
        Pawn(1,1,True),
        Pawn(2,1,True),
        Pawn(3,1,True),
        Pawn(4,1,True),
        Pawn(5,1,True),
        Pawn(6,1,True),
        Pawn(7,1,True),
        Knight(1,0,True),
        Knight(6,0,True),
        Bishop(2,0,True),
        Bishop(5,0,True),
        Rook(0,0,True),
        Rook(7,0,True),
        King(4,0,True),
        Queen(3,0,True)]

        #set up Black
        self.black = [
        Pawn(0,6,False),
        Pawn(1,6,False),
        Pawn(2,6,False),
        Pawn(3,6,False),
        Pawn(4,6,False),
        Pawn(5,6,False),
        Pawn(6,6,False),
        Pawn(7,6,False),
        Knight(1,7,False),
        Knight(6,7,False),
        Bishop(2,7,False),
        Bishop(5,7,False),
        Rook(0,7,False),
        Rook(7,7,False),
        King(4,7,False),
        Queen(3,7,False)]

        #set up board
        for obj in self.white:
            # print(obj.x, obj.y)
            self.board[obj.x][obj.y] = obj
        for obj in self.black:
            self.board[obj.x][obj.y] = obj

    #check if any Kings are in mate
    #True if in check
    def checkKing(self, isWhite):
        if isWhite:
            for obj in self.white:
                #found the King
                if obj == "K":
                    #can any piece kill the King?
                    for enemy in self.black:
                        # print("enemy", enemy, " x:", enemy.x, " y:", enemy.y)
                        if enemy != "K" and enemy.validMoves(self, obj.x, obj.y):
                            return True
                    return False
        #is Black
        else:
            for obj in self.black:
                #found the King
                if obj == "K":
                    #can another piece kill the King
                    for enemy in self.white:
                        # print("enemy", enemy, " x:", enemy.x, " y:", enemy.y)
                        if enemy != "K" and enemy.validMoves(self, obj.x, obj.y):
                            return True
                    return False

    def movePiece(self, board, start_x, start_y, new_x, new_y):
        # print("pre obj:", board[start_x][start_y])
        # print("pre nothing:", board[new_x][new_y])
        board[start_x][start_y].x = new_x
        board[start_x][start_y].y = new_y

        board[new_x][new_y] = board[start_x][start_y]
        board[start_x][start_y] = " "
        # print("post obj:", board[new_x][new_y])
        # print("post obj y:", board[new_x][new_y].x, "post obj y:", board[new_x][new_y].y)
        # print("post nothing:", board[start_x][start_y])

    def performMoveWhite(self, start_x, start_y, new_x, new_y):
        temp = self.board
        tempblack = self.black
        tempyard =  self.graveyard
        #are they moving a piece
        if self.board[start_x][start_y] == " ":
            print("not a piece: 1")
            return False
        #are they moving a white piece
        if self.board[start_x][start_y].isWhite == True:
            #is the move a castling move
            if self.board[start_x][start_y] == "K" and self.checkKing(True):
                castle = False
                if self.board[start_x][start_y].validMoves(self, new_x, new_y, castle) == True:
                    if castle == True:
                        print("attempt castle: 1")
                        #White King is attempting to castle Queenside
                        if new_x == 2 and new_y == 0:
                            print("attempt castle Queen: 1")
                            #move King
                            self.movePiece(4,0,3,0)
                            if self.checkKing(True):
                                self.board = temp
                                return False
                            self.movePiece(4,0,2,0)
                            #move Rook
                            self.movePiece(7,0,3,0)
                            if self.checkKing(True):
                                self.board = temp
                                return False
                        #White King is attempting to castle Kingside
                        elif new_x == 6 and new_y == 0:
                            print("attempt castle King: 1")
                            #move King
                            self.movePiece(4,0,5,0)
                            if self.checkKing(True):
                                self.board = temp
                                return False
                            self.movePiece(4,0,6,0)
                            #move Rook
                            self.movePiece(0,0,5,0)
                            if self.checkKing(True):
                                self.board = temp
                                return False
            #not castling move
            if self.board[start_x][start_y].validMoves(self, new_x, new_y) == True:
                if self.board[new_x][new_y] != " ":
                    print("capture move: 1")
                    #capturing, remove graveyard and pieces accordingly
                    self.graveyard.append(self.board[new_x][new_y])
                    self.white.remove(self.board[new_x][new_y])
                    #implement move
                    self.movePiece(self.board,start_x,start_y,new_x,new_y)
                else:
                    #only time that capturing piece doesn't move to capture square is enpassant
                    print(self.board[start_x][start_y] == "P", self.EPlocation == (new_x,new_y-1))
                    if self.board[start_x][start_y] == "P" and self.EPlocation == (new_x,new_y-1):
                        print("enpassant capture: 1")
                        self.graveyard.append(self.board[new_x][new_y-1])
                        self.white.remove(self.board[new_x][new_y-1])
                        self.board[new_x][new_y-1] = " "
                    else:
                        print("standard move: 1")
                    self.movePiece(self.board,start_x,start_y,new_x,new_y)
            else:
                print("not a valid move: 1")
                return False
        if self.checkKing(True):
            print("king in check: 1")
            self.board = temp
            self.black = tempblack
            self.graveyard = tempyard
            self.movePiece(self.board,new_x,new_y,start_x,start_y)
            return False
        else:
            #if the newly moved piece isn't a pawn then enpassant is false
            if self.board[new_x][new_y] != "P" and abs(new_y-start_y) != 2:
                print("enpassant reset: 1")
                self.enpassant = False
                self.EPlocation = ()
            return True

    # performs moves but as black
    def performMoveBlack(self, start_x, start_y, new_x, new_y):
        temp = self.board
        tempwhite = self.white
        tempyard =  self.graveyard
        #are they moving a piece
        if self.board[start_x][start_y] == " ":
            print("not a piece: 2")
            return False
        #are they moving a black piece
        if self.board[start_x][start_y].isWhite == False:
            #is the move a castling move
            if self.board[start_x][start_y] == "K"and self.checkKing(False):
                castle = False
                if self.board[start_x][start_y].validMoves(self, new_x, new_y, castle) == True:
                    if castle == True:
                        print("attempt castle Queen: 2")
                        #Black King is attempting to castle Queenside
                        if new_x == 2 and new_y == 7:
                            #move King
                            self.movePiece(4,7,3,7)
                            if self.checkKing(False):
                                self.board = temp
                                return False
                            self.movePiece(4,7,2,7)
                            # move Rook
                            self.movePiece(0,7,3,7)
                            if self.checkKing(False):
                                self.board = temp
                                return False
                        #White King is attempting to castle Kingside
                        elif new_x == 6 and new_y == 7:
                            print("attempt castle King: 2")
                            # move King
                            self.movePiece(4,7,5,7)
                            if self.checkKing(False):
                                self.board = temp
                                return False
                            self.movePiece(4,7,6,7)
                            # move Rook
                            self.movePiece(0,7,5,7)
                            if self.checkKing(False):
                                self.board = temp
                                return False
            #not castling move
            if self.board[start_x][start_y].validMoves(self, new_x, new_y) == True:
                if self.board[new_x][new_y] != " ":
                    print("capture move: 2")
                    #capturing, remove graveyard and pieces accordingly
                    self.graveyard.append(self.board[new_x][new_y])
                    self.white.remove(self.board[new_x][new_y])
                    #implement move
                    self.movePiece(self.board,start_x,start_y,new_x,new_y)
                else:
                    #only time that capturing piece doesn't move to capture square is enpassant
                    if self.board[start_x][start_y] == "P" and self.EPlocation == (new_x,new_y+1):
                        print("enpassant capture: 2")
                        self.graveyard.append(self.board[new_x][new_y+1])
                        self.white.remove(self.board[new_x][new_y+1])
                        self.board[new_x][new_y+1] = " "
                    else:
                        print("standard move: 2")
                    self.movePiece(self.board,start_x,start_y,new_x,new_y)
            else:
                print("not a valid move: 2")
                return False
        if self.checkKing(False):
            print("king in check: 2")
            self.board = temp
            self.white = tempwhite
            self.graveyard = tempyard
            self.movePiece(self.board,new_x,new_y,start_x,start_y)
            return False
        else:
            #if the newly moved piece isn't a pawn then enpassant is false
            if self.board[new_x][new_y] != "P" and self.EPlocation != (new_x,new_y) and abs(new_y-start_y) != 2:
                print("enpassant reset: 2")
                self.enpassant = False
                self.EPlocation = ()
            return True
