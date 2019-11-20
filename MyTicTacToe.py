#Coursework Assignment part 2 TicTacToe

import math
def Board(board):

    print (" %s | %s | %s " % (board[0], board[1], board[2]))
    print ("-----------")
    print (" %s | %s | %s " % (board[3], board[4], board[5]))
    print ("-----------")
    print (" %s | %s | %s " % (board[6], board[7], board[8]))

def GoalState(board,letter):
    if ((board[0] == letter and board[1] == letter and board[2] == letter) or #top row
    (board[3] == letter and board[4] == letter and board[5] == letter) or # middle row
    (board[6] == letter and board[7] == letter and board[8] == letter) or # bottom row
    (board[0] == letter and board[3] == letter and board[6] == letter) or # left collumn
    (board[1] == letter and board[4] == letter and board[7] == letter) or # middle collumn
    (board[2] == letter and board[5] == letter and board[8] == letter) or # right column
    (board[0] == letter and board[4] == letter and board[8] == letter) or # diagonal left to right downwards
    (board[2] == letter and board[4] == letter and board[6] == letter)): # diagonal right to left downwards
        return  True

    

def ChoseSide():
    choice = input('Are you X or are you O? X/O :').upper()
    while choice not in ["X", "O"]:
        print("incorrect input, choose between X/O")
        choice = input('Are you X or are you O? X/O :').upper()
    if choice == "X":
        return "X", "O"
    else:
        return "O", "X"

def WhoFirst():
    turn = input("Play first Y/N? :").upper()
    while turn not in ["Y", "N"]:
        print("Incorrect input, please input one of the following values Y/N :")
        turn = input("Play first Y/N? :").upper()
    if turn == "Y":
        return "human"
    elif turn == "N":
        return "computer"


def AllowedMoves(board, letter):
    AllowedMoves = []
    for i in [0,1,2,3,4,5,6,7,8]:
        Copyboard = board[:]
        if Copyboard[i] == " ":
            AllowedMoves.append(make_move(Copyboard,letter,i)) #list which containts the next possible moves, based on the board
    return AllowedMoves

def find_score(board, computer, human):
    if GoalState(board, human): #if computer wins
        return -10
    elif GoalState(board, computer): #if player wins
        return 10
    elif board[0] != " " and board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[6] != " " and board[7] != " " and board[8] != " " :
        return 0


def pick_move(board):
    move = input("Make your choice 0-8 :")
    if move in ['0','1','2','3','4','5','6','7','8'] and board[int(move)] == " ":
        return int(move)
    else:
       
        while move not in ['0','1','2','3','4','5','6','7','8']:
            print("This option is not available. Please choose a number from 0 to 8.")
            move = input("Make your choice 0-8 :")
            if move in ['0','1','2','3','4','5','6','7','8'] and board[int(move)] == " ":
                return int(move)
        while board[int(move)] != " ":
            print("This option is not available, because someone has used this move.")
            move = input("Make your choice 0-8 :")
            if move in ['0','1','2','3','4','5','6','7','8'] and board[int(move)] == " ":
                return int(move)
    



def make_move(board, letter, move):
    new_board = list(board)
    new_board[move] = letter
    return new_board


    
def alphabeta(board, depth, computer,human, Maximise,alpha, beta):
    score = find_score(board, computer, human)
    if score == 10 or score == -10 or score == 0 or depth == 0:
        return score, board   
    if Maximise == True :
        MaxEval = -math.inf
        BestMove = None
        for moves in AllowedMoves(board,computer):
            evaluation, choice = alphabeta(moves, depth -1, computer, human,False, alpha, beta)
            if evaluation > MaxEval :
                BestMove = moves
                MaxEval = evaluation
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
            print(MaxEval)
            if MaxEval == 0:
                print("This is a Tie move max",MaxEval, Board(BestMove))
            elif MaxEval == 10:
                print("This is a Losing move max",MaxEval,)
            elif MaxEval == -10:
                print("This is a Maximising move max",MaxEval, Board(BestMove))
        return MaxEval, BestMove

    else:
        BestMove = None
        MinEval = math.inf
        for moves in AllowedMoves(board,human):
            evaluation, choice = alphabeta(moves, depth -1, computer, human, True , alpha, beta)
            if evaluation < MinEval:
                MinEval = evaluation
                BestMove = moves
            beta = min(beta,evaluation)
            if beta <= alpha:
                break
            print(MinEval)
            if MinEval == 0:
                print("This is a Tie move min",MinEval, Board(BestMove))
            elif MinEval == 10:
                print("This is a Minimising move min",MinEval , Board(BestMove))
            elif MinEval == -10:
                print("This is a Losing move min",MinEval)
        return MinEval, BestMove
    
        
print('Welcome to Tic Tac Toe!')
board = [" "] * 9
human, computer = ChoseSide()
turn = WhoFirst()

print("This is the initial board:")
Board(board)

Gaming = True
while Gaming:
    if turn == "human":
        move = pick_move(board)
        board = make_move(board, human, move)
        Board(board)
        if GoalState(board, human):
            print("You Won, cheater")
            Gaming = False
        else:
            if board[0] != " " and board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[6] != " " and board[7] != " " and board[8] != " " :
                print("That's a Tie")
                Gaming = False
                break
            else:
                turn = "computer"
    elif turn == "computer":
        print("This is what opponent played:")
        score, board = alphabeta(board,9, computer,human ,True,-10,10)
        Board(board)
        if GoalState(board,computer):
            print("You Lost")
            Gaming = False
        else:
            if board[0] != " " and board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[6] != " " and board[7] != " " and board[8] != " " :
                print(" That's a Tie")
                Gaming = False

            else:
                turn = "human"

