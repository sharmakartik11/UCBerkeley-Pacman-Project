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

def depthFirstSearch(problem):
    "*** YOUR CODE HERE ***"

    # create fringe to store nodes
    fringe = util.Stack()
    # track visited nodes
    visited = []
    # push initial state to fringe
    fringe.push((problem.getStartState(), [], 1))
    
    while not fringe.isEmpty():
        node = fringe.pop()
        state = node[0]
        actions = node[1]
        # visited node
        # goal check
        if problem.isGoalState(state):
            return actions
        if state not in visited:
            visited.append(state)
            # visit child nodes
            successors = problem.getSuccessors(state)
            for child in successors:
                # store state, action and cost = 1
                child_state = child[0]
                child_action = child[1]
                if child_state not in visited:
                    # add child nodes
                    child_action = actions + [child_action]
                    fringe.push((child_state, child_action, 1))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
                
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Q1.3
    Search the node that has the lowest combined cost and heuristic first."""
    """Call heuristic(s,problem) to get h(s) value."""
    "*** YOUR CODE HERE ***"
    # create fringe to store nodes
    fringe = util.PriorityQueue()
    # track visited nodes
    visited = []
    # push initial state to fringe
    fringe.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem))
    while not fringe.isEmpty():
        node = fringe.pop()
        state = node[0]
        actions = node[1]
        # goal check
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.append(state)
            # visit child nodes
            successors = problem.getSuccessors(state)
            for child in successors:
                # store state, action and cost = 1
                child_state = child[0]
                child_action = child[1]
                if child_state not in visited:
                    # add child nodes
                    child_action = actions + [child_action]
                    cost = problem.getCostOfActions(child_action)
                    fringe.push((child_state, child_action, 0), cost + heuristic(child_state, problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
