#This is the part 1 Assignment of Foundations of AI COMP
#initialised the board in the state that each location within the baord had a corresponding value such as 
#    ---- ---- ---- ----
#   |  0 |  1 |  2 |  3 |    
#    ---- ---- ---- ----
#   |  4 |  5 |  6 |  7 |    
#    ---- ---- ---- ----
#   |  8 |  9 | 10 | 11 |    
#    ---- ---- ---- ----
#   | 12 | 13 | 14 | 15 |    
#    ---- ---- ---- ----  


import math
import random

#Starting positions of the tiles and the agent
TileA = 5
TileB = 9
TileC = 12

Agent = 15

#creating and inputting the values that are corresponding to the tiles and agent 1=Tile1, 2=Tile2, 3=Tile3, 9=Agent
StartState = []
for i in range(0,16):
    if i==TileA:
        StartState.append(1)
    elif i==TileB:
        StartState.append(2)
    elif i==TileC:
        StartState.append(3)
    elif i==Agent:
        StartState.append(9)
    else:
        StartState.append(0)
print(StartState)

#This are the different situatins that a goal state has been identified
#where the agent is in all the positions beside the ones where the tiles should be 
GoalState0  = [9,0,0,0,0,1,0,0,0,2,0,0,0,3,0,0]
GoalState1  = [0,9,0,0,0,1,0,0,0,2,0,0,0,3,0,0]
GoalState2  = [0,0,9,0,0,1,0,0,0,2,0,0,0,3,0,0]
GoalState3  = [0,0,0,9,0,1,0,0,0,2,0,0,0,3,0,0]
GoalState4  = [0,0,0,0,9,1,0,0,0,2,0,0,0,3,0,0]
GoalState5  = [0,0,0,0,0,1,9,0,0,2,0,0,0,3,0,0]
GoalState6  = [0,0,0,0,0,1,0,9,0,2,0,0,0,3,0,0]
GoalState7  = [0,0,0,0,0,1,0,0,9,2,0,0,0,3,0,0]
GoalState8  = [0,0,0,0,0,1,0,0,0,2,9,0,0,3,0,0]
GoalState9  = [0,0,0,0,0,1,0,0,0,2,0,9,0,3,0,0]
GoalState10 = [0,0,0,0,0,1,0,0,0,2,0,0,9,3,0,0]
GoalState11 = [0,0,0,0,0,1,0,0,0,2,0,0,0,3,9,0]
GoalState12 = [0,0,0,0,0,1,0,0,0,2,0,0,0,3,0,9]
# Class for Node to reference aupon within the algorithm
# the necessary variables are state,its parent, action, cost of movement and depth of node
class Node:
    def __init__( self, state, parent, action, cost, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth

#Special case for A * - same as class Node plus storing the result of the heuristic function
class AstarNode:
    def __init__( self, state, parent, action, cost, depth, h_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth
        self.h_cost = h_cost
    


#Function for movement
def movement (state, direction):
    NEW_STATE=list(state) # generate the list of the tiles
    AgentPos = NEW_STATE.index(9) #identify the agent position and assign it 
    #if the agent goes up
    if direction == "up": 
        if AgentPos not in [0,1,2,3]: # if it's not in the top range do 
            AgentNewPos = NEW_STATE[AgentPos - 4] # assign new positions
            # move agent up
            NEW_STATE[AgentPos - 4] = NEW_STATE[AgentPos]
            # Replace the tile that the agent was located with NewPostion
            NEW_STATE[AgentPos] = AgentNewPos
            return NEW_STATE #return the new state of the agent
    # if the agent goes down
    if direction == "down":
        if AgentPos not in [12,13,14,15]: # if it's not in the bottom range do 
            AgentNewPos = NEW_STATE[AgentPos + 4] # assign new positions
            # move agent down
            NEW_STATE[AgentPos + 4] = NEW_STATE[AgentPos]
            # Replace the tile that the agent was located with NewPostion
            NEW_STATE[AgentPos] = AgentNewPos
            return NEW_STATE #return the new state of the agent
    #if the agent goes left
    if direction == "left":
        if AgentPos not in [0,4,8,12]: # if it's not in  the left-most range do 
            AgentNewPos = NEW_STATE[AgentPos - 1] # assign new positions
            #move agent left
            NEW_STATE[AgentPos - 1] = NEW_STATE[AgentPos]
            # Replace the tile that the agent was located with NewPostion
            NEW_STATE[AgentPos] = AgentNewPos
            return NEW_STATE #return the new state of the agent
    # if the agent moves right
    if direction == "right":
        if AgentPos not in [3,7,11,15]: # if it's in  the right-most range do 
            AgentNewPos = NEW_STATE[AgentPos + 1] # assign new positions
            #move agent right
            NEW_STATE[AgentPos + 1] = NEW_STATE[AgentPos]
            # if it's not in the bottom range do 
            NEW_STATE[AgentPos] = AgentNewPos
            return NEW_STATE #return the new state of the agent
    #else do nothing
    else:
        return None


        
#define the board state and accordingly the positions    
def Board(state):
        #copy the current list
        Copylist = state[:]
        #identify locations of tiles and agent
        tilea = Copylist.index(1)
        tileb = Copylist.index(2)
        tilec = Copylist.index(3)
        agent = Copylist.index(9)
        #where tiles and agent found replace visually
        Copylist[tilea] = 'A'
        Copylist[tileb] = 'B'
        Copylist[tilec] = 'C'
        Copylist[agent] = '*'
        Copylist = [ x if x!= 0 else " " for x in Copylist ]
        
        #print the board
    
        print ("-----------------")
        print ("| %s | %s | %s | %s |" % (Copylist[0], Copylist[1], Copylist[2], Copylist[3]))
        print ("-----------------")
        print ("| %s | %s | %s | %s |" % (Copylist[4], Copylist[5], Copylist[6], Copylist[7]))
        print ("-----------------")
        print ("| %s | %s | %s | %s |" % (Copylist[8], Copylist[9], Copylist[10], Copylist[11]))
        print ("-----------------")
        print ("| %s | %s | %s | %s |" % (Copylist[12], Copylist[13], Copylist[14], Copylist[15]))
        print ("-----------------")
        
#Visualise the sequence of movement for the agent in order to reach the solution
def visualiase_movement(move,state):
    #copy the list of the state
    new_list_state = list(state)
    #initialise new position
    NewPosition = list(new_list_state)
    #set the new state, depending on the movement
    if move == "up":
        NewPosition = movement( new_list_state, "up" )
    elif move == "down":
        NewPosition = movement( new_list_state, "down" )
    elif move == "left":
        NewPosition = movement( new_list_state, "left" )
    elif move == "right":
        NewPosition = movement( new_list_state, "right" )
    #return the new state
    return NewPosition


#Expand node with the possible movements
#append to the list the several nodes that will be displayed on expandsion based on the movement used based on the values (state,parent,action,cost,depth)
#for each movement towards the goal expand the node and alter the successors in order to find the solution and also increase the depth and cost by 1
def ExpandNode (node):
    Expanded=[] #Initilise list of succesors
    Expanded.append( Node( movement(node.state, "up" ), node, "up", node.cost + 1, node.depth + 1 ))
    Expanded.append( Node( movement(node.state, "down" ), node, "down",node.cost + 1, node.depth + 1 ))
    Expanded.append( Node( movement(node.state, "left" ), node, "left",node.cost + 1, node.depth + 1 ))
    Expanded.append( Node( movement(node.state, "right" ), node, "right",node.cost + 1, node.depth + 1 ))
    Expanded = [node for node in Expanded if node.state != None] #remove the ones with no movement
    return Expanded 

#randmisation function
def shuffle (node):
    random.shuffle(node)
    return node

#Expand node while include the heuristic cost for astar2
def ExpandNodeAstar2( node,goal ):
    Expanded = []
    Expanded.append( AstarNode( movement( node.state, "up" ), node, "up", node.cost + 1, node.depth + 1, h2(movement( node.state, "up" ), goal) ) )
    Expanded.append( AstarNode( movement( node.state, "down" ), node, "down", node.cost + 1, node.depth + 1, h2(movement( node.state, "down" ), goal) ) )
    Expanded.append( AstarNode( movement( node.state, "left" ), node, "left", node.cost + 1, node.depth + 1, h2(movement( node.state, "left" ), goal) ) )
    Expanded.append( AstarNode( movement( node.state, "right" ),  node, "right", node.cost + 1, node.depth + 1, h2(movement( node.state, "right" ), goal) ) )
    Expanded = [node for node in Expanded if node.state != None]
    return Expanded

#Expand node while include the heuristic cost for astar1
def ExpandNodeAstar (node):
    Expanded=[]
    Expanded.append(AstarNode(movement( node.state, "up"),node, "up", node.cost + 1, node.depth+1, AddDepth(node,h1(node.state))))
    Expanded.append(AstarNode(movement( node.state, "down"),node, "down", node.cost + 1, node.depth+1, AddDepth(node,h1(node.state))))
    Expanded.append(AstarNode(movement( node.state, "left"),node, "left", node.cost + 1, node.depth+1, AddDepth(node,h1(node.state))))
    Expanded.append(AstarNode(movement( node.state, "right"),node, "right", node.cost + 1, node.depth+1, AddDepth(node,h1(node.state))))
    Expanded = [node for node in Expanded if node.state != None] 
    return Expanded

def Comparison(child, explored, Fringe):
    for i in range(0,len(explored)):
        if child.state == explored[i].state:
            return True
    for i in range(0,len(Fringe)):
        if child.state == Fringe[i].state:
            return True
    return False


def bfs(start):
    #initialise the list of the nodes to be expanded  
    Fringe = []
    #initilise list of explored nodes.
    explored = []
    #initilise list to input moves if solution found.
    moves = [] 
    #set boolean for braking loop
    bottom = 1
    #Append Initial State
    Fringe.append( Node( start, None, None, 0, 0 ) )

    while bottom != 0:
        #if bottom has been reached and no more nodes to left to use
        if len( Fringe ) == 0:
            bottom = 0 # brake loop
            return None, len(explored) #return the length of the explored values.
        #use the first node of the Fringe 
        node = Fringe.pop(0)
        #check if it's in any state of a goal(s)
        if node.state == GoalState0 or node.state == GoalState1 or node.state == GoalState2 or node.state == GoalState3 or node.state == GoalState4 or node.state == GoalState5 or node.state == GoalState6 or node.state == GoalState7 or node.state == GoalState8 or node.state == GoalState9 or node.state == GoalState10 or node.state == GoalState11 or node.state == GoalState12:
            #if goal as been reached do
            while True:
                # insert into list the action taken
                moves.insert(0, node.action)
                # if the state is right after initialstate
                if node.depth == 1:
                    # brake loop
                    break
                # swap place of the child with the parent
                node = node.parent
            # terminate while loop
            bottom = 0
            # return moves plus nodes expanded/explored
            return moves, len(explored)
        # append the explored to the list explored
        explored.append(node)
        #explore the children and for each child append to Fringe
        children = ExpandNode(node)
        for child in children:
            #if not Comparison(child, explored, Fringe): #for graph search
                Fringe.append(child)
            
                print('nodes expanded', len(explored))
                print("BFS with depth: " + str(child.depth))
                actionsdone = []
                actionsdone.insert(0, child.action)
                print(actionsdone)
                Board(child.state)
#For Depth First Search
def dfs(start):
    #same logic with breadth first search,although the function used to insert into the fringe i used insert 
    #this was done in order to choose the initial position to append the childs in order to enable Depth-First-Search
    #in this case, the last node of the stack must be expanded
    Fringe = []
    explored = []
    moves = []
    bottom = 1
    Fringe.append( Node( start, None, None, 0, 0 ) )
    #implimented a user input algorithm to enable the user wether he/she wants to choose the randomisation function or not.
    rndmchoices = input("1) Without Randomisation 2) With Randomisation:")
    while rndmchoices not in ['1','2']:  
        print("you have not inputted the correct choice valid input is 1/2") 
        rndmchoices = input("1) Without Randomisation 2) With Randomisation:") 
    else:     
        while bottom!= 0:
            if len( Fringe ) == 0:
                bottom = 0
                return None, len(explored)
            # use the first node of the lstack (LIFO)
            node = Fringe.pop(0)
            if node.state == GoalState0 or node.state == GoalState1 or node.state == GoalState2 or node.state == GoalState3 or node.state == GoalState4 or node.state == GoalState5 or node.state == GoalState6 or node.state == GoalState7 or node.state == GoalState8 or node.state == GoalState9 or node.state == GoalState10 or node.state == GoalState11 or node.state == GoalState12:
                while True:
                    moves.insert(0, node.action)
                    if node.depth == 1:
                        break
                    node = node.parent
                bottom = 0
                return moves, len(explored)
            explored.append(node)  
            if rndmchoices == '1':
                
                children = ExpandNode(node)
            if rndmchoices == '2':
                children = shuffle(ExpandNode(node))
            
            #i is the indicator where the child will be saved and iterates through it until all  childs are inserted.
            i = 0
            for child in children:
                #if not Comparison(child, explored, Fringe): for Graph search
                    Fringe.insert(i,child)
                    i+=1      
                    print('nodes expanded', len(explored))
                    print("DFS with depth: " + str(child.depth))
                    Board(child.state)
                
def dls( start, depth ):
    #depth limited search implimented with a value supplied at the call of the function of 5000
    limit = depth
    Fringe = []
    explored = []
    moves =[]
    bottom = 1
    Fringe.append( Node( start, None, None, 0, 0 ) )
    while bottom != 0:
        if len( Fringe ) == 0:
            bottom = 0
            return None, len(explored)
        node = Fringe.pop(0)
        if node.state == GoalState0 or node.state == GoalState1 or node.state == GoalState2 or node.state == GoalState3 or node.state == GoalState4 or node.state == GoalState5 or node.state == GoalState6 or node.state == GoalState7 or node.state == GoalState8 or node.state == GoalState9 or node.state == GoalState10 or node.state == GoalState11 or node.state == GoalState12:
            while True:
                moves.insert(0, node.action)
                if node.depth == 1:
                    break
                node = node.parent
            bottom = 0
            return moves, len(explored)
        #until  the limit has been reached iterate through the following
        if node.depth < limit:
            explored.append(node)
            children = ExpandNode(node)
            for child in children:
                #if not Comparison(child, explored, Fringe): #for graph search
                    Fringe.insert(0,child)
                    print('nodes expanded', len(explored))
                    print("With depth: " + str(child.depth))
                    Board(child.state)



def ids( start, depth ):
    #Keep the expansion of the nodes even though displaying otherwise
    AllExpanded = 0
    #iterate the dls function for each depth until it reaches the limit that the user gives
    for i in range( depth + 1 ): #adding one since it starts from 0 to reach the approrpiate depth
        result, amount = dls( start, i )
        #increment by amount
        AllExpanded += amount
        #if the goal has beeen reached present the 
        if result != None:
            return result, AllExpanded
            break
    #if the goal is not reached, when the depth is reached present the following expansion
    if result == None:
        return result, AllExpanded      
          
#faster algorithm for astar
def astar1(start):
    Fringe = []
    moves = []
    explored = []
    bottom = 1
    
    Fringe.append(AstarNode(start, None,None,0,0,h1(start))) #similar to normal Node although we also supply heauristics cost.
    while bottom!= 0: #iterative loop for the end of the expansion.
        if len(Fringe)== 0:
            bottom = 0
            return None, len(explored)

        Fringe = sorted(Fringe, key=lambda node: node.h_cost) # sorting according to the heurstics provided h_cost
        node = Fringe.pop(0) #using the first(lowest) value possible to fid the answer.
        if node.state == GoalState0 or node.state == GoalState1 or node.state == GoalState2 or node.state == GoalState3 or node.state == GoalState4 or node.state == GoalState5 or node.state == GoalState6 or node.state == GoalState7 or node.state == GoalState8 or node.state == GoalState9 or node.state == GoalState10 or node.state == GoalState11 or node.state == GoalState12:
            while True: #following the same routine as the other algorythms to expand the nodes and append the output.
                moves.insert(0, node.action) 
                if node.depth == 1:
                    break
                node = node.parent
            bottom = 0
            return moves, len(explored)
        explored.append(node)
        children = ExpandNodeAstar(node) # using specialised expansion that includes the first heurstic h1
        for child in children:
            # if not Comparison(child, explored, Fringe): #for graph search
                    Fringe.append(child)
                    print('nodes expanded', len(explored))
                    print("astar1 with depth: " + str(child.depth))
                    Board(child.state)

# heuristic one function takes the values of the current state and based on their goal position a heuristic is drawn 
# from the tiles that are misplaces so 0 is goal state 1,2,3 
#alsong with the distance of the tile from its goal state 
#these values are then added to produce a heursitic score to use for helping the algorithm.
def h1(state):
    Misplaced = 0
    Distance = 0
    
    if state[5] != 1:
        Misplaced+=1
        Distance += math.fabs(state.index(1)-5)
    if state[9] != 2:
        Misplaced+=1
        Distance += math.fabs(state.index(2)-9)
    if state[13] != 3:
        Misplaced+=1    
        Distance += math.fabs(state.index(3)-13)
    Heuristic=Distance+Misplaced
    print(Heuristic)
    return Heuristic
#function used to incorporate depth within algorithm1
def AddDepth(node, heuristic):
    AddDepth = (node.depth + heuristic)
    return AddDepth 


def astar2(start, goal):
    Fringe = []
    moves = []
    explored = []
    bottom = 1
    #insert the initial state
    Fringe.append( AstarNode( start, None, None, 0, 0, h2( start, goal ) ) )

    while bottom!= 0:
        if len(Fringe)== 0:
            return None, len(explored)
        #same as previously although this time also incorporating the depth and the heursitic cost of the state of the algorithm 
        Fringe = sorted(Fringe, key=lambda node: node.depth + node.h_cost)
        node = Fringe.pop(0)
        if node.state == GoalState0 or node.state == GoalState1 or node.state == GoalState2 or node.state == GoalState3 or node.state == GoalState4 or node.state == GoalState5 or node.state == GoalState6 or node.state == GoalState7 or node.state == GoalState8 or node.state == GoalState9 or node.state == GoalState10 or node.state == GoalState11 or node.state == GoalState12:
            while True:
                moves.insert(0, node.action)
                if node.depth == 1:
                    break
                node = node.parent
            bottom = 0
            return moves, len(explored)
        explored.append(node)
        children = ExpandNodeAstar2(node,goal)
        for child in children:
            #if not Comparison(child, explored, Fringe): #for grah search
                    Fringe.append(child)
                    print('nodes expanded', len(explored))
                    print("astar2 with depth: " + str(child.depth))
                    Board(child.state)

def h2( state, goal ):
    #if no state identified 
    if state == None:
        return None
    else:
        Heuristic = 0
        #find position of current and goal state
        Currentstate = find_index( state )
        ar,ac,br,bc, cr, cc = find_index( state )
        print(Currentstate) #for debug
        Setgoal = find_index( goal )
        gar,gac,gbr,gbc, gcr, gcc = find_index( goal )
        print(Setgoal) #for debug
        
        #for i in range(len(Currentstate)): multiplies and enhances algorithm
        Heuristic += abs(gar-ar) + abs(gac-ac) #for tilea
        Heuristic += abs(gbr-br) + abs(gbc-bc) #for tileb 
        Heuristic += abs(gcr-cr) + abs(gcc-cc) #for tilec

        print(Heuristic)
        return Heuristic

                    
#find the place of each tile in the board in order to ssist the heuristic2
def find_index(node):
    TileA = node.index(1)
    TileB = node.index(2)
    TileC = node.index(3)
    #set the row and the colum for each tile
    RowA, ColumnA = FindRowColumn( TileA )
    RowB, ColumnB = FindRowColumn( TileB )
    RowC, ColumnC = FindRowColumn( TileC )
    return list([RowA, ColumnA, RowB, ColumnB, RowC, ColumnC])

def FindRowColumn(state):
    #initialise row and column
    row = 0
    column = 0
    #if the tile is in the first row
    if state in [0,1,2,3]:
        row = 0
    #if the tiles is in the second row
    elif state in [4,5,6,7]:
        row = 1
    #if the tiles is in the third row
    elif state in [8,9,10,11]:
        row = 2
    #if the tiles is in the fourth row
    elif state in [12,13,14,15]:
        row = 3
        
    if state in [0,4,8,12]:
        column = 0
    elif state in [1,5,9,13]:
        column = 1
    elif state in [2,6,10,14]:
        column = 2
    elif state in [3,7,11,15]:
        column = 3
    #return the number of the row and column
    return row, column



goal = GoalState12
depth = 14              
nodes =[]
choices = ""
choices = input("Which Algorithm: 1) BFS 2) DFS 3) DLS 4) IDS 5) A* 6) A*-2 7) Exit :")
while choices not in ['1','2','3','4','5', '6', '7']:  
    print("you have not inputted the correct choice valid input is 1/2/3/4/5/6 or 7 for Exit") 
    choices = input("Which Algorithm: 1) BFS 2) DFS 3) DLS 4) IDS 5) A* 6) A*-2 7) Exit :")
 
else:   
 
        if choices == '1':
            result, amount = bfs(StartState)
            print("the moves are ", (result))
            print("the amount of iterations ", amount )
        elif choices == '2':
            result, amount = dfs(StartState)
            print("the moves are ", (result))
            print("the amount of iterations ", amount )
        elif choices == '3':
            result, amount = dls(StartState, depth)
            #print("the moves are ", (result)) #for debug
            print("the amount of iterations ", amount )
        elif choices == '4':
            result, amount = ids(StartState, depth)
            print("the moves are ", (result))
            print("the amount of iterations ", amount )
        elif choices == '5':
            result, amount = astar1(StartState)
            print("the moves are ", (result))
            print("the amount of iterations ", amount )
        elif choices == '6':
            result, amount = astar2(StartState, goal)
            print("the moves are ", (result))
            print("the amount of iterations ", amount )
        elif choices == '7': 
            print("See Ya!")
        if choices in ['1','2','4','5','6']:  
            nodes.append(amount)   
            if result == None:
                print("This search method didn't solve the problem")
            else:
                print(len(result), "moves")
                Board(StartState)
            for iter in range(len(result)):
                if iter == 0:
                    a = visualiase_movement(result[iter],StartState)
                    Board(a)
                elif iter == 1:
                    temp = a
                    b = visualiase_movement(result[iter], temp)
                    c = b
                    Board(c)
                else:
                    temp = c
                    b = visualiase_movement(result[iter], temp)
                    c = b
                    Board(c)
            print("the moves are ", (result))
            print("the amount of iterations ", amount )
            print('the solution is visualised above')
            