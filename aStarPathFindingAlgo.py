import pygame
import math
from queue import PriorityQueue

WIDTH = 800
# Setting the display as a square
WIN = pygame.display.set_mode((WIDTH, WIDTH))

pygame.display.set_caption("A* Path Finding Algorithm")

#Setting RGB values for the Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:
    """
    This class allows us to keep track of the different blocks in the visualisation. In the algorithm, these blocks are equivalent to the nodes
    It needs to keep track of several feature to achieve its function as a node:
     (1) Position: row and column
     (2) Width
     (3) Neighbours
     (4) Color:
    """
    def __init__(self, row, column, total_rows):
        """
        - Row and Column: This gives us the relative position number with respect to the top left corner
        - x & y: This give us the pixel coordinate of the node, where the width is the size of each block
        - Starting color of each block is gonna be white
        """
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        """
        Block has been considered in the algoithm
        """
        return self.color == RED

    def is_open(self):
        """
        """
        return self.color == GREEN

    def is_barrier(self):
        """
        The color of the obstacle or barrier
        """
        return self.color == BLACK

    def is_start(self):
        """
        The color of the starting node
        """
        return self.color == ORANGE

    def is_end(self):
        """
        The color of the ending node
        """
        return self.color == 
