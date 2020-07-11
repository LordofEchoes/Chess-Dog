#automatic tester file

from Board import ChessBoard

Chess = ChessBoard()
Chess.setUpBoard()
print(Chess)

#start of movement/move 1
#e4
Chess.performMoveWhite(4,1,4,3,True)
print(Chess)
#e5
Chess.performMoveBlack(4,6,4,4,False)
print(Chess)
