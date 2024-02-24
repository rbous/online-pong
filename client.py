import pygame
from network import Network

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

clientNumber = 0


class Player:
    def __init__(self, x, y=50, width=10, height=70, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.velocity = 5

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y -= self.velocity

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += self.velocity

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

"""
def read_pos(string):
    string = string.split(",")
    return int(string[0]), int(string[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])
"""

def redraw_window(player1, player2, win=window):
    win.fill((0, 0, 0))
    player1.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    running = True
    n = Network()
    start_pos = int(n.get_pos())

    p1 = Player(start_pos)
    p2 = Player(SCREEN_WIDTH - 50)

    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        p2pos = int(n.send(str(p1.y)))
        p2.y = p2pos
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        p1.move()
        redraw_window(p1, p2)


main()
