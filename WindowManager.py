import pygame

class WindowManager:
    def __init__(self, screen_width=1200, screen_height=800,  resolution=10):
        # Initial setup
        width = screen_width
        height = screen_height
        self.resolution = resolution
        self.screen = pygame.display.set_mode((width, height))

    def set_caption(self, title="Game Of Life!"):
        pygame.display.set_caption(title)        
    
    # Draws all the cells
    def draw(self):
        self.grid.draw(self.screen)

    # Update Logic
    def update(self, stop):
        if not stop:
            # Count the number of active neighbors cells
            for row in self.grid:
                for cell in row:
                    cell.count(self.grid)
            
            # Updates all the values
            for row in self.grid:
                for cell in row:
                    cell.update()