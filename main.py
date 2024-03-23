import pygame
from WindowManager import WindowManager
from Game import Game

pygame.init()
clock = pygame.time.Clock()

# Set up the game window
wm = WindowManager(resolution=60)
wm.set_caption("Game Of Life!")

game = Game(wm)
while game.running:
    
    wm.screen.fill((255,255,255))

    if not game.stop:
        game.update()
    game.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False

        # Drawing on Grid
        if event.type == pygame.MOUSEBUTTONDOWN or game.clicking:
            game.clicking = True
            pos = pygame.mouse.get_pos()
            game.drawAt(pos)

        # Stop drawing
        if event.type == pygame.MOUSEBUTTONUP:
            game.clicking = False

        # Handle key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game.stop = not game.stop
                if game.stop:
                    wm.set_caption("Game Of Life - Stopped!")
                else:
                    wm.set_caption("Game Of Life - Playing...")
            if event.key == pygame.K_x:
                wm.set_caption("Game Of Life - Reset!")
                game.grid.clean_state()
                game.stop = True
            if event.key == pygame.K_r:
                wm.set_caption("Game Of Life - Randomize!")
                game.grid.clean_state()
                game.grid.randomize_state()
                game.stop = True

    if(not game.stop):
        clock.tick(30)
    pygame.display.flip()

pygame.quit()