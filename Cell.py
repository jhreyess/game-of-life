import pygame
import math 

# Cell class
class Cell:
    def __init__(self, value, posX, posY, size, shape):
        self.isAlive = value 
        self.color = (0,0,0)
        self.x = posX
        self.y = posY
        self.size = size
        self.next_state = self.isAlive
        self.shape = shape
        if(self.shape == 'circle'):
            self.centerX = self.x + self.size * 0.5
            self.centerY = self.y + self.size * 0.5
        elif(self.shape == 'hexa'):
            self.centerX = self.x + self.size * 0.5
            self.centerY = self.y + self.size * 0.5
            if((self.x/self.size) % 2 != 0):
                self.centerY += self.size * math.sin(math.radians(30))
            offset = self.size * math.cos(math.radians(30)) - self.size
            self.centerX += offset * (self.x/self.size)
            self.points = self._calculate_hexagon_points(self.centerX, self.centerY, self.size * 0.5)

    def draw(self, screen):
        if(self.shape == 'square'):
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
        elif(self.shape == 'circle'):
            pygame.draw.circle(screen, self.color, (self.centerX, self.centerY), self.size * 0.5)
        elif(self.shape == 'hexa'):
            pygame.draw.polygon(screen, self.color, self.points)
            
        
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

    def _calculate_hexagon_points(self, centerX, centerY, radius):
        points = []
        for i in range(6):
            angle_rad = math.radians(60 * i)
            x = centerX + radius * math.cos(angle_rad)
            y = centerY + radius * math.sin(angle_rad)
            points.append((x, y))
        return points