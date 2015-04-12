# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

from util import Stack
from util import Queue

def commonSearch(problem, dataStructure):


    currentPosition = problem.getStartState()

    stackNodes = dataStructure

    alreadyVisitedNodes = []

    stackNodes.push([(currentPosition, "Stop", 0)])
    alreadyVisitedNodes += [currentPosition]
    rounds = 0

    while not stackNodes.isEmpty():

        rounds += 1
        currentPath = stackNodes.pop()

        lastState = currentPath[len(currentPath) - 1][0]

        for tempLocation in problem.getSuccessors(lastState):

            if problem.isGoalState(tempLocation[0]):
                goalPath = []
                for tempNode in currentPath:
                    goalPath += [tempNode[1]]
                return goalPath + [tempLocation[1]]

            if tempLocation[0] not in alreadyVisitedNodes:
                alreadyVisitedNodes += [tempLocation[0]]

                stackNodes.push(currentPath + [tempLocation])

    return []

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 85].

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    return commonSearch(problem, Stack())



def breadthFirstSearch(problem):
    "Search the shallowest nodes in the search tree first. [p 81]"

    return commonSearch(problem, Queue())

from util import PriorityQueueWithFunction

def uniformCostSearch(problem):
    "Search the node of least total cost first. "

    def costFunction(path1):
        pathNodes = []
        for tempNode in path1:
            pathNodes += [tempNode[1]]
        return problem.getCostOfActions(pathNodes)

    return commonSearch(problem, PriorityQueueWithFunction(costFunction))


def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."

    def costFunction(path1):
        pathNodes = []
        for tempNode in path1:
            pathNodes += [tempNode[1]]
        return problem.getCostOfActions(pathNodes) + heuristic(path1[len(path1) - 1][0], problem)

    return commonSearch(problem, PriorityQueueWithFunction(costFunction))

  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch