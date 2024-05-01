import heapq

def dijkstra(graph, start):
    # Initialize distances from the start node to all other nodes as infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to store nodes to be explored next
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip if we have already found a shorter path to the current node
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node + ":")
for node, distance in shortest_distances.items():
    print("To", node + ":", distance)
