import heapq

def prim(graph):
    start_node = next(iter(graph))
    visited = {start_node}
    mst = []
    edges = [(weight, start_node, neighbor) for neighbor, weight in graph[start_node].items()]
    heapq.heapify(edges)

    while edges:
        weight, node1, node2 = heapq.heappop(edges)
        if node2 not in visited:
            mst.append((node1, node2, weight))
            visited.add(node2)
            for neighbor, weight in graph[node2].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, node2, neighbor))

    return mst

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8},
    'D': {'B': 5, 'C': 8}
}
minimum_spanning_tree = prim(graph)
for edge in minimum_spanning_tree:
    print(edge)
