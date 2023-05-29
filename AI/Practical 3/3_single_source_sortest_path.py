import heapq

def dijkstra(graph, source):
    # Step 1: Create a dictionary to store the shortest distances from the source node
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    # Step 2: Create a priority queue to store the nodes to be visited
    priority_queue = [(0, source)]

    while priority_queue:
        # Step 3: Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Step 4: Check if the current node has already been visited
        if current_distance > distances[current_node]:
            continue

        # Step 5: Explore the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Step 6: Update the distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

source_node = 'A'
shortest_distances = dijkstra(graph, source_node)
print(shortest_distances)
