
from graph import *
from main import *
import heapq

# Dijkstra's algorithm to find the shortest path
def shortest_path(graph, start, end):
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        for neighbor in graph[current_node]:
            distance = current_distance + 1  
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_nodes[current]

    return path[::-1]  