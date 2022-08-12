# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        #import manhattan Distance
        from util import manhattanDistance 
        
        #Initialize ghostDistance and foodDistance to zero
        ghostDistance = 0
        foodDistance = 0
        #ghostDistance is the sum of total manhattanDistance from position to all ghost position
        for ghost in newGhostStates:
        	ghostDistance = sum([manhattanDistance(newPos,ghost.getPosition())])
        
        #foodDistance is minimum of all manhattanDistance from the new position to all food location in newFood.asList()
        for foodLoc in newFood.asList():
        	try: foodDistance = min([manhattanDistance(newPos,foodLoc)])
        	except: foodDistance = 0
        
        totalScore = 4 * min(4, ghostDistance) + 15/(1+foodDistance)
        return successorGameState.getScore() + totalScore

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        #minimum value function
        def minValue(state, agentIndex, depth):
        	#total number of agents
        	totalAgent = state.getNumAgents()
        	#getting the legal actions
        	legalActions = state.getLegalActions(agentIndex)
        	
        	#if no legal action are there then return evaluation function
        	if not legalActions:
        		return self.evaluationFunction(state)
        		
        	#if there is only pacman movement left
        	if agentIndex == totalAgent - 1:
        		#call the maxValue to all its successor and choose minimum of them
        		miniValue = min(maxValue(state.generateSuccessor(agentIndex,action),agentIndex, depth)for action in legalActions)
        	else:
        		#call the minValue to all its successor and choose minimum of them
        		miniValue = min(minValue(state.generateSuccessor(agentIndex,action),agentIndex+1, depth)for action in legalActions)
        	
        	#finally return minimum value
        	return miniValue
        	
        #maximum value function
        def maxValue(state, agentIndex, depth):
        	#Initialize agent index to zero
        	agentIndex = 0
        	#getting the legal actions
        	legalActions = state.getLegalActions(agentIndex)
        	
        	#if no legal action are there and we reached maximum depth then return evaluation function
        	if not legalActions or depth == self.depth:
        		return self.evaluationFunction(state)
        		
        	#call the minValue to all its successor and choose maximum of them
        	maxiValue = max(minValue(state.generateSuccessor(agentIndex,action),agentIndex+1, depth+1)for action in legalActions)
        	
        	return maxiValue #finally return maximum value
        	
        #We have to maximize all possible moves from root node, so for pacman agent index be zero
        actions = gameState.getLegalActions(0)
        
        #We are storing all actions with its value and return the maximum value among them
        totalactions = {}
        
        
        for action in actions:
        	totalactions[action] = minValue(gameState.generateSuccessor(0,action),1,1)
        	
        return max(totalactions, key = totalactions.get)
        
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        #minimum value function
        def minValue(state, agentIndex, depth, alpha, beta):
        	#total number of agents
        	totalAgent = state.getNumAgents()
        	#getting the legal actions
        	legalActions = state.getLegalActions(agentIndex)
        	
        	#if no legal action are there then return evaluation function
        	if not legalActions:
        		return self.evaluationFunction(state)
        		
        	#Initializing minimum value to infinite and present beta to beta
        	miniValue = 99999
        	presentBeta = beta    
        		
        	#if there is only pacman movement left
        	if agentIndex == totalAgent - 1:
        		for action in legalActions:
        			#call the maxValue to all its successor and choose minimum of previously minimum value and its successor value
        			miniValue = min(miniValue, maxValue(state.generateSuccessor(agentIndex,action),agentIndex, depth, alpha, presentBeta))
        			#if minimum value is less than alpha then we return minimum value , we don't further check (we prunned that part)
        			if miniValue < alpha:
        				return miniValue
        		
        			presentBeta = min(miniValue,presentBeta)
        		
        	else:
        		for action in legalActions:
        		#call the minValue to all its successor and choose minimum of previously minimum value and its successor value
        			miniValue = min(miniValue, minValue(state.generateSuccessor(agentIndex,action),agentIndex+1, depth,alpha,presentBeta))
        			#if minimum value is less than alpha then we return minimum value , we don't further check (we prunned that part)
        			if miniValue < alpha:
        				return miniValue
        		
        			presentBeta = min(miniValue,presentBeta)
        	
        	return miniValue
        	
        	
        def maxValue(state, agentIndex, depth, alpha ,beta):
        	#Initializing agent index to zero
        	agentIndex = 0
        	#getting the legal actions
        	legalActions = state.getLegalActions(agentIndex)
        	
        	#if no legal action are there and we reached maximum depth then return evaluation function
        	if not legalActions or depth == self.depth:
        		return self.evaluationFunction(state)
        		
        	#Initializing maximum value to negative infinite and present alpha to alpha
        	maxiValue = -99999
        	presentAlpha = alpha
        	
        	for action in legalActions:
        	#call the maxValue to all its successor and choose maximum of previously maximum value and its successor value
        		maxiValue = max(maxiValue,minValue(state.generateSuccessor(agentIndex,action),agentIndex+1, depth+1,presentAlpha,beta) )
        		#if maximum value is greater than beta then return maximum value , so that we don't further check(we prunned that part)
        		if maxiValue > beta:
        			return maxiValue
        		
        		presentAlpha = max(presentAlpha,maxiValue)
        	
        	return maxiValue
        	
        #We have to maximize all possible moves from root node, so for pacman agent index be zero
        actions = gameState.getLegalActions(0)
        
        #Initialize alpha to negative infinite and beta to infinite
        alpha = -99999
        beta = 99999
        
        #We are storing all actions with its value and return the maximum value among them
        totalactions = {}
        
        for action in actions:
        	value = minValue(gameState.generateSuccessor(0,action),1,1, alpha, beta)
        	totalactions[action] = value
        	
        	if value > beta:
        		return action
        	
        	alpha = max(alpha,value)

        return max(totalactions, key = totalactions.get)
        	
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        #expected value function
        def expValue(state, agentIndex, depth):
        	#total number of agents
        	totalAgent = state.getNumAgents()
        	#getting the legal actions
        	legalActions = state.getLegalActions(agentIndex)
        	
        	#if no legal action are there then return evaluation function
        	if not legalActions:
        		return self.evaluationFunction(state)
        		
        	#Initializing expected value to zero
        	expectedValue = 0
        	#probability will be the reciprocal of length of legal actions
        	prob = 1.0/len(legalActions)
        	
        	for action in legalActions:
        		#if there is only pacman movement left
        		if agentIndex == totalAgent - 1:
        			#call maxValue to all its successor
        			presentExpectedValue = maxValue(state.generateSuccessor(agentIndex,action),agentIndex, depth)
        		else:
        			#call expValue to all its successor
        			presentExpectedValue = expValue(state.generateSuccessor(agentIndex,action),agentIndex+1, depth)
        	
        		#calculating its total expected value
        		expectedValue += presentExpectedValue * prob
        	return expectedValue
        	
        	
        def maxValue(state, agentIndex, depth):
        	#Initializing agent index to zero
        	agentIndex = 0
        	#getting the legal actions
        	legalActions = state.getLegalActions(agentIndex)
        	
        	#if no legal action are there and we reached maximum depth then return evaluation function
        	if not legalActions or depth == self.depth:
        		return self.evaluationFunction(state)
        		
        	#call expValue to all its successor and choose maximum of them
        	maxiValue = max(expValue(state.generateSuccessor(agentIndex,action),agentIndex+1, depth+1)for action in legalActions)
        	
        	return maxiValue
        	
        #We have to maximize all possible moves from root node, so for pacman agent index be zero
        actions = gameState.getLegalActions(0)
        
        #We are storing all actions with its value and return the maximum value among them
        totalactions = {}
        
        for action in actions:
        	totalactions[action] = expValue(gameState.generateSuccessor(0,action),1,1)
        	
        return max(totalactions, key = totalactions.get)
        	
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    #getting the location of pacman
    location = currentGameState.getPacmanPosition()
    #foods list contains the total foods in all position 
    foodsList = currentGameState.getFood().asList()
    #we find the closest food distance by help of manhattan distance for all food in foodsList and choose minimum of them
    #if foodslist is empty then closest food distance taking as 1(assume)
    closestfoodDistance = min(manhattanDistance(location, food) for food in foodsList) if foodsList else 1
    #calculating the score in currentGameState
    score = currentGameState.getScore()
		
		#as the food distance is minimum then evaluation will be maximum(i.e, evaluation score is inversely proportional to food distance) 
    evaluation = 1.0 / closestfoodDistance + score
    return evaluation
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
