'''
This file initialized the files needed to store ML data
For each number there will be a file with a list of moves, wins, and losses
Formated as so:

File Name: 12

moveset     wins    losses
12          5       3884
10,2        8       4727
9,3         3       3821
8,4         8       3729
7,5         7       5473
7,3,2       3       3275
5,4,3       5       4367
etc...      
'''

#initalize the file
def init_file(filenum):
    #temp init values
    wins = 1
    losses = 1
    
    #creating and opening the file
    filename = str(filenum) + ".txt"
    file = open(filename, "w")
    
    #writing in the lines
    #writing in first line
    line = str(filenum) + ",." + str(wins) + "." + str(losses) + "\n"
    file.write(line)
    
    #writing in 2sum lines
    moveset = find_2sum(filenum)
    for array in moveset:
        move = ""
        for num in array:
            move = move + str(num) + ","
        line = move + "." + str(wins) + "." + str(losses) + "\n"
        file.write(line)
        
    #writing 3sum combos
    third = filenum - 7
    moveset = []
    
    #checking if the current file num is large enough
    if third >= 2:
        #appending the 3sum arrays to the moveset
        for i in range(2,third + 1):
            target = filenum - i
            twosum = find_2sum(target)
            for array in twosum:
                if i not in array:
                    array.append(i)
                    array.sort()
                    if array not in moveset:
                        moveset.append(array)
                    
        #write the completed moveset to the file
        for array in moveset:
            move = ""
            for num in array:
                move = move + str(num) + ","
            line = move + "." + str(wins) + "." + str(losses) + "\n"
            file.write(line)
    #close the file
    file.close()
  
#given a target number find all combinations that add up without repeats  
#returns a list of valid combinations
def find_2sum(target):
    seen = {}
    possibleMoves = []
    moveset = []
    
    #initalizing the possible move set
    for i in range(2, target + 1):
        possibleMoves.append(i)
        
    #running 2sum
    for i in range(len(possibleMoves)):
        result = target - possibleMoves[i]
        if result in seen:
            move = []
            move.append(possibleMoves[i])
            move.append(possibleMoves[seen[result]])
            move.sort()
            if move not in moveset:
                moveset.append(move)
        seen[possibleMoves[i]] = i
        
    return moveset
         
#given a file number to read from, reads in the data as a 2d array
#returns a list containing the movesets, wins, losses in the following format
'''
   moveset,     wins,   losses
[[[12],         1,      1], 
 [[5, 7],       1,      1], 
 [[4, 8],       1,      1], 
 [[3, 9],       1,      1], 
 [[2, 10],      1,      1], 
 [[2, 4, 6],    1,      1], 
 [[2, 3, 7],    1,      1], 
 [[3, 4, 5],    1,      1]]
'''
def read_file(filenum):
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

#--------------MAIN-------------
for i in range(2,13):
    init_file(i)
    
'''
file12 = read_file(12)
file12[1][1] = 3
print(file12)
write_file(file12, 12)
'''