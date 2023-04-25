# Sample graph represented as a dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# BFS algorithm in Python
from collections import deque

def bfs(graph, start):
    visited, queue = set(), deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# DFS algorithm in Python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

# BFS algorithm driver code
visited = set()
print("BFS Traversal:")
for node in graph:
    if node not in visited:
        bfs(graph, node)

# DFS algorithm driver code
visited = set()
print("\nDFS Traversal:")
for node in graph:
    if node not in visited:
        dfs(graph, node, visited)
