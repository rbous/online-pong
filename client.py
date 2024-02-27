import pygame
from network import Network
from player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")


def redraw_window(player1, player2, win=window):
    win.fill((0, 0, 0))
    player1.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    running = True
    n = Network()
    p1 = n.get_p()
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        p2 = n.send(p1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        p1.move()
        redraw_window(p1, p2)


main()
