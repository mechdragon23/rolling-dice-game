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
    