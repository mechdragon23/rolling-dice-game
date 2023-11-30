from random import randint

board = {}  #initialize the board

#intitalize the board with values, used to reset board
#returns nothing
def init_board(board):
    for key in range(2,13):
        board[key] = True

#checks if the board is empty(all false)
#returns t/f
def check_win(board):
    if True in board.values():
        return False
    else:
        return True
    
#rolls 2 dice
#returns a number between 2 and 12 with a bellcurve distribution
def roll_dice():
    return randint(1,6) + randint(1,6)

#extracts a list of possible moves from the board
#returns a list of valid moves
def possible_moves(board):
    moves = []
    for key in range(2,13):
        if board[key] is True:
             moves.append(key)
    return moves

def smart_move(board, number):
    print("test")
    
#generates a random move from the possible moves
#returns a valid move set, if no valid move set then returns a list containing 0
def monte_move(board, number):
    possibleMoves = possible_moves(board)
    move = [0]
    
    if randint(possibleMoves[0],number) + sum(move) in possibleMoves:
        move.append
    
    
    
    

init_board(board)

        