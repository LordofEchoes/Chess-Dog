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

    def __eq__(self, other):
        return 'P' == other

    def __str__(self):
        return "P"

    def validMoves(self, board, new_x, new_y):
        # are new coords inside the board?
        if new_x > 7 or new_x < 0 or new_y > 7 or new_y < 0:
            return False
        # color is white
        color = 1
        if self.isWhite != True:
            # color is black, multiplier negative
            color = -1
        #try capturing techniques
        #try enpassant capture:
        if (new_x == self.x+1) and new_y == self.y+color:
            #try capture right
            if self.x+1 <= 7 and board.enpassant == True and board.EPlocation == (new_x,new_y-color):
                print("Pawn enpassant: 1")
                return True
        elif (new_x == self.x-1) and new_y == self.y+color:
            #try capture left
            if self.x-1 >= 0  and board.enpassant == True and board.EPlocation == (new_x,new_y-color):
                print("Pawn enpassant: 2")
                return True
        #check normal capture
        if board.board[new_x][new_y] != ' ':
            #new square is black
            if board.board[new_x][new_y].isWhite == False:
                #pawn capturing left and right
                if (new_x ==  self.x+1 or new_x  == self.x-1) and new_y == self.y+color:
                    print("Pawn capture: 1")
                    return True
            #new square is white
            else:
                return False
        #check if new board spot is empty
        if board.board[new_x][new_y] == " ":
        #check if new move is pure movement
            #check if move is uptwo
            if self.y+color*2 == new_y:
                if self.uptwo == True:
                    if board.board[self.x][self.y+color] != " ":
                        return False
                    self.uptwo = False
                    #uptwo is utilized
                    #board updates enpassant
                    board.enpassant = True
                    board.EPlocation = (new_x,new_y)
                    print("Pawn uptwo: 1")
                    return True
                else:
                    return False
            #move is up one
        elif self.y+color == new_y:
                self.uptwo = False
                return True
