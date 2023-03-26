class Node: 
   
   def __init__(self, state, parent, action, totalCost):
    self.state = state
    self.parent = parent
    self.action = action
    self.totalCost = totalCost

def actionSequence(graph, initialState,goalState):
  solution = [goalState]
  currentParent = graph[goalState].parent
  while currentParent!=None:
    solution.append(currentParent)
    currentParent= graph[currentParent].parent
  solution.reverse()
  return solution
    
def DFS():

  initialState= 'Arad'
  goalState= 'Bucharest'

    
  graph = {
    'Neamt' : Node('Neamt', None, ['Iasi'], None),
    'Iasi' : Node('Iasi', None, ['Neamt','Vaslui'], None),
    'Vaslui' : Node('Vaslui', None, ['Urziceni','Iasi'], None),
    'Urziceni' : Node('Urziceni', None, ['Vaslui','Hirsova','Bucharest'], None),
    'Hirsova' : Node('Hirsova', None, ['Urziceni','Vaslui','Eforie'], None),
    'Eforie' : Node('Eforie', None, ['Hirsova'], None),
    'Bucharest' : Node('Bucharest', None, ['Urziceni','Giurgiu','Pitesti','Fagarus'], None),
    'Giurgiu' : Node('Giurgiu', None, ['Bucharest'], None),
    'Pitesti' : Node('Pitesti', None, ['Rimnicu Vilcea','Bucharest','Craiova'], None),
    'Craiova' : Node('Craiova', None, ['Pitesti','Rimnicu Vilcea','Drobeta'], None),
    'Rimnicu Vilcea' : Node('Rimnicu Vilcea', None,['Pitesti','Craiova','Sibiu'], None),
    'Fagarus' : Node('Fagarus', None, ['Sibiu','Bucharest'], None),
    'Sibiu' : Node('Sibiu', None, ['Fagarus','Rimnicu Vilcea'], None),
    'Oradea' : Node('Oradea', None, [ 'Sibiu','Zerind'], None),
    'Zerind' : Node('Zerind', None, ['Arad','Oradea'], None),
    'Arad' : Node('Arad', None, ['Zerind','Sibiu','Timisoara'], None),
    'Timisoara' : Node('Timisoara', None, ['Arad','Lugoj'], None),
    'Lugoj' : Node('Lugoj', None, ['Timisoara','Mehadia'], None),
    'Mehadia' : Node('Mehadia', None, ['Lugoj','Drobeta'], None),
    'Drobeta' : Node('Drobeta', None, ['Mehadia','Craiova'], None),   
}

  frontier = [initialState]
  explored = []

  while len(frontier)!=0:
    currentNode = frontier.pop(len(frontier)-1)
    explored.append(currentNode)
    currentChildren = 0

    for child in graph[currentNode].action:
      if child not in frontier and child not in explored:
        graph[child].parent = currentNode

        if graph[child].state ==  goalState:
          return actionSequence(graph, initialState, goalState)
        currentChildren+=1
        frontier.append(child)
        
    if currentChildren == 0:
      del explored[len(explored)-1]

solution = DFS()
print (solution)

