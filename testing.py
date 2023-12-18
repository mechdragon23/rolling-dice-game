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

#returns a valid move play for the given possible moves
def smart_move(number, possibleMoves):
    move = []
    tempNum = number
    
    #tries to chose the highest valid number
    if tempNum in possibleMoves:
        move.append(tempNum)
        return move
    
    #if not then run 2 sum until a valid combo is found
    else:
        seen = {}
        for i in range(len(possibleMoves)):
            result = number - possibleMoves[i]
            if result in seen:
                #print("appending ", possibleMoves[i])
                move.append(possibleMoves[i])
                #print("appending ", possibleMoves[seen[result]])
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
    
#a simpler random algorithm to generate a moveset
def better_monte_move(number, possibleMoves):
    tries = 1000
    found = False
    sample = []
    
    #choses random possible number sets until the sum is equal to the number
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
        

#extract data from file
def extract(filenum):
    #opening the file
    filename = str(filenum) + ".txt"
    file = open(filename, "r")
    
    #reading in all the lines
    lines = file.readlines()
    
    #initalize the number array to check for valid moves
    nums = []
    for i in range(2,13):
        nums.append(str(i))
        
    #parcing through the lines and appending the data to a list
    moveset = []
    i = 0
    for line in lines:          #for each line
        line = line.split(".")  #split the line at "."
        moveset.append([])      #initalize a new index for the moveset
        for word in line:       
            if word[-1] == ",":
                temp = []
                word = word.split(",")
                for char in word:
                    if char in nums:
                        #print(char)
                        temp.append(int(char))
                #print(temp)
                moveset[i].append(temp)
            else:
                moveset[i].append(int(word))
        i += 1
    #print(moveset)
    return moveset

#takes in a list of data and writes it to the file
def write_file(data, filenum):
    
    #opening the file to write to
    filename = str(filenum) + ".txt"
    file = open(filename, "w")
    
    #for each line of data
    for line in data:
        array = line[0] #seperate the move
        move = ""       #write the move to a string
        for num in array:
            move = move + str(num) + ","
        writeLine = move + "." + str(line[1]) + "." + str(line[2]) + "\n"
        file.write(writeLine) 
    

# ------------------- MAIN -----------------------
samplesize = 1000
tries = samplesize 
wins = 0    
loss = 0
writeCol = 2    #the colum to tally up, W/L 1/2

while tries > 0:
    init_board(board)
    playing = True
    diceRolls = []
    moveHistory = []

    print("running sample #",samplesize - tries)
    while playing:
        #print("The current board is:")
        #print(board)
        diceRoll = roll_dice()
        #print("rolled dice: ", diceRoll)
        diceRolls.append(diceRoll)
        
        possibleMoves = possible_moves(board)
        #print("the possible moves are: ", possibleMoves)
        
        moves = better_monte_move(diceRoll, possibleMoves)
        #print("monte has choosen: ",moves)
        moves.sort()
        #print(moves)
        moveHistory.append(moves)
        
        
        if len(moves) > 0:
            for move in moves:
                if move in board:
                    board = execute_move(board, move)
                    
        #print("checking win...")
        if check_win(board) is True:
            #print("won")
            playing = False
            wins = wins + 1
            writeCol = 1
        if len(moves) == 0:
            #print("loss")
            playing = False
            loss = loss + 1
            writeCol = 2
    
    #adding results to the files     
    for index in range(len(moveHistory)):
        data = extract(diceRolls[index])    #extract data from file
        for line in data:
            if line[0] == moveHistory[index]:   #if move is similar
                line[writeCol] += 1 #increment win/loss
        write_file(data, diceRolls[index])  #write the data
    #print("dice rolls: ",diceRolls)
    #print("move history: ",moveHistory)
    
    tries = tries - 1
    
print("played: ", samplesize, " Won: ", wins, " Loss: ", loss, " Win %: ", (wins/samplesize * 100))
        