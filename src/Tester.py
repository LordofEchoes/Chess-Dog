#automatic tester file

from Board import ChessBoard

Chess = ChessBoard()
Chess.setUpBoard()
print(Chess)
#start of movement/move 1
#e4
Chess.performMoveWhite(4,1,4,3,True)
print(Chess)
#d5
Chess.performMoveBlack(3,6,3,4,False)
print(Chess)
#e4xd5
Chess.performMoveWhite(4,3,3,4,True)
print(Chess)
#e5
Chess.performMoveBlack(4,6,4,4,False)
print(Chess)
#d5xe5 - enpassant
Chess.performMoveWhite(3,4,4,3,True)
print(Chess)
