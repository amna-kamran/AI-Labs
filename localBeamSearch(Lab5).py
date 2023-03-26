import math
class Node:
  def __init__(self, state, parent, actions, totalCost, heuristic):
    self.state = state
    self.parent = parent
    self.actions = actions
    self.totalCost = totalCost
    self.heuristic = heuristic

graph = {
    "A" : Node("A", None, [("F", 1)], 0, (0, 0)),
    "B" : Node("B", None, [("G", 1), ("C", 1)], 0, (2, 0)),
    "C" : Node("C", None, [("B", 1), ("D", 1)], 0, (3, 0)),
    "D" : Node("D", None, [("C", 1), ("E", 1)], 0, (4, 0)),
    "E" : Node("E", None, [("D", 1)], 0, (5, 0)),
    "F" : Node("F", None, [("A", 1), ("H", 1)], 0, (0, 1)),
    "G" : Node("G", None, [("B", 1), ("J", 1)], 0, (2, 1)),
    "H" : Node("H", None, [("F", 1), ("I", 1), ("M", 1)], 0, (0, 2)),
    "I" : Node("I", None, [("H", 1), ("J", 1), ("N", 1)], 0, (1, 2)),
    "J" : Node("J", None, [("G", 1), ("I", 1)], 0, (2, 2)),
    "K" : Node("K", None, [("L", 1), ("P", 1)], 0, (4, 2)),
    "L" : Node("L", None, [("K", 1), ("Q", 1)], 0, (5, 2)),
    "M" : Node("M", None, [("H", 1), ("N", 1), ("R", 1)], 0, (0, 3)),
    "N" : Node("N", None, [("I", 1), ("M", 1), ("S", 1)], 0, (1, 3)),
    "O" : Node("O", None, [("P", 1), ("U", 1)], 0, (3, 3)),
    "P" : Node("P", None, [("O", 1), ("Q", 1)], 0, (4, 3)),
    "Q" : Node("Q", None, [("L", 1), ("P", 1), ("V", 1)], 0, (5, 3)),
    "R" : Node("R", None, [("M", 1) ,("S", 1)], 0, (0, 4)),
    "S" : Node("S", None, [("N", 1), ("R", 1), ("T", 1)], 0, (1, 4)),
    "T" : Node("T", None, [("S", 1), ("U", 1), ("W", 1)], 0, (2, 4)),
    "U" : Node("U", None, [("O", 1), ("T", 1)], 0, (3, 4)),
    "V" : Node("V", None, [("Q", 1), ("Y", 1)], 0, (5, 4)),
    "W" : Node("W", None, [("T", 1)], 0, (2, 5)),
    "X" : Node("X", None, [("Y", 1)], 0, (4, 5)),
    "Y" : Node("Y", None, [("V", 1), ("X", 1)], 0, (5, 5))
}

def localBeamSearch(graph, initialState, goalState, beamWidth):
    parentNode = initialState
    parentCost = math.sqrt(((graph[goalState].heuristic[0] - graph[initialState].heuristic[0])**2) + ((graph[goalState].heuristic[1] - graph[initialState].heuristic[1])**2))
    explored = []
    solution = []
    minChildCost = parentCost - 1
    bestNodes = []

    while parentNode != goalState:
        print("Parent Node:", parentNode)
        bestNode = parentNode
        minChildCost = parentCost
        explored.append(parentNode)
        for child in graph[parentNode].actions:
            if child[0] not in explored:
                childCost = math.sqrt(((graph[goalState].heuristic[0] - graph[child[0]].heuristic[0]) ** 2) + ((graph[goalState].heuristic[1] - graph[child[0]].heuristic[1]) ** 2))
                bestNodes.append((childCost, child[0]))
                if childCost < minChildCost:
                    bestNode = child[0]
                    minChildCost = childCost
        #sorting the child nodes
        bestNodes.sort()
        print("Child Nodes:", bestNodes)
        bestNodes = bestNodes[:beamWidth]
        if bestNode == parentNode:
            if len(bestNodes) < 1:
                break
            elif bestNode == bestNodes[0][1]:
                bestNodes.pop(0)
                minChildCost, bestNode = bestNodes.pop(0)
                last = solution[len(solution) - 2]
                for n in graph[last].actions:
                    if bestNode in n:
                        solution.pop()
            else:
                minChildCost, bestNode = bestNodes.pop(0)
        parentNode = bestNode
        parentCost = minChildCost
        solution.append(parentNode)
    return solution

solution = localBeamSearch(graph, "A", "Y", 2)
print("Solution:", solution)