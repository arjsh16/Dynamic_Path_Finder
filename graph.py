
from main import *
from dijkstra import *

def grid_to_graph(grid):
    graph = {}
    rows = len(grid)
    cols = len(grid[0])

    def get_neighbors(row, col):
        neighbors = []
        if row > 0 and grid[row - 1][col] == 0:  
            neighbors.append((row - 1, col))
        if row < rows - 1 and grid[row + 1][col] == 0: 
            neighbors.append((row + 1, col))
        if col > 0 and grid[row][col - 1] == 0: 
            neighbors.append((row, col - 1))
        if col < cols - 1 and grid[row][col + 1] == 0: 
            neighbors.append((row, col + 1))
        return neighbors

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:  
                graph[(row, col)] = get_neighbors(row, col)

    return graph
