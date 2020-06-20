# Pieces class
class Pieces:
    #args are x_coord, y_coord
    def __init__(self, *args):
        self.x = args[0]
        self.y = args[1]

        def __eq__(self, other):
            return ' ' == other

    def __str__(self):
        return str("Piece")

    def validMoves(self, board, new_x, new_y):
        pass
