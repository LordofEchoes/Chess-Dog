#Knight Piece class
from Piece import Pieces

class Knight(Pieces):
    #arg[0] = x_coord
    #arg[1] = y_coord
    #arg[2] = isWhite
    def __init__(self, *args):
        super().__init__(args[0],args[1])
        self.isWhite = args[2]

    def __eq__(self, other):
        return 'N' == other

    def __str__(self):
        return "N"

    def validMoves(self, board, new_x, new_y):
        #are the new moves in the board?
        if new_x > 7 or new_x < 0 or new_y > 7 or new_y < 0:
            return False
        #check if new move is valid:
        if (abs(new_x - self.x) == 2 and abs(new_y - self.y) == 1) or (abs(new_x - self.x) == 1 and abs(new_y-self.y) == 2):
            #new move is valid, is the new move empty?
            if board.board[new_x][new_y] == " ":
                return True
            #new move is occupied
            #this piece is white
            if self.isWhite:
                #new move is same color
                if board.board[new_x][new_y].isWhite == True:
                    return False
                #new move is different color
                return True
            #piece is black
            else:
                #new move is same color
                if board.board[new_x][new_y].isWhite == False:
                    return False
                #new move is different color
                return True
