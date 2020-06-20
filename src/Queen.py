#Queen Piece class
from Piece import Pieces

class Queen(Pieces):
    #arg[0] = x_coord
    #arg[1] = y_coord
    #arg[2] = isWhite
    def __init__(self, *args):
        super().__init__(args[0],args[1])
        self.isWhite = args[2]

    def __eq__(self, other):
        return 'Q' == other

    def __str__(self):
        return "Q"

    def validMoves(self, board, new_x, new_y):
        #are the new moves in the board?
        if new_x > 7 or new_x < 0 or new_y > 7 or new_y < 0:
            return False
        #is the movement diagonal or a straight line from the Queen?
        #Queen moves in straight line of x coord
        if (new_x - self.x != 0 and new_y - self.y == 0):
            self_check = True
            for space in range(self.x, new_x):
                #don't check self for empty
                if self_check == True:
                    self_check = False
                    continue
                #board is empty till newspace
                if board[space][self.y+space-self.x] != " ":
                    return False
        #Queen moves in a straight line of y coord
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
        #Queen moves in a bishop like manner
        elif new_x - self.x == new_y - self.y:
            self_check = True
            for space in range(self.x, new_x):
                #don't check self for empty
                if self_check == True:
                    self_check = False
                    continue
                #board is empty till newspace
                if board[space][self.y+space-self.x] != " ":
                    return False
        #path is not a valid move for the Queen
        else:
            return False

        #path is clear for the Queen
        if board[new_x][new_y] == " ":
            return True
        else:
            # Queen is white
            if self.isWhite:
                #new move is same color
                if board[new_x][new_y].isWhite == True:
                    return False
                #new move is different color
                return True
            #Queen is black
            else:
                #new move is same color
                if board[new_x][new_y].isWhite == False:
                    return False
                #new move is different color
                return True
