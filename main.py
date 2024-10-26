
import pygame
import sys
from dijkstra import *
from graph import *

width, height = 400, 450 
rows, cols = 10, 10
cell_size = width // cols
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 138, 138)
GREEN = (15, 255, 80)
GREY = (215, 215, 215)
BUTTON_BG = (180, 180, 180)

button_width, button_height = 100, 40
button_x, button_y = (width - button_width) // 2, 410  

grid = [
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0]
]

points = []

class Map:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Grid Map")
        self.selected_boxes = []
        self.run_game()

    def run_game(self):
        while True:
            self.screen.fill(WHITE)
            self.draw_grid()
            self.draw_refresh_button()
            self.choosing_points()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_button_click()

            if len(points) == 2:
                self.find_shortest_path()

            pygame.display.flip()

    def choosing_points(self):
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            row, col = pos[1] // cell_size, pos[0] // cell_size
            if pos[1]>400:
                return 
            if grid[row][col] == 0:     
                if len(points) < 2 and (row, col) not in points and pos[1] < 400:
                    points.append((row, col))
                    self.selected_boxes.append((row, col))

        for row, col in self.selected_boxes:
            pygame.draw.rect(self.screen, BLUE, (col * cell_size, row * cell_size, cell_size, cell_size))

    def draw_grid(self):
        for row in range(rows):
            for col in range(cols):
                color = WHITE if grid[row][col] == 0 else BLACK
                pygame.draw.rect(self.screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))
                pygame.draw.rect(self.screen, GREY, (col * cell_size, row * cell_size, cell_size, cell_size), 1)

    def highlight_path(self, path):
        for row, col in path:
            pygame.draw.rect(self.screen, GREEN, (col * cell_size, row * cell_size, cell_size, cell_size))

    def find_shortest_path(self):
        graph = grid_to_graph(grid)
        start, end = points[0], points[1]
        path = shortest_path(graph, start, end)
        if path:
            self.highlight_path(path)

    def draw_refresh_button(self):
        pygame.draw.rect(self.screen, BUTTON_BG, (button_x, button_y, button_width, button_height))
        font = pygame.font.SysFont(None, 36)
        text = font.render("Refresh", True, WHITE)
        self.screen.blit(text, (button_x + 5, button_y + 8))

    def handle_button_click(self):
        if pygame.mouse.get_pressed()[0]:    
            pos = pygame.mouse.get_pos()
            if pos[1]>400 and button_x<=pos[0]<=button_x+button_width:
                self.reset_game()

    def reset_game(self):
        global points
        points = []
        self.selected_boxes = []
        self.screen.fill(WHITE)

if __name__ == "__main__":
    Map()
