# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from util import Stack
    
    stack_node = Stack() #creating a stack for the nodes 
    stack_path=  Stack() #creating a stack for the lists of actions taken to reach a particular node 

    visited_list = [] # Visited nodes list
    path_list = [] # for keeping track of path of everystate (means list of actions taken to reach that state(node)) from the starting state

    # Checking whether the  initial node is goal node or not
    if problem.isGoalState(problem.getStartState()):  #if it is a goal state return empty list
        return []

    stack_node.push(problem.getStartState()) #pushing initial node to the stack
    stack_path.push([])                        #since no path required for reaching initial node so pushing an empty list

    while(True):
    
        if stack_node.isEmpty():
            return []

        node = stack_node.pop() #obtain the current node from the stack_node
        path_list=stack_path.pop() #get the the path_list(list of actions taken to reach the cuurent node from the starting node)
        visited_list.append(node)     #if a node is visited add that node to visited nodes list


        # return path list if goal state is found
        if problem.isGoalState(node):
            return path_list

        #for getting the successors of the current state call getSuccessors function
        succ_list = problem.getSuccessors(node)
          #succ_list is the list of information of its successor nodes
        
        if succ_list:  # checking whether the node have successors or not
            for item in succ_list:          #item in successors list contains a list of tuples and  each tuple contains 
                if item[0] not in visited_list:
    
                    Path_list = path_list + [item[1]] # adding new action to the path list
                    stack_node.push(item[0])     # if node is not a goal state push the node to stack
                    stack_path.push(Path_list)   # also push the path to that node
    util.raiseNotDefined()
    

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue

    queue_state = Queue()#creating a queue for the state which contain node and lists of actions taken to reach a particular node  
    visited_list = [] #  # Visited nodes list
    path_list = [] # for keeping track of path of everystate (means list of actions taken to reach that state(node)) from the starting state
    
    if problem.isGoalState(problem.getStartState()):# Checking whether the  initial node is goal node or not
        return []                                   #if it is a goal state return empty list

    queue_state.push((problem.getStartState(),[])) #push the initial state
    
    while(True):

        if queue_state.isEmpty():
            return []
        
        node,path_list= queue_state.pop() #obtain the current node from the queue_node
                                         #get the the path_list(list of actions taken to reach the cuurent node from the starting node)
        visited_list.append(node) #if a node is visited add that node to visited nodes list
        # return path list if goal state is found
        if problem.isGoalState(node):
            return path_list

        #for getting the successors of the current state call getSuccessors function
        succ_list = problem.getSuccessors(node)
        #succ_list is the list of information of its successor nodes
        if succ_list:   # checking whether the node have successors or not
            for item in succ_list:
                if item[0] not in visited_list and item[0] not in (state[0] for state in queue_state.list):#checking whether node is not in visited
                
                    Path_list = path_list + [item[1]]     # adding new action to the path list
                    queue_state.push((item[0],Path_list))         
                                                           # also push the path to that node
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue

    priority_queue = PriorityQueue()

    visited_list = [] # Visited nodes list
    path_list = []    # for keeping track of path of everystate (means list of actions taken to reach that state(node)) from the starting state

    if problem.isGoalState(problem.getStartState()):# Checking whether the  initial node is goal node or not
        return []                                   #if it is a goal state return empty list

    priority_queue.push((problem.getStartState(),[]),0) #push initial_node,its empty path list

    while(True):

        if priority_queue.isEmpty():
            return []
            
        node,path_list = priority_queue.pop() #obtain the current node and its path list from the queue_node
        if node in visited_list:#if node is found in visited_list then the lower cost path already found so just leave that node
            continue
        visited_list.append(node)             #if a node is visited add that node to visited nodes list
        # return path list if goal state is found
        if problem.isGoalState(node):
            return path_list
        #for getting the successors of the current state call getSuccessors function
        succ_list = problem.getSuccessors(node)
        #succ_list is the list of information of its successor nodes
        if succ_list:   # checking whether the node have successors or not
            for item in succ_list:#checking whether node is not in visited
                if item[0] not in visited_list :

                    Path_list = path_list + [item[1]]  # push that node ,path_list,cost of actions for that path list
                    priority_queue.push((item[0],Path_list),problem.getCostOfActions(Path_list))
                    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def f(problem,state,heuristic):        #calculate f(n) = g(n) + h(n), f(n)=pathcost to reach node n and estimated cost to reach goal node

    return problem.getCostOfActions(state[1]) + heuristic(state[0],problem)
    
def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    priorityqueue = PriorityQueue()

    path_list = [] # Visited nodes list
    visited_list = [] # for keeping track of path of everystate (means list of actions taken to reach that state(node)) from the starting state
    # Checking whether the  initial node is goal node or not
    if problem.isGoalState(problem.getStartState()):#if it is a goal state return empty list
        return []

    node = problem.getStartState() #get initial node 
    #push initial node,initial empty path list,and also f value for the intial node into priority_queue
    priorityqueue.push((node,[]),f(problem,(node,[]),heuristic))

    while(True):

    
        if priorityqueue.isEmpty():    #if queue is empty then return empty path list means no goal state found 
            return []

        node,path_list = priorityqueue.pop() #else get the current node and path_list from queue based on f value (priority)

        
        if node in visited_list:#if node is found in visited_list then the lower cost path already found so just leave that node
            continue
        visited_list.append(node) #else not found means add to visited_list

        if problem.isGoalState(node): #if that node is goal state then return the path_list
            return path_list

   
        succ_list = problem.getSuccessors(node)#for getting the successors of the current state call getSuccessors function
         #succ_list is the list of information of its successor nodes
        if succ_list: # checking whether the node have successors or not
                      #item in successors list contains a list of tuples and  each tuple contains node,action,cost
            for item in succ_list:
                if item[0] not in visited_list:#if node is not visited then add the action corresponding to that node to the path list
                
                    Path_list = path_list + [item[1]] 
                    #again push that node ,its path_list,its f value into the priority_queue
                    priorityqueue.push((item[0],Path_list),f(problem,(item[0],Path_list),heuristic))
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
