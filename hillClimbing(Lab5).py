import math

class Node:
  def __init__(self, state, parent, actions, heuristic, totalCost):
    self.state = state
    self.parent = parent
    self.actions = actions
    self.totalCost = totalCost
    self.heuristic = heuristic

def hillclimbing(ist, gst):
  initialstate = ist
  goalstate=gst
  #creating two lists
  explored=[]
  solution=[]
  #graph
  graph = {'A': Node('A', None, [('F',1)], (0,0), 0),
           'B': Node('B', None, [('G',1), ('C',1)], (2,0), 0),
           'C': Node('C', None, [('B',1), ('D',1)], (3,0), 0),
           'D': Node('D', None, [('C',1), ('E',1)], (4,0), 0),
           'E': Node('E', None, [('D',1)], (5,0), 0),
           'F': Node('F', None, [('A',1), ('H',1)], (0,1), 0),
           'G': Node('G', None, [('B',1), ('J',1)], (2,1), 0),
           'H': Node('H', None, [('F',1), ('I',1), ('M',1)], (0,2), 0),
           'I': Node('I', None, [('N',1), ('J',1), ('H',1)], (1,2), 0),
           'J': Node('J', None, [('G',1), ('I',1)], (2,2), 0),
           'K': Node('K', None, [('L',1), ('P',1)], (4,2), 0),
           'L': Node('L', None, [('K',1), ('Q',1)], (5,2), 0),
           'M': Node('M', None, [('H',1), ('N',1), ('R',1)], (0,3), 0),
           'N': Node('N', None, [('I',1), ('M',1), ('S',1)], (1,3), 0),
           'O': Node('O', None, [('P',1), ('U',1)], (3,3), 0),
           'P': Node('P', None, [('O',1), ('Q',1),('K',1)], (4,3), 0),
           'Q': Node('Q', None, [('L',1), ('P',1), ('V',1)], (5,3), 0),
           'R': Node('R', None, [('M',1), ('S',1)], (0,4), 0),
           'S': Node('S', None, [('N',1), ('R',1), ('T',1)], (1,4), 0),
           'T': Node('T', None, [('S',1), ('U',1), ('W',1)], (2,4), 0),
           'U': Node('U', None, [('O',1), ('T',1)], (3,4), 0),
           'V': Node('V', None, [('Q',1), ('Y',1)], (5,4), 0),
           'W': Node('W', None, [('T',1)], (2,5), 0),
           'X': Node('X', None, [('Y',1)], (4,5), 0),
           'Y': Node('Y', None, [('Y',1), ('X',1)], (5,5), 0)
          }
  #defining the parent node
  parentnode=initialstate

  #calculating the parent's cost
  parentcost = math.sqrt(
    (graph[goalstate].heuristic[0] - graph[initialstate].heuristic[0])**2
    +
    (graph[goalstate].heuristic[1] - graph[initialstate].heuristic[1])**2
  )
  #calculating the cost of the minchild
  #not sure why we are subtracting 1
  minChildCost=parentcost-1


  #now defining the conditions where we go to a node and call it a parent, then we check it's children
  #to look for the child with the minimum cost(local maxima).

  #we repeat the process until we reach the goal state(global maxima).

  #usually this method does not yield the goal state rather it gets stuck on a local maxima.
  #for that case we will solve this problem using local beam search

  while parentnode!=goalstate:
    #bestnode is the node with the minimum cost at the moment
    bestnode = parentnode
    minChildCost=parentcost
    #appending the checked node (which will technically be a parentnode) to the explored list
    #we are basically referring the current node (that we are present on at the moment) as the parent node
    explored.append(parentnode)

    #looking for the next node with the minimum cost which we will move towards
    #this node will be one of the childrens of the current node(parent node)
    for child in graph[parentnode].actions:
      #graph[parentnode].actions is referring to the list of children present in the graph dictionary corresponding to the parentnode key
      if child[0] not in explored:
        #calculating the new cost
        childcost = math.sqrt(
          (graph[goalstate].heuristic[0] - graph[child[0]].heuristic[0])**2
          +
          (graph[goalstate].heuristic[1] - graph[child[0]].heuristic[1])**2
          )
        #checking if childcost is lesser than the current minchildcost
        if childcost<minChildCost:
          bestnode=child[0]
          minChildCost=childcost

    #checking if the bestnode is equal to the parentnode(its the case where either we have reached the goal state)
    #(or are stuck at some local maxima)
    if bestnode==parentnode:
      break
    #if thats not the case then, make the current node as the parent node and move forward
    parentnode = bestnode
    parentcost = minChildCost
    #appending the node to the solution list
    solution.append(parentnode)

  return solution


#main
solution = hillclimbing('A','Y')
print(solution)

