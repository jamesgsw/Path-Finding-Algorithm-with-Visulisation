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
    #This class allows us to keep track of the different blocks in the visualisation. In the algorithm, these blocks are equivalent to the nodes
    def __init__(self, row, col, width, total_rows):
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

    """
    There are many methods that I've created below, but they can be grouped into several overarching functions they are trying to solve
    (A) get_pos:
    This method return the row and column of the particular block in terms of relative position
    (B) is_someStatus:
    This method checks the status of the block with the different permutation of status/color of the block. Therefore, it'll return a boolean value of the status of the block
    (C) make_someStatus:
    This method changes the status of the block. It does not return any vlaue
    """
    # (A) get_pos
    def get_pos(self):
        return self.row, self.col

    # (B) is_someStatus:
    def is_closed(self):
        """Block has been considered in the algorithm"""
        return self.color == RED
    def is_open(self):
        """Block is in the open set"""
        return self.color == GREEN
    def is_barrier(self):
        """The color of the obstacle or barrier"""
        return self.color == BLACK
    def is_start(self):
        """The color of the starting node"""
        return self.color == ORANGE
    def is_end(self):
        """The color of the ending node"""
        return self.color == TURQUOISE
    def reset(self):
        """Setting the color to reset a block"""
        self.color = WHITE

    # (C) Setting the status of the block.
    def make_start(self):
        self.color = ORANGE
    def make_closed(self):
        self.color = RED
    def make_open(self):
        self.color = GREEN
    def make_barrier(self):
        self.color = BLACK
    def make_end(self):
        self.color = TURQUOISE
    def make_path(self):
        self.color = PURPLE

    # (D) Other methods for the block object
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self,grid):
        """
        Inputs: Grid object
        Outputs: No output, updating the Grid object
        Method: We need to check the 4 axis(up, down, left, right) neighbour block of the current block to check if it's a barrier
        """
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): #DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): #UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): #LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): #RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

    def __lt__(self, other):
        """"This method compares 2 block and return a boolean values"""
        return False

""""
Creating our A* Algo
f(n) = g(n) + h(n)
There are 2 components to the A* Algorithm which are the (1) Cost Function, g(n) and (2) Heuristic Function, h(n).
"""

# (1) Cost Function, g(n)
def algorithm(draw, grid, start, end):
    """
    Inputs: draw method that creates each block, 2D array of every block object
    Outputs:
    Methods: Crreating the search algorithm where we perform heursitic on the best path by searching the current node and its neighbor
    """
    count = 0
    open_set = PriorityQueue() #Package we installed at the start that allows us to keep track the nodes in the open set, allows us to get the mimimum count from the queue when we use the .get() method
    open_set.put((0, count, start)) #(Add start node with original F score of 0, when the node was added, starting node)
    came_from = {} #Keeping track of our path, where each node links to the other, so when the best path is found, we can trace back the shortest path

    #Setting the initial f_score, g_score and h_score when we have defined the starting and ending node
    g_score = {spot: float("inf") for row in grid for spot in row} #Set each block to have a value of infinity with a nested for loop
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row} #Set each block to have a value of infinity with a nested for loop
    f_score[start] = h(start.get_pos(), end.get_pos()) #Since the g_score is zero, our f_score is only the heuristic of the distance from start to end node

    open_set_hash = {start}
    while not open_set.empty(): #Run until the open set has been exhausted

        for event in pygame.event.get(): #Handle when the user quits the game
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2] #get current node
        open_set_hash.remove(current) #Since we are not considering the current node, we can remove it from the open set

        if current == end: #Shortest Path found, then we can draw the path
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1 #The neighbor is 1 value past the curent node therefore it's + 1
            if temp_g_score < g_score[neighbor]: #If better g_score found, them update path
                came_from[neighbor] = current #Update the came from dict to where this neighbor node came from, which is from our current node that has the shortest path
                g_score[neighbor] = temp_g_score #Since this is our new shortest path in the if statement above, therefore we can reassign the g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor)) #Adding the neighbor node to the open set in the open_set queue
                    open_set_hash.add(neighbor) #The neighbor is part of the open set
                    neighbor.make_open() #Since now the neighbor is part of the open set, we need to update the color

        draw()
        if current != start:
            current.make_closed()

    return False

# (2) Heuristic Function, h(n)
def h(p1, p2):
    """
    Inputs: Pixel position of node in investigation and end node
    Ouptuts: Positive value of pixel length between node in invesitgation and end node
    Method: Manhanttan distance - Taking the absolute distance from node in investigation and end node
    """
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

"""
Draw the best path
"""
def reconstruct_path(came_from, current, draw):
    """
    Inputs: List of optimal nodes, starting node, draw object
    Outputs: Returns nothing
    Method: Draw most optimal path
    """
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

"""
Creating a container which holds the status/color of each block
"""
def make_grid(rows, width):
    """
    Inputs: Number of rows and the width of the entire grid
    Outputs: The array of the dimension of the grid
    Method: Nested for loop to input the dimension of the grid
    """
    grid = []
    gap = width // rows #the width of the entire grid divided by the number of rows to get the pixel size of each block
    for i in range(rows):
        grid.append([]) #Creating a list for every row in this 2D symmetrical array
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid

"""
Creating the grid columns visual
"""
def draw_grid(win, rows, width):
    """
    Inputs: Object of the pygame display, number of rows and the width of the entire grid
    Outputs: No output, updating the win object
    Method: We iterate through the drawing the vertical lines for every horizontal line
    """
    gap = width // rows
    for i in range(rows): #Drawing the horizontal lines
        pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap))
        for j in range(rows): #Drawing the vertical lines
            pygame.draw.line(win, GREY, (j*gap, 0), (j*gap, width))

"""
Draw the color of block and instantiate the draw_grid method
"""
def draw(win, grid, rows, width):
    """
    Inputs: Object of the pygame display, grid object of the 2D array, number of rows and the width of the entire grid
    Outputs: No output, updating the win object
    Method: Fills the block with the respective color and create the grid
    """
    win.fill(WHITE)

    for row in grid:  #Draw the color for a particular block
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width) #Draw the grid
    pygame.display.update()

"""
Finding mouse position in grid
"""
def get_clicked_pos(pos, rows, width):
    """
    Inputs: Mouse position, number of rows and the width of the entire grid
    Outputs: Row and Column number where the mouse is at
    Method: We take the pixel position of the mouse and get an rounded off integer value of the row and column value corresponding to the grid
    """
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

def main(win, width):
    """
    Inputs: Object of the pygame display and the width of the entire grid
    Outputs:
    Method: This ties in all the other methods, where we link the mouse functions to the methods
    """
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get(): #This method gets all the events that pygame records
            if event.type == pygame.QUIT: # When we quit the program
                run = False

            if pygame.mouse.get_pressed()[0]: #Index 0 is the left mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width) #Using our defined get_clicked_pos method to get the row and column value
                #After we get the row and column value, then we can get index to that particular block
                spot = grid[row][col]
                if not start and spot != end: #Defining the start node
                    start = spot
                    start.make_start()
                elif not end and spot != start: #Defning the end node
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]: #Index 2 is the right mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width) #Using our defined get_clicked_pos method to get the row and column value
                #After we get the row and column value, then we can get index to that particular block
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pygame.quit()

main(WIN, WIDTH)
