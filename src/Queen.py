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
            #positive x direction
            if self.x > new_x:
                for space in range(1, new_x-self.x):
                    #don't check self for empty
                    #board is empty till newspace
                    if board[self.x+space][self.y] != " ":
                        return False
            else:
                #negative x direction
                for space in range(1, self.x - new_x):
                    #don't check self for empty
                    #board is empty till newspace
                    if board[self.x-space][self.y] != " ":
                        return False
        #Queen moves in a straight line of y coord
        elif new_x - self.x == 0 and new_y - self.y != 0:
            if self.y > new_y:
                for space in range(1, new_y - self.y):
                    #don't check self for empty
                    #board is empty till newspace
                    if board[self.x][self.y+space] != " ":
                        return False
            else:
                # negative y direction
                for space in range(1, self.y - new_y):
                    #don't check self for empty
                    #board is empty till newspace
                    if board[self.x][self.y-space] != " ":
                        return False
        #Queen moves in a bishop like manner
        elif abs(new_x - self.x) == abs(new_y - self.y) and new_y - self.y != 0:
            #check if positive or negative
            #positive x direction
            if new_x > self.x:
                # positive y direction
                if new_y > self.y:
                    for space in range(1, new_x - self.x):
                        #don't check self for empty
                        #board is empty till newspace
                        print("x space :", str(self.x+space), "y space: ", str(self.y+space))
                        if board[self.x+space][self.y+space] != " ":
                            print("Queen obstacle: 1")
                            return False
                #negative y direction
                else:
                    for space in range(1, new_x - self_x):
                        #don't check self for empty
                        #board is empty till newspace
                        print("x space :", str(self.x+space), "y space: ", str(self.y-space))
                        if board[self.x - space][self.y - space] != " ":
                            print("Queen obstacle:2")
                            return False
            else:
                #negative y direction
                if new_x > self.x:
                    # positive y direction
                    if new_y > self.y:
                        for space in range(1, self.x - new_x):
                            #don't check self for empty
                            #board is empty till newspace
                            print("x space :", str(self.x-space), "y space: ", str(self.y+space))
                            if board[self.x - space][self.y+space] != " ":
                                print("Queen obstacle:3")
                                return False
                    #negative y direction
                    else:
                        for space in range(1, self.x - new_x):
                            #don't check self for empty
                            #board is empty till newspace
                            print("x space :", str(self.x-space), "y space: ", str(self.y-space))
                            if board[self.x - space][self.y - space] != " ":
                                print("Queen obstacle:4")
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
