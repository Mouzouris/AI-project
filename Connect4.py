#Coursework Assignment part 2 Connect 4
import math
import numpy as np
RowCount = 6
ColumnCount = 7

def Board():

    board = np.zeros((RowCount,ColumnCount))
    return board

def PrintBoard(board):
	print(np.flip(board, 0))
    
def IsZero(board, col):
	for r in range(RowCount):
		if board[r][col] == 0 :
			return r 
    
def IsValid(board, col):
    if col < 0 or col > ColumnCount:
        return 0
    return board[RowCount - 1][col] == 0
#      
def GoalState(board, letter):
    counter = 0
	# Check Horizontal Win				
    for col in range(ColumnCount-3):
        for row in range(RowCount):
            counter=0
            for i in range(4):
                if board[row][col+i] == letter:
                    counter += 1
            if counter == 4: 
                return True
                    
	# Check Vertical Win				
    for col in range(ColumnCount):
        for row in range(RowCount-3):
            counter=0
            for i in range(4):
                if board[row+i][col] == letter:
                    counter += 1
            if counter == 4: 
                return True
	# Check / Diagonal Win

    for col in range(ColumnCount-3):
        for row in range(RowCount-3):
            counter = 0
            for i in range(4):
                if board[row+i][col+i] == letter:
                    counter +=1
            if counter == 4:
                return True
	# Check \ Diagonal Win

    for col in range(ColumnCount-3):
        for row in range(3, RowCount):
            counter = 0
            for i in range(4):
                if board[row-i][col+i] == letter:
                    counter += 1
            if counter == 4:
                return True

            
def MakeMove(board,row, col,letter):
    board[row][col] = letter
    return board
	

def AllowedMoves(board, letter):
    AllowedMoves = [] 
    for col in range(ColumnCount ):
        Copyboard = np.copy(board)
        #for row in range(RowCount):
        if IsValid(Copyboard,col):
            row = IsZero(Copyboard, col)
            AllowedMoves.append(MakeMove(Copyboard,row,col,letter)) 
                            
    return AllowedMoves

    
def full_board(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for col in range(ColumnCount):
        if IsValid(board, col):
            return False
            pass
    return True  

    
def ChoseSide():
    choice = input('Are you Player 1 or are you Player 2? 1/2 :').upper()
    while choice not in ["1", "2"]:
        print("incorrect input, choose between 1/2")
        choice = input('Are you Player 1 or are you Player 2? 1/2 :').upper()
    if choice == "1":
        return 1, 2
    else:
        return 2, 1

def WhoFirst():
    turn = input("Play first Y/N? :").upper()
    while turn not in ["Y", "N"]:
        print("Incorrect input, please input one of the following values Y/N :")
        turn = input("Play first Y/N? :").upper()
    if turn == "Y":
        return "human"
    elif turn == "N":
        return "computer"



def PickMove(board):
    col = input("Make your choice 0-6 or 9 to Exit :")
    if col in ['0','1','2','3','4','5','6','9'] and IsValid(board, int(col)) or col == '9':
        return int(col)
    else:
        while col not in ['0','1','2','3','4','5','6','9']:
            print("This option is invalid. Please choose a number from 0 to 6 or 9 for Exit.")
            col = input("Make your choice 0-6 or 9 to Exit :")
            if col in ['0','1','2','3','4','5','6','9'] and IsValid(board, int(col)) or col == '9':
                return int(col)
        while not IsValid(board, int(col)):
            print("This option is not available. Please choose a number from 0 to 6 or 9 for Exit.")
            col = input("Make your choice 0-6 or 9 to Exit :")
            if col in ['0','1','2','3','4','5','6','9'] and IsValid(board, int(col)) or col == '9':
                return int(col)

        
            
    

def evaluate(board,computer,human):
    if GoalState(board, human):
        return -999999999
    elif GoalState(board, computer):
        return 999999999 
    elif full_board(board):
        return 909090909
    else:
        score = 0

        for col in range(ColumnCount-3):
            for row in range(RowCount):
                FilledChoices = 0
                player = 0
                for i in range(4):
                    if board[row][col+i] != 0:
                        FilledChoices += 1
                        player = board[row][col+i] == computer and player + 1 or player - 1
                score += (FilledChoices * 2 * player) + (FilledChoices / 2)


        for col in range(ColumnCount):
            for row in range(RowCount-3):
                FilledChoices = 0
                player = 0
                for i in range(4):
                    if board[row+i][col] != 0:
                        FilledChoices += 1
                        player = board[row+i][col] == computer and player + 1 or player - 1
                score += (FilledChoices * 2 * player) + (FilledChoices / 2)


        for col in range(ColumnCount-3):
            for row in range(RowCount-3):
                FilledChoices = 0
                player = 0
                for i in range(4):
                    if board[row+i][col+i] != 0:
                        FilledChoices += 1
                        player = board[row+i][col+i] == computer and player + 1 or player - 1
                score += (FilledChoices * 2 * player) + (FilledChoices / 2)


        for col in range(ColumnCount-3):
            for row in range(3, RowCount):
                FilledChoices = 0
                player = 0
                for i in range(4):
                    if board[row-i][col+i] != 0:
                        FilledChoices += 1
                        player = board[row-i][col+i] == computer and player + 1 or player - 1
                score += (FilledChoices * 2 * player) + (FilledChoices / 2)


        return score


    
def alphabeta(board, depth, computer,human, Maximise,alpha, beta):
    score = evaluate(board, computer, human)
    if score == 999999999 or score == -999999999 or score == 909090909 or depth == 0:
        return score, board
    if Maximise == True :
        MaxEval = -math.inf
        BestMove = None
        for moves in (AllowedMoves(board,computer)):
            
            evaluation, choice = alphabeta(moves, depth -1, computer, human,False, alpha, beta)
            print(evaluation)
            if evaluation > MaxEval :
                BestMove = moves
                MaxEval = evaluation
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
#            print(MaxEval)
#            if MaxEval == 0:
#                print("This is a Tie move max",MaxEval, Board(BestMove))
#            elif MaxEval == 10:
#                print("This is a Losing move max",MaxEval,)
#            elif MaxEval == -10:
#                print("This is a Maximising move max",MaxEval, Board(BestMove))
        return MaxEval, BestMove

    else:
        BestMove = None
        MinEval = math.inf
        for moves in (AllowedMoves(board,human)):
            evaluation, choice = alphabeta(moves, depth -1, computer, human, True , alpha, beta)
            print(evaluation)
            if evaluation < MinEval:
                MinEval = evaluation
                BestMove = moves
            beta = min(beta,evaluation)
            if beta <= alpha:
                break
#            print(MinEval)
#            if MinEval == 0:
#                print("This is a Tie move min",MinEval, Board(BestMove))
#            elif MinEval == 10:
#                print("This is a Minimising move min",MinEval , Board(BestMove))
#            elif MinEval == -10:
#                print("This is a Losing move min",MinEval)
        return MinEval, BestMove
    
        
print('Welcome to Connect 4!')
board = Board()
human, computer = ChoseSide()
turn = WhoFirst()

print("This is the initial board:")
PrintBoard(board)

Gaming = True
while Gaming:
    if turn == "human":
        col = PickMove(board)
        if col == 9 :
            print("See Ya!")
            Gaming = False
        else:
            print(col)
            if IsValid(board,col):
                row = IsZero(board, col)
                print(row)
                board = MakeMove(board,row,col, human) 
            PrintBoard(board)
            if GoalState(board, human):
                print("You Won, cheater")
                Gaming = False
            else:
                if full_board(board):
                    print("That's a Tie")
                    Gaming = False
                    break
                else:
                    turn = "computer"
    elif turn == "computer":
        print("This is what opponent played:")
        score, board = alphabeta(board, 4 , computer,human ,True,-999999999,999999999)
        PrintBoard(board)
        if GoalState(board,computer):
            print("You Lost")
            Gaming = False
        else:
            if full_board(board):
                print(" That's a Tie")
                Gaming = False

            else:
                turn = "human"

#fails
#    print ("-----------------------------")
#    print ("| %s | %s | %s | %s | %s | %s | %s |" % (board[0], board[1], board[2], board[3], board[4], board[5], board[6]))
#    print ("-----------------------------")
#    print ("| %s | %s | %s | %s | %s | %s | %s |" % (board[7], board[8], board[9], board[10], board[11], board[12], board[13]))
#    print ("-----------------------------")
#    print ("| %s | %s | %s | %s | %s | %s | %s |" % (board[14], board[15], board[16], board[17], board[18], board[19], board[20]))
#    print ("-----------------------------")
#    print ("| %s | %s | %s | %s | %s | %s | %s |" % (board[21], board[22], board[23], board[24], board[25], board[26], board[27]))
#    print ("-----------------------------")
#    print ("| %s | %s | %s | %s | %s | %s | %s |" % (board[28], board[29], board[30], board[31], board[32], board[33], board[34]))
#    print ("-----------------------------")
#    print ("| %s | %s | %s | %s | %s | %s | %s |" % (board[35], board[36], board[37], board[38], board[39], board[40], board[41]))
#    print ("-----------------------------")
#     
#
#         
#def GoalState(board,letter):
#    if ((board[0][0] == letter and board[0][1] == letter and board[0][2] == letter and board[0][3] == letter) or
#        (board[0][1] == letter and board[0][2] == letter and board[0][3] == letter and board[0][4] == letter) or #first streight line
#        (board[0][2] == letter and board[0][3] == letter and board[0][4] == letter and board[0][5] == letter) or
#        (board[0][3] == letter and board[0][4] == letter and board[0][5] == letter and board[0][6] == letter) or
#        
#        (board[1][0] == letter and board[1][1] == letter and board[1][2] == letter and board[1][3] == letter) or
#        (board[1][1] == letter and board[1][2] == letter and board[1][3] == letter and board[1][4] == letter) or #second streight line
#        (board[1][2] == letter and board[1][3] == letter and board[1][4] == letter and board[1][5] == letter) or
#        (board[1][3] == letter and board[1][4] == letter and board[1][5] == letter and board[1][6] == letter) or
#        
#        (board[2][0] == letter and board[2][1] == letter and board[2][2] == letter and board[2][3] == letter) or
#        (board[2][1] == letter and board[2][2] == letter and board[2][3] == letter and board[2][4] == letter) or #third streight line
#        (board[2][2] == letter and board[2][3] == letter and board[2][4] == letter and board[2][5] == letter) or
#        (board[2][3] == letter and board[2][4] == letter and board[2][5] == letter and board[2][6] == letter) or
#        
#        (board[3][0] == letter and board[3][1] == letter and board[3][2] == letter and board[3][3] == letter) or
#        (board[3][1] == letter and board[3][2] == letter and board[3][3] == letter and board[3][4] == letter) or #fourth streight line
#        (board[3][2] == letter and board[3][3] == letter and board[3][4] == letter and board[3][5] == letter) or
#        (board[3][3] == letter and board[3][4] == letter and board[3][5] == letter and board[3][6] == letter) or
#        
#        (board[4][0] == letter and board[4][1] == letter and board[4][2] == letter and board[4][3] == letter) or
#        (board[4][1] == letter and board[4][2] == letter and board[4][3] == letter and board[4][4] == letter) or #fifth streight line
#        (board[4][2] == letter and board[4][3] == letter and board[4][4] == letter and board[4][5] == letter) or
#        (board[4][3] == letter and board[4][4] == letter and board[4][5] == letter and board[4][6] == letter) or
#                
#        (board[5][0] == letter and board[5][1] == letter and board[5][2] == letter and board[5][3] == letter) or
#        (board[5][1] == letter and board[5][2] == letter and board[5][3] == letter and board[5][4] == letter) or #sixth streight line
#        (board[5][2] == letter and board[5][3] == letter and board[5][4] == letter and board[5][5] == letter) or
#        (board[5][3] == letter and board[5][4] == letter and board[5][5] == letter and board[5][6] == letter) or
#        
#        
#        #middle
#
#        (board[0][0] == letter and board[1][0] == letter and board[2][0] == letter and board[3][0] == letter) or
#        (board[1][0] == letter and board[2][0] == letter and board[3][0] == letter and board[4][0] == letter) or #first middle line
#        (board[2][0] == letter and board[3][0] == letter and board[4][0] == letter and board[5][0] == letter) or
#                
#        (board[0][1] == letter and board[1][1] == letter and board[2][1] == letter and board[3][1] == letter) or
#        (board[1][1] == letter and board[2][1] == letter and board[3][1] == letter and board[4][1] == letter) or #second middle line
#        (board[2][1] == letter and board[3][1] == letter and board[4][1] == letter and board[5][1] == letter) or
#         
#        (board[0][2] == letter and board[1][2] == letter and board[2][2] == letter and board[3][2] == letter) or
#        (board[1][2] == letter and board[2][2] == letter and board[3][2] == letter and board[4][2] == letter) or #third middle line
#        (board[2][2] == letter and board[3][2] == letter and board[4][2] == letter and board[5][2] == letter) or
#          
#        (board[0][3] == letter and board[1][3] == letter and board[2][3] == letter and board[3][3] == letter) or
#        (board[1][3] == letter and board[2][3] == letter and board[3][3] == letter and board[4][3] == letter) or #fourth middle line
#        (board[2][3] == letter and board[3][3] == letter and board[4][3] == letter and board[5][3] == letter) or
#                
#        (board[0][4] == letter and board[1][4] == letter and board[2][4] == letter and board[3][4] == letter) or
#        (board[1][4] == letter and board[2][4] == letter and board[3][4] == letter and board[4][4] == letter) or #firfth middle line
#        (board[2][4] == letter and board[3][4] == letter and board[4][4] == letter and board[5][4] == letter) or
#    
#        (board[0][5] == letter and board[1][5] == letter and board[2][5] == letter and board[3][5] == letter) or
#        (board[1][5] == letter and board[2][5] == letter and board[3][5] == letter and board[4][5] == letter) or #sixth middle line
#        (board[2][5] == letter and board[3][5] == letter and board[4][5] == letter and board[5][5] == letter) or
#                        
#        (board[0][6] == letter and board[1][6] == letter and board[2][6] == letter and board[3][6] == letter) or
#        (board[1][6] == letter and board[2][6] == letter and board[3][6] == letter and board[4][6] == letter) or #seventh middle line
#        (board[2][6] == letter and board[3][6] == letter and board[4][6] == letter and board[5][6] == letter) or
#
#                                
#        
#        #diagonal form right to left
#        (board[0][3] == letter and board[1][2] == letter and board[2][1] == letter and board[3][0] == letter) or
#        
#        (board[0][4] == letter and board[1][3] == letter and board[2][2] == letter and board[3][1] == letter) or 
#        (board[1][3] == letter and board[2][2] == letter and board[3][1] == letter and board[4][0] == letter) or
#        
#        (board[0][5] == letter and board[1][4] == letter and board[2][3] == letter and board[3][2] == letter) or
#        (board[1][4] == letter and board[2][3] == letter and board[3][2] == letter and board[4][1] == letter) or
#        (board[2][3] == letter and board[3][2] == letter and board[4][1] == letter and board[5][0] == letter) or
#        
#        
#        (board[0][6] == letter and board[1][5] == letter and board[2][4] == letter and board[3][3] == letter) or
#        (board[1][5] == letter and board[2][4] == letter and board[3][3] == letter and board[4][2] == letter) or
#        (board[2][4] == letter and board[3][3] == letter and board[4][2] == letter and board[5][1] == letter) or
#        
#        (board[1][6] == letter and board[2][5] == letter and board[3][4] == letter and board[4][3] == letter) or 
#        (board[2][5] == letter and board[3][4] == letter and board[4][3] == letter and board[5][2] == letter) or
#        
#        (board[2][6] == letter and board[3][5] == letter and board[4][4] == letter and board[5][3] == letter) or
#        
#        #diagonal from left to right
#        (board[0][3] == letter and board[1][4] == letter and board[2][5] == letter and board[3][6] == letter) or
#        
#        (board[0][2] == letter and board[1][3] == letter and board[2][4] == letter and board[3][5] == letter) or 
#        (board[1][3] == letter and board[2][4] == letter and board[3][5] == letter and board[4][6] == letter) or
#        
#        (board[0][1] == letter and board[1][2] == letter and board[2][3] == letter and board[3][4] == letter) or
#        (board[1][2] == letter and board[2][3] == letter and board[3][4] == letter and board[4][5] == letter) or
#        (board[2][3] == letter and board[3][4] == letter and board[4][5] == letter and board[5][6] == letter) or
#        
#        
#        (board[0][0] == letter and board[1][1] == letter and board[2][2] == letter and board[3][3] == letter) or
#        (board[1][1] == letter and board[2][2] == letter and board[3][3] == letter and board[4][4] == letter) or
#        (board[2][2] == letter and board[3][3] == letter and board[4][4] == letter and board[5][5] == letter) or
#        
#        (board[1][0] == letter and board[2][1] == letter and board[3][2] == letter and board[4][3] == letter) or 
#        (board[2][1] == letter and board[3][2] == letter and board[4][3] == letter and board[5][4] == letter) or
#        
#        (board[2][0] == letter and board[3][1] == letter and board[4][2] == letter and board[5][3] == letter)): 
#        return  True
