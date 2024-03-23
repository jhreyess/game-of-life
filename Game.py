import math
from Grid import Grid

class Game:
    def __init__(self, window, cell_type='hexa'):
        self.window = window
        self.running = True
        self.stop = True
        self.clicking = False

        # Size of cells
        height = window.screen.get_height()
        width = window.screen.get_width()
        resolution = window.resolution

        self.rows = int(height/resolution)
        self.cols = int(width/resolution)
        self.cell_type = cell_type
        self.grid = self.make2DArray(resolution, self.cell_type)

    def update(self):
        self.grid.update()

    def draw(self):
        self.grid.draw(self.window.screen)
    
    # Create a new array with random values
    def make2DArray(self, resolution, cell_type):
        if(cell_type == 'hexa'):
            offset = abs(resolution * math.cos(math.radians(30)) - resolution)
            self.cols += math.ceil((offset * (self.cols)) / resolution)
        grid = Grid(self.rows, self.cols, resolution, cell_type)
        grid.randomize_state()
        return grid
    
    def drawAt(self, position):
        column = int((position[0]/self.window.screen.get_width())*self.cols)
        row = int((position[1]/self.window.screen.get_height())*self.rows)
        self.grid.drawAt((column, row))