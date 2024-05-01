def floyd_warshall(graph):
    # Initialize distance matrix with shortest distances between all pairs of vertices
    distance = {i: {j: float('inf') for j in graph} for i in graph}
    for i in graph:
        distance[i][i] = 0
    for i in graph:
        for j in graph[i]:
            distance[i][j] = graph[i][j]
    
    # Update distance matrix using Floyd-Warshall algorithm
    for k in graph:
        for i in graph:
            for j in graph:
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    return distance

# Example usage:
graph = {
    'A': {'B': 3, 'C': 8, 'E': -4},
    'B': {'D': 1, 'E': 7},
    'C': {'B': 4},
    'D': {'A': 2, 'C': -5},
    'E': {'D': 6}
}

shortest_distances = floyd_warshall(graph)
print("Shortest distances between all pairs of vertices:")
for source in graph:
    for target in graph:
        print("From", source, "to", target + ":", shortest_distances[source][target])
