import pygame

# Cell class
class Cell:
    def __init__(self, value, posX, posY, size):
        self.isAlive = value 
        self.color = (0,0,0)
        self.x = posX
        self.y = posY
        self.width = size
        self.next_state = self.isAlive

    def draw(self):
        raise NotImplementedError
        
    # Determines whether the cell lives or dies
    def set_next_state(self, neighbors):
        # Dies if it has less than 2 or more than 3 neighbors
        if(self.isAlive and (neighbors < 2 or neighbors > 3)):
            self.next_state = 0
        # A cell is born if it has exactly 3 neighbors
        elif(not self.isAlive and neighbors == 3):
            self.next_state = 1
        # Remains the same
        else:
            self.next_state = self.isAlive

    def update(self):
        self.isAlive = self.next_state
        self.next_state = 0

class SquareCell(Cell):
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))
