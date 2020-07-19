#automatic tester file

from Board import ChessBoard

Chess = ChessBoard()
Chess.setUpBoard()
print(Chess)
#start of movement/move 1
#e4
Chess.performMoveWhite(4,1,4,3)
print(Chess)
#d5
Chess.performMoveBlack(3,6,3,4)
print(Chess)
#e4xd5
Chess.performMoveWhite(4,3,3,4)
print(Chess)
#e5
Chess.performMoveBlack(4,6,4,4)
print(Chess)
#d5xe5
Chess.performMoveWhite(3,4,4,5)
print(Chess)
#Qe7
Chess.performMoveBlack(3,7,4,6)
print(Chess)
#Nf3
Chess.performMoveWhite(6,0,5,2)
print(Chess)
