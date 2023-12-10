from random import randint
import random

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
    
#exectues the move given, takes in the board and the move
#returns the board
def execute_move(board, move):
    board[move] = False
    return board
    
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

def smart_move(number, possibleMoves):
    move = []
    tempNum = number
    if tempNum in possibleMoves:
        move.append(tempNum)
        return move
    else:
        seen = {}
        for i in range(len(possibleMoves)):
            result = number - possibleMoves[i]
            if result in seen:
                print("appending ", possibleMoves[i])
                move.append(possibleMoves[i])
                print("appending ", possibleMoves[seen[result]])
                move.append(possibleMoves[seen[result]])
                return move
            seen[possibleMoves[i]] = i
    return move
            
    
    
    
    
    
#generates a random move from the possible moves
#returns a valid move set, if no valid move set then returns a list containing 0
def monte_move(number, possibleMoveList):
    possibleMoves = possibleMoveList
    move = []  #init the move set to be returned
    tempNum = number    #set a temporary modifiable number
    tries = 1000    #number of tries the algorithm will attempt
    
    
    while tempNum > 0 and tries > 0:
        if tempNum > possibleMoves[0]:
            possibleMove = randint(possibleMoves[0],tempNum)
        else:
            move = [0]
            tempNum = number
            possibleMoves = possibleMoveList
            #print("reset")
        #print("current num: ", number)
        #print("current tries: ", tries)
        
        #print("checking : ", possibleMove)
        #check if the random number is in possible moves
        if possibleMove + sum(move) in possibleMoves:
            move.append(possibleMove)
            possibleMoves.remove(possibleMove)
            tempNum = tempNum - possibleMove
            #print("the move list is now: ", move)
            #print("temp num is now: ",tempNum)
        else:
            tries = tries - 1
            #print("tries decresed")
            
        #if number not found after 10 tries, then reset
        if tries % 10 == 1:
            if tempNum not in possibleMoves:
                move = [0]
                tempNum = number
                possibleMoves = possibleMoveList
                #print("reset")
                
    if tries == 0:
        return []
    else:
        return move
    
def better_monte_move(number, possibleMoves):
    tries = 1000
    found = False
    sample = []
    
    while tries > 0 and not found:
        sample = random.sample(possibleMoves,randint(1,min(4, len(possibleMoves))))
        #print("trying: ", sample)
        if sum(sample) == number:
            found = True
        else:
            tries = tries - 1
            
    if tries == 0:
        sample = []
    
    return sample
        
    
samplesize = 10000
tries = samplesize 
wins = 0    
loss = 0

while tries > 0:
    init_board(board)
    playing = True

    while playing:
        #print("The current board is:")
        #print(board)
        diceRoll = roll_dice()
        print("rolled dice: ", diceRoll)
        possibleMoves = possible_moves(board)
        print("the possible moves are: ", possibleMoves)
        moves = smart_move(diceRoll, possibleMoves)
        print("monte has choosen: ",moves)
        
        if len(moves) > 0:
            for move in moves:
                if move in board:
                    board = execute_move(board, move)
                    
        print("checking win...")
        if check_win(board) is True:
            print("won")
            playing = False
            wins = wins + 1
        if len(moves) == 0:
            print("loss")
            playing = False
            loss = loss + 1
    
    tries = tries - 1
    
print("played: ", samplesize, " Won: ", wins, " Loss: ", loss, " Win %: ", (wins/samplesize * 100))
        