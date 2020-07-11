#Bishop Piece class
from Piece import Pieces

class Bishop(Pieces):
    #arg[0] = x_coord
    #arg[1] = y_coord
    #arg[2] = isWhite
    def __init__(self, *args):
        super().__init__(args[0],args[1])
        self.isWhite = args[2]

    def __eq__(self, other):
        return 'B' == other

    def __str__(self):
        return "B"

    def validMoves(self, board, new_x, new_y):
        #are the new moves in the board?
        if new_x > 7 or new_x < 0 or new_y > 7 or new_y < 0:
            return False
        #check if piece can move to i
        #movement in x and y must be equal
        if new_x - self.x == new_y - self.y:
            self_check = True
            for space in range(self.x, new_x):
                #don't check self for empty
                if self_check == True:
                    self_check = False
                    continue
                #board is empty till newspace
                print("x space :", space, "y space: ", str(self.y+space-self.x))
                if board[space][self.y+space-self.x] != " ":
                    print("bishop obstacle")
                    return False
        else:
            #can't move to the spot
            return False
        #check if new move is empty spot to move to.
        if board[new_x][new_y] == " ":
            return True
        #new move is a piece/capture
        #this piece is white
        if self.isWhite:
            #new move is same color
            if board[new_x][new_y].isWhite == True:
                print("bishop same move 1")
                return False
            #new move is different color
            print("bishop capture 1")
            return True
        #piece is black
        else:
            #new move is same color
            if board[new_x][new_y].isWhite == False:
                print("bishop same move 1")
                return False
            #new move is different color
            print("bishop capture 2")
            return True
