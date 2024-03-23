from random import random
from Cell import Cell

class Grid:
    def __init__(self, num_rows, num_cols, cell_size, cell_type):
        self.rows = num_rows
        self.cols = num_cols
        self.cell_size = cell_size
        self.cell_type = cell_type
        self.cells = self.create_cells()
        self.cells_to_be_updated = []
        self.cells_to_be_drawn = []
        print(self.rows, self.cols)

    def update(self):        
        self.cells_to_be_drawn.clear()
        self.cells_to_be_updated.clear()
        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.cells[i][j]
                neighbors = self.__count_neighbors((i, j))
                cell.set_next_state(neighbors)

                # If it changed its state it must be updated
                # if it stays living it must be re-drawn
                if cell.next_state != cell.isAlive:
                    self.cells_to_be_updated.append(cell)
                elif cell.isAlive:
                    self.cells_to_be_drawn.append(cell)

        # Update each cell
        for cell in self.cells_to_be_updated:
            cell.update()
            # If the cell was born it must be drawn
            if cell.isAlive:
                self.cells_to_be_drawn.append(cell)

    def __count_neighbors(self, pos):
        neighbors = 0
        for a in range(-1, 2):
            for b in range(-1, 2):
                if a == 0 and b == 0:
                    continue
                row = (pos[0] + b + self.rows) % self.rows
                col = (pos[1] + a + self.cols) % self.cols
                neighbors += self.cells[row][col].isAlive
        return neighbors

    def draw(self, screen):
        for cell in self.cells_to_be_drawn:
            cell.draw(screen)
    
    def drawAt(self, pos):
        col, row = pos
        if col >= 0 and col < self.cols and row >= 0 and row < self.rows:
            cell = self.cells[row][col]
            cell.next_state = 1
            cell.update()
            self.cells_to_be_drawn.append(cell)
    
    def create_cells(self):
        cells = []
        for row in range(self.rows):
            row_cells = []
            for col in range(self.cols):
                x = col * self.cell_size
                y = row * self.cell_size
                cell = Cell(0, x, y, self.cell_size, self.cell_type)
                row_cells.append(cell)
            cells.append(row_cells)
        return cells
    
    def randomize_state(self):
        for row in self.cells:
            for cell in row:
                cell.isAlive = 0 if (random() < 0.5) else 1
                if cell.isAlive:
                    self.cells_to_be_drawn.append(cell)

    def clean_state(self):
        for row in self.cells:
            for cell in row:
                cell.isAlive = 0
        self.cells_to_be_drawn.clear()