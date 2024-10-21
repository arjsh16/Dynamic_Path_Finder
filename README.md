# Dynamic_Path_Finder

This Python project is a pathfinding visualizer built using Pygame. It implements Dijkstra's Algorithm to find and display the shortest path between two points on a grid. Users can interactively set start and end points, with the algorithm dynamically calculating and highlighting the optimal path around obstacles.

## Pathfinding Visualizer with Dijkstra's Algorithm

This project is a Python-based visual pathfinding tool that uses Dijkstra's Algorithm to find the shortest path between two points on a 2D grid. Built with Pygame, it features an interactive grid where you can place a start point, an endpoint, and navigate around obstacles.

## Features
- Visual representation of the grid where white cells represent roads and black cells represent obstacles.
- Select your start and end points, and the program calculates the shortest path using Dijkstra’s Algorithm.
- The calculated path is highlighted in green.
- Interactive grid with the ability to reset and experiment with different paths.
- Simple and intuitive UI built with Pygame.

## How to Run

### Clone the repository:
    git clone https://github.com/arjsh16/Dynamic_Path_Finder.git
    cd pathfinding-visualizer
### Install dependencies(Make sure you have python 3 is installed):
    pip install pygame
### Run the project:
    python main.py
## Future improvements
- Adding support for more pathfinding algorithms (e.g., A*).
- Allow users to dynamically place obstacles on the grid.
- Add more grid sizes and performance optimization for larger grids.
