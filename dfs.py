graph={
    'a':['b','c'],
    'b':['d','e'],
    'c':['f'],
    'd':[],
    'e':['f'],
    'f':[]
}
#dfs
def dfs(graph,start,visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    
    for neibours in graph[start]:
        if neibours not in visited:
            dfs(graph,neibours,visited)
  
#Driver code          
visited = set()
print("\n DFS Traverasl:")
            
for node in graph:
    if node not in visited:
        dfs(graph,node,visited)
    
#bfs           
from collections import deque

def bfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)        
                
visited = set()
print("BFS Traversal:")
for node in graph:
    if node not in visited:
        bfs(graph, node, visited)
