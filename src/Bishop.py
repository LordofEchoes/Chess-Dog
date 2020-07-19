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
        #movement in x and y must be equal
        if abs(new_x - self.x) == abs(new_y - self.y) and new_y - self.y != 0:
            # check if positive or negative
            #positive x direction
            if new_x > self.x:
                # positive y direction
                if new_y > self.y:
                    for space in range(1, new_x - self.x):
                        #don't check self for empty
                        #board is empty till newspace
                        # print("x space :", str(self.x+space), "y space: ", str(self.y+space))
                        if board.board[self.x+space][self.y+space] != " ":
                            # print("bishop obstacle: 1")
                            return False
                #negative y direction
                else:
                    for space in range(1, new_x - self_x):
                        #don't check self for empty
                        #board is empty till newspace
                        # print("x space :", str(self.x+space), "y space: ", str(self.y-space))
                        if board.board[self.x-space][self.y-space] != " ":
                            # print("bishop obstacle:2")
                            return False
            #negative y direction
            else:
                if new_x > self.x:
                    # positive x direction
                    if new_y > self.y:
                        for space in range(1, self.x - new_x):
                            #don't check self for empty
                            #board is empty till newspace
                            # print("x space :", str(self.x-space), "y space: ", str(self.y+space))
                            if board.board[self.x-space][self.y+space] != " ":
                                # print("bishop obstacle:3")
                                return False
                    #negative x direction
                    else:
                        for space in range(1, self.x - new_x):
                            #don't check self for empty
                            #board is empty till newspace
                            # print("x space :", str(self.x-space), "y space: ", str(self.y-space))
                            if board.board[self.x-space][self.y-space] != " ":
                                # print("bishop obstacle:4")
                                return False
        else:
            #can't move to the spot
            return False
        #check if new move is empty spot to move to.
        if board.board[new_x][new_y] == " ":
            return True
        #new move is a piece/capture
        #this piece is white
        if self.isWhite:
            #new move is same color
            if board.board[new_x][new_y].isWhite == True:
                print("bishop same move 1")
                return False
            #new move is different color
            print("bishop capture 1")
            return True
        #piece is black
        else:
            #new move is same color
            if board.board[new_x][new_y].isWhite == False:
                print("bishop same move 1")
                return False
            #new move is different color
            print("bishop capture 2")
            return True
